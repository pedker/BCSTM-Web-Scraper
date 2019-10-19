import urllib.request
import requests
from bs4 import BeautifulSoup

exclusion = ['Random', 'Games', 'Donate', 'Contact', 'Tweet', 'Buy this Game', 'Buy the official music album']
reservedChars = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>']

baseDownloadURL = "http://smashcustommusic.com/bcstm"
downloadLocation = str(input("Download Location: "))
gameURL = "http://smashcustommusic.com/game/" + str(input('Game Code: '))

response = requests.get(gameURL)
soup = BeautifulSoup(response.text, 'html.parser')
entries = soup.findAll('a')

for entry in entries:
    if entry.get_text() not in exclusion:
        href = entry['href']
        fileName = entry.get_text() + '.bcstm'
        for char in reservedChars:
            fileName = fileName.replace(char, '_')
        
        print(f'Downloading {fileName} ...')
        page = urllib.request.urlretrieve(baseDownloadURL+href, downloadLocation+'/'+fileName)

