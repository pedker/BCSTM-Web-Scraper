import time
import urllib
import requests
import pathlib
from bs4 import BeautifulSoup

EXCLUSION = ['Random', 'Games', 'Switch Theme', 'Log In', 'About', 'Donate', 'Contact', 'Tools', 'Tweet', 'Buy this Game', 'Buy the official music album', 'Preferences', '']
RESERVED_CHARS = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '\t']
DOWNLOAD_BUFFER = 15
BASE_DOWNLOAD_URL = "https://smashcustommusic.net/brstm/"



def recursiveScrape(index: int):
    if index >= len(entries):
        return;
    if  entries[index].get_text() in EXCLUSION:
        recursiveScrape(index + 1)
    else:
        href = entries[index]['href'][6:];
        fileName = entries[index].get_text() + '.brstm';
        for char in RESERVED_CHARS:
            fileName = fileName.replace(char, '_');

        print(f'Downloading {fileName} using {BASE_DOWNLOAD_URL+href}... ', end='');
        try:
            page = urllib.request.urlretrieve(BASE_DOWNLOAD_URL+href, downloadLocation+'/'+fileName);
            print("Done. Continuing in ", DOWNLOAD_BUFFER, " seconds...");
            time.sleep(DOWNLOAD_BUFFER);
            recursiveScrape(index + 1);
        except urllib.error.HTTPError as e:
            print("An error occured {", str(e), "}. Retrying in ", DOWNLOAD_BUFFER, " seconds...");
            time.sleep(DOWNLOAD_BUFFER);
            recursiveScrape(index);

            


if __name__ == '__main__':
    downloadLocation = pathlib.Path(str(input("Download Location: ")))
    while not downloadLocation.is_dir():
        downloadLocation = pathlib.Path(str(input("That didn't work. Try again: \n")))
    downloadLocation = str(downloadLocation)
    gameURL = "https://smashcustommusic.net/game/" + str(input('Game Code: '))
    response = requests.get(gameURL)
    soup = BeautifulSoup(response.text, 'html.parser')
    entries = soup.findAll('a')
    recursiveScrape(0)
    x = input("\nCompleted successfully. Press ENTER.");


# OLD

#try:
#    for entry in entries:
#        if entry.get_text() not in EXCLUSION:
#            href = entry['href'][6:]
#            fileName = entry.get_text() + '.bcstm'
#            for char in RESERVED_CHARS:
#                fileName = fileName.replace(char, '_')
            
#            print(f'Downloading {fileName}...')
#            page = urllib.request.urlretrieve(BASE_DOWNLOAD_URL+href, downloadLocation+'/'+fileName)
#            time.sleep(DOWNLOAD_BUFFER)
#    x = input("\nCompleted successfully. Press ENTER.");
#except urllib.error.HTTPError as e:
#    print("An error occured {", str(e), "}. Retrying in ", 90, " seconds...")
#    time.sleep(90)
#    page = urllib.request.urlretrieve(BASE_DOWNLOAD_URL+href, downloadLocation+'/'+fileName)
