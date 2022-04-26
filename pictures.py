#Authentication - without user
from tkinter.font import nametofont
from unicodedata import name
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from pprint import pp, pprint
import requests

client_credentials_manager = SpotifyClientCredentials(client_id='4ef8a3c792034658ac0ce70ffb110eba', client_secret='ad3c18b38e124063ab760a49253e92f3')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# Get artist profile pic
# if len(sys.argv) > 1:
#     urn = sys.argv[1]
# else:
#     urn = 'spotify:artist:0QYQjRbAV7qfoTpUW4Bmrh'
# artist = sp.artist(urn)
# pprint(artist['images'][0]['url'])    

# Get artists URNs

with open("artists_pfp.txt", "r") as artists:
  for artist in artists:
    # single_artist = artist.removeprefix('https://open.spotify.com/artist/').strip()
    single_artist = ("0QYQjRbAV7qfoTpUW4Bmrh")
    
    if len(sys.argv) > 1:
        urn = sys.argv[1]
    else:
        urn = single_artist

        result = sp.artist(urn)
        pprint(result)
        name = result["name"]
        image = result["images"][0]["url"]
        url = result["external_urls"]["spotify"]

        # Download the image
        response = requests.get(image)
        open(f"{name}.jpg", "wb").write(response.content)
        
        with open("output.txt", "a") as f:
            pprint(f"{name}", f)
            pprint(f"{image}", f)
            pprint(f"{url}", f)




