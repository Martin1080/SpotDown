[SpotDown](https://github.com/Martin1080/Discord.php) 👽
====

Official [SpotDown](https://github.com/Martin1080/SpotDown) Documentation

Discover the ultimate Spotify Downloader – Your gateway to converting your favorite Spotify tracks into high-quality MP3 files at up to 320kbps. Enjoy your music offline, anytime, anywhere!

SpotDown is an open source website that is built using [spotDL](https://spotdl.readthedocs.io/en/latest/) and [Flask](https://flask.palletsprojects.com/en/3.0.x/) in Python allows you to to download songs/playlists/albums from [Spotify](https://open.spotify.com) to your device. Format is mp3 and user can choose between (8, 16, 32, 64, 96, 128, 192, 256, 320)kbps.


## Before you start

Before you start using SpotDown note that We do not host any copyrighted materials. Instead, we utilize third-party sources to provide our users with the content they seek. We should not be held liable for any content or materials accessed through our platform..

Adwantage is Python and Flask knowedge, but it isn't necessary.


## Setup 🖥

### Requirements
- [Python 3.10](https://www.python.org) or newer (Compatible up to Python 3.14 with patches)
- `python-dotenv` and other dependencies in `requirements.txt`

### Authorization
1. Create a `.env` file in the root directory.
2. Add your Spotify API credentials (Get them from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)):
   ```env
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   ```

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If you are using Python 3.14, you may need to use the patched version of `spotdl` included in `temp_deps` or patch it manually.*

2. Run the application:
   ```bash
   python app.py
   ```
   
3. Open your browser at `http://127.0.0.1:5000`

### Features
- Download songs, albums, and playlists from Spotify.
- Selectable quality (64kbps - 320kbps).
- Metadata embedding (Cover art, Artist, etc.).
- Modern, responsive Dark Mode UI.

**Disclaimer**: This tool is for educational purposes only. We do not host any copyrighted material.
