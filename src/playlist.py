```python
from src.utils import UserSchema, PlaylistSchema
from src.config import playlistData

class Playlist:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_data = UserSchema.validate(user_id)
        self.playlist_data = PlaylistSchema.validate(playlistData)

    def create_playlist(self, playlist_name, song_list):
        new_playlist = {
            "playlist_name": playlist_name,
            "song_list": song_list,
            "created_by": self.user_id
        }
        self.playlist_data.append(new_playlist)
        return new_playlist

    def share_playlist(self, playlist_name, friend_id):
        for playlist in self.playlist_data:
            if playlist["playlist_name"] == playlist_name and playlist["created_by"] == self.user_id:
                playlist["shared_with"].append(friend_id)
                return True
        return False

    def add_song_to_playlist(self, playlist_name, song_id):
        for playlist in self.playlist_data:
            if playlist["playlist_name"] == playlist_name and playlist["created_by"] == self.user_id:
                playlist["song_list"].append(song_id)
                return True
        return False

    def remove_song_from_playlist(self, playlist_name, song_id):
        for playlist in self.playlist_data:
            if playlist["playlist_name"] == playlist_name and playlist["created_by"] == self.user_id:
                if song_id in playlist["song_list"]:
                    playlist["song_list"].remove(song_id)
                    return True
        return False
```