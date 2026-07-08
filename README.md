[SpotDown](https://github.com/Martin1080/SpotDown)
====

Official [SpotDown](https://github.com/Martin1080/SpotDown) documentation.

SpotDown is an open source Spotify downloader web app built with [spotDL](https://spotdl.readthedocs.io/en/latest/) and [Flask](https://flask.palletsprojects.com/) in Python. It can download songs, albums, and playlists from [Spotify](https://open.spotify.com), then prepare them for browser download.

Single songs can be downloaded as audio files, and playlists or albums are packaged into a ZIP file after download. The app defaults to 320kbps when no bitrate is selected.

## Before You Start

SpotDown does not host copyrighted materials. It uses third-party sources to provide content requested by users. You are responsible for how you use the downloaded content.

Python and Flask knowledge is helpful, but it is not required to run the app.

## Setup

### Requirements

- [Python 3.10](https://www.python.org) or newer
- Dependencies from `requirements.txt`
- FFmpeg for audio conversion

If FFmpeg is not installed globally, install SpotDL's local FFmpeg binary with:

```bash
python -m spotdl --download-ffmpeg
```

### Authorization

1. Create a `.env` file in the root directory.
2. Add your Spotify API credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard):

```env
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

3. Open your browser at `http://127.0.0.1:5000`.

## Features

- Download songs, albums, and playlists from Spotify.
- Package playlist and album downloads into ZIP files.
- Default quality is 320kbps when no bitrate is selected.
- Selectable bitrates: 320, 256, 224, 160, 112, 96, 64, 48, and 40kbps.
- Metadata embedding, including cover art and artist information.
- Modern, responsive dark mode UI.

## Disclaimer

This tool is for educational purposes only. SpotDown does not host copyrighted material.
