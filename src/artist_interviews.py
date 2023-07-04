```python
import json
from src.utils import get_data_from_API

artistData = {}

def updateArtistData():
    global artistData
    artistData = get_data_from_API("https://api.voicewave247.com/artists")

def interviewArtists(artist_id):
    artist = artistData.get(artist_id)
    if not artist:
        print(f"No artist found with id {artist_id}")
        return

    print(f"Interview with {artist['name']}")
    print(f"Bio: {artist['bio']}")
    print(f"Behind the scenes: {artist['behind_the_scenes']}")

def get_artist_interviews():
    updateArtistData()
    for artist_id in artistData:
        interviewArtists(artist_id)

if __name__ == "__main__":
    get_artist_interviews()
```