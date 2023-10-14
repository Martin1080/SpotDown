from spotdl import Spotdl
spotdl = Spotdl(client_id='4b53766c6ce84022b1b041d91a320975', client_secret='874cb2f3555542b8a16dad888b19adcc')
"""def download(song):
    songs = spotdl.search([song])

    results = spotdl.download_songs(songs)
    song, path = spotdl.download(songs[0])"""

def download_single(song, metadata):
    downloaded_song = {"path": [], "metadata": []}
    # Use spotdl to search for and download the song
    spotdl.downloader.bitrate = metadata["bitrate"]
    songs = spotdl.search([song])
    results = spotdl.download_songs(songs)
    downloaded_song["path"].append(results[0][1])
    downloaded_song["metadata"].append(results[0][0].cover_url)
    return downloaded_song

def download_multiple(song, metadata):
    downloaded_songs = {"playlist": [], "songs": [], "metadata": []}
    # Use spotdl to search for and download the song
    spotdl.downloader.bitrate = metadata["bitrate"]
    songs = spotdl.search([song])
    results = spotdl.download_songs(songs)
    downloaded_songs["playlist"].append(results[0][0].song_list.name)
    if song.startswith('https://open.spotify.com/playlist'):     
        downloaded_songs["metadata"].append(results[0][0].song_list.cover_url)
    elif song.startswith('https://open.spotify.com/album'):
        print(results)
        downloaded_songs["metadata"].append(results[0][0].cover_url)
    for i in range(len(results)):
        downloaded_songs["songs"].append(results[i][1])
    return downloaded_songs

        


