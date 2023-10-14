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
- [Python 3.9](https://www.python.org) or newer
- [requirements.txt](https://github.com/Martin1080/SpotDown/blob/main/requirements.txt)

### Setup
Download the repository zip file and extract it.

Edit the runme.txt and change 2nd line:

- `"path\to\python.exe" "path\to\app.py(this folder)"`

So the file looks for example like this:

- `@echo off
"C:\Users\Mike\AppData\Local\Programs\Python\Python39\python.exe" "C:\Mike\Documents\SpotDown\app.py"
pause`

After you replace the paths save the file as `runme.bat`

#### Congratulations, setup is done. Now you can run the `rumne.bat` file to test it! It will give you link eg. `http://127.0.0.1:8000/`, just copy it and paste it to your web browser.
