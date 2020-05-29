# ytdl
A free and simple YouTube video downloader for Mac and Linux.

### Mac Instructions
#### Install the following:
Skip this step if xcode commandline tools is already installed on your system.
Xcode commandline tools with `xcode-select --install`

python3 (https://www.python.org/downloads/)

#### Clone the repository:
`git clone https://github.com/EthanLeitch/ytdl.git`

#### Install Brew with modified install
Skip this step if Brew is already installed on your system.
(For some stupid reason, Brew's xcode detection is faulty and it won't let you install Brew if you try and do it normally.
It would claim that the xcode command line tools weren't installed when they actually were.)

`chmod +x moddedinstall.sh`
`./moddedinstall.sh`

#### Install ffmpeg
`brew install ffmpeg`

#### Install youtube-dl
`brew install youtube-dl`

#### Move "youtube-dl.conf" to /etc/
`sudo mv youtube-dl.conf /etc/`

#### Move "youtube-downloader.py" to /Users/Name
`sudo mv youtube-downloader.py /Users/Name`

You're done! Just launch the bash script and you should be good to go!
