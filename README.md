# Web Scraper
This project was hastily created for the website smashcustommusic.com, with the purpose of quickly downloading songs from the site before it may or may not have been taken down at the time.

The site hosts user-created edits of video game soundtracks, encoded in their native "stream" filetype, which allows the audio to play on an infinite loop by using loop-points.

This script allowed me to quickly download as many songs as I could before the site was ultimately taken down at the time.

(As of 2021, the site is currently operational under the URL [smashcustommusic.net](www.smashcustommusic.net). It is unknown to me whether or not the site may stay, or for how long, given the nature of Nintendo and previous examples of their interactions with music, content creation, Copyright law, etc. Hopefully it stays :) )

# Download
There is only one file: scraper.py

download, view, edit, and run it.

# A Note on File Types
The site's native file type to download songs from is .BRSTM. While other file types are supported, the server must do a file conversion on-demand in order to meet those requests. This script is currently set to download songs in the native BRSTM format. Please do not change the script to scrape in a different format. Instead, convert any files you download natively using either [openrevolution](https://github.com/ic-scm/openrevolution) or [VGAudio](https://github.com/Thealexbarney/VGAudio).

# Legality
This is a legal use of web scraping. The function of this script is to essentially click on the download buttons offered by the site automatically and efficiently.

# What I Learned
* Basics of web scraping
* Basics of HTML web-page structures and hrefs
* Using the BeautifulSoup4 API
