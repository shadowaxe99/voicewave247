```python
import json
from src.utils import get_genre_data

# Global variable for storing genre channels data
genre_channels = {}

def curateGenreChannels(userPreferences):
    """
    Function to curate genre-specific channels based on user preferences
    """
    global genre_channels
    genre_channels = get_genre_data(userPreferences)

def getGenreChannels():
    """
    Function to return the curated genre channels
    """
    global genre_channels
    return genre_channels

def updateGenreChannels(newPreferences):
    """
    Function to update the genre channels based on new user preferences
    """
    curateGenreChannels(newPreferences)

def displayGenreChannels():
    """
    Function to display the curated genre channels
    """
    global genre_channels
    print(json.dumps(genre_channels, indent=4))

if __name__ == "__main__":
    userPreferences = {"genres": ["pop", "rock", "jazz", "classical"]}
    curateGenreChannels(userPreferences)
    displayGenreChannels()
```