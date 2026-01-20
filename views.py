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
metadata = {
  "bitrate": "320k",
  "format": "flac",
}

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
            metadata['bitrate'] = request.form['select_input']
        print(str(metadata['bitrate']) + "  " + str(text_variable))
        return jsonify({'text_variable': text_variable, 'select_variable': metadata['bitrate']})
    
    return render_template("index.html", song_url=song_url)

@views.route('/enter')
def enter():
    global song_path, text_variable, metadata
    try:
        #song_path = spotify.download("https://open.spotify.com/playlist/3sAlZQ32bYMdnH3vPZITty?si=a197db6137fd4760")
        if text_variable.startswith('https://open.spotify.com/playlist') or text_variable.startswith('https://open.spotify.com/album'):
            songs = spotify.download_multiple(text_variable, metadata)

            # Create a zip file to store the downloaded songs
            song_path = str(songs["playlist"][0]) + '.zip'
            print(str(songs))
            with zipfile.ZipFile(song_path, 'w') as zipf:
                for song in songs["songs"]:
                    zipf.write(song, os.path.basename(song))
                    os.remove(song)

            return render_template("download.html", cover_url=songs["metadata"][0], file_size=round(get_file_size_in_mb(song_path), 2), song_name=song_path)
        else:
            single_song = spotify.download_single(text_variable, metadata)
            temp_path = str(single_song["path"][0])
            dist_path = "static\\" + str(single_song["path"][0])
            shutil.move(temp_path, dist_path)
            song_path = dist_path
            text_variable = ""
            metadata = {
            "bitrate": "320k",
            "format": "flac",
            }
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
    

