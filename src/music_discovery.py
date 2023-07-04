```python
import random
from src.utils import get_music_data, update_user_preferences

class MusicDiscovery:
    def __init__(self, user_preferences):
        self.user_preferences = user_preferences
        self.music_data = get_music_data()

    def discover_music(self):
        genre_pref = self.user_preferences['genre']
        artist_pref = self.user_preferences['artist']

        genre_music = [song for song in self.music_data if song['genre'] == genre_pref]
        artist_music = [song for song in self.music_data if song['artist'] == artist_pref]

        recommendations = genre_music + artist_music
        random.shuffle(recommendations)

        return recommendations[:10]

    def update_preferences(self, new_preferences):
        self.user_preferences = update_user_preferences(self.user_preferences, new_preferences)

    def get_recommendations(self):
        recommendations = self.discover_music()
        return recommendations
```