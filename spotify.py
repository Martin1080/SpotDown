from spotdl import Spotdl
import asyncio

import os
from dotenv import load_dotenv

load_dotenv()

# Global client credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Initialize Spotdl globally once
spotdl_client = Spotdl(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

def ensure_loop():
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

def prepare_spotdl(metadata):
    """
    Updates the global spotdl instance with the current thread's loop and requested bitrate.
    """
    ensure_loop()
    # Update loop to the current thread's loop (required for asyncio in threads)
    spotdl_client.downloader.loop = asyncio.get_event_loop()
    # Update settings
    print(f"DEBUG: Setting bitrate to {metadata['bitrate']}")
    spotdl_client.downloader.settings["bitrate"] = metadata["bitrate"]
    return spotdl_client

"""def download(song):
    songs = spotdl.search([song])

    results = spotdl.download_songs(songs)
    song, path = spotdl.download(songs[0])"""

def download_single(song, metadata):
    spotdl = prepare_spotdl(metadata)
    downloaded_song = {"path": [], "metadata": []}
    # Use spotdl to search for and download the song
    songs = spotdl.search([song])
    results = spotdl.download_songs(songs)
    downloaded_song["path"].append(results[0][1])
    downloaded_song["metadata"].append(results[0][0].cover_url)
    return downloaded_song

def download_multiple(song, metadata):
    spotdl = prepare_spotdl(metadata)
    downloaded_songs = {"playlist": [], "songs": [], "metadata": []}
    # Use spotdl to search for and download the song
    songs = spotdl.search([song])
    results = spotdl.download_songs(songs)
    downloaded_songs["playlist"].append(results[0][0].list_name)
    if song.startswith('https://open.spotify.com/playlist'):     
        # Playlist cover usually comes from the first song or separate metadata query, 
        # but Song object might not store the *playlist* cover, only the album cover.
        # However, v3 code used song_list.cover_url.
        # In v4 Song object, we don't seem to have playlist cover directly.
        # But let's check if we can get it from the first song's cover or similar.
        # Actually, let's use the first song's cover for now as fallback or check if list_url gives us hints.
        # Wait, the v4 Song definition has `cover_url`.
        downloaded_songs["metadata"].append(results[0][0].cover_url)
    elif song.startswith('https://open.spotify.com/album'):
        print(results)
        downloaded_songs["metadata"].append(results[0][0].cover_url)
    for i in range(len(results)):
        downloaded_songs["songs"].append(results[i][1])
    return downloaded_songs

        


