from flask import Blueprint, render_template, send_file, request, jsonify
import spotify as spotify
import os
import zipfile
import time
import threading
import shutil

views = Blueprint(__name__, "views")
song_path = ""
text_variable = ""
def default_metadata():
    return {
        "bitrate": spotify.DEFAULT_BITRATE,
        "format": "flac",
    }

metadata = default_metadata()

def safe_filename(name, default_name="download"):
    safe_name = "".join(char for char in str(name or default_name) if char not in '<>:"/\\|?*').strip()
    return safe_name or default_name

def get_file_size_in_mb(file_path):
    # Get the file size in bytes
    file_size_bytes = os.path.getsize(file_path)

    # Convert bytes to megabytes
    file_size_mb = file_size_bytes / (1024 * 1024)

    return file_size_mb


def delete_file_after_delay(path, duration):
    if song_path:
        time.sleep(duration)
        try:
            os.remove(path)
        except:
            pass

#@views.route('/')
#def index():
#    return render_template("download.html")

@views.route("/", methods=['GET', 'POST'])
def home():
    global text_variable, metadata
    song_url = "static/song.mp3"
    if request.method == 'POST':
        if 'text_input' in request.form:
            text_variable = request.form['text_input']
        if 'select_input' in request.form:
            metadata['bitrate'] = spotify.normalize_bitrate(request.form['select_input'])
        else:
            metadata['bitrate'] = spotify.normalize_bitrate(metadata.get('bitrate'))
        print(str(metadata['bitrate']) + "  " + str(text_variable))
        return jsonify({'text_variable': text_variable, 'select_variable': metadata['bitrate']})

    metadata['bitrate'] = spotify.DEFAULT_BITRATE
    return render_template(
        "index.html",
        song_url=song_url,
        bitrates=spotify.SUPPORTED_BITRATES,
        selected_bitrate=metadata['bitrate'],
    )

@views.route('/enter')
def enter():
    global song_path, text_variable, metadata
    try:
        metadata["bitrate"] = spotify.normalize_bitrate(metadata.get("bitrate"))
        #song_path = spotify.download("https://open.spotify.com/playlist/3sAlZQ32bYMdnH3vPZITty?si=a197db6137fd4760")
        if text_variable.startswith('https://open.spotify.com/playlist') or text_variable.startswith('https://open.spotify.com/album'):
            songs = spotify.download_multiple(text_variable, metadata)

            # Create a zip file to store the downloaded songs
            song_files = [os.fspath(song) for song in songs["songs"] if song and os.path.exists(song)]
            if not song_files:
                raise Exception("No songs were downloaded successfully.")

            playlist_name = safe_filename(songs["playlist"][0] if songs["playlist"] else "playlist")
            song_path = playlist_name + '.zip'
            print(str(songs))
            with zipfile.ZipFile(song_path, 'w') as zipf:
                for song in song_files:
                    zipf.write(song, os.path.basename(song))
                    os.remove(song)

            metadata = default_metadata()
            cover_url = songs["metadata"][0] if songs["metadata"] else ""
            return render_template("download.html", cover_url=cover_url, file_size=round(get_file_size_in_mb(song_path), 2), song_name=song_path)
        else:
            single_song = spotify.download_single(text_variable, metadata)
            temp_path = str(single_song["path"][0])
            dist_path = "static\\" + str(single_song["path"][0])
            shutil.move(temp_path, dist_path)
            song_path = dist_path
            text_variable = ""
            metadata = default_metadata()
            return render_template("download.html", cover_url=single_song["metadata"][0], file_size=round(get_file_size_in_mb(song_path), 2), song_name=song_path)
    except Exception as e:
        return render_template("error.html", exception=str(e), short=str(e)[0:26])
    

@views.after_request
def after_enter(response):
    global song_path
    delete_thread = threading.Thread(target=delete_file_after_delay, args=(song_path, 40,))
    delete_thread.start()
    return response

@views.route('/download')
def download():
    global song_path
    # Provide the path to your a.mp3 file
    path = song_path
    response = send_file(path, as_attachment=True)
    delete_thread = threading.Thread(target=delete_file_after_delay, args=(path,5,))
    delete_thread.start()
    return response
    

