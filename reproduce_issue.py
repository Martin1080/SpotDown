
import threading
import traceback
import spotify

def run_download():
    metadata = {
      "bitrate": "320k",
      "format": "flac",
    }
    song_url = "https://open.spotify.com/track/5rlMVKnvE6ZSzNCs8ZyHqU?si=1c1be553d9fc4ded"
    try:
        print("Starting download...")
        spotify.download_single(song_url, metadata)
        print("Download finished.")
    except Exception as e:
        print("Download failed:")
        traceback.print_exc()

if __name__ == "__main__":
    t = threading.Thread(target=run_download, name="TestThread")
    t.start()
    t.join()
