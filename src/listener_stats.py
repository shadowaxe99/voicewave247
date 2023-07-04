```python
import json
from src.utils import get_current_time

listenerStats = {}

class StatsSchema:
    def __init__(self, user_id, engagement, preferences, feedback):
        self.user_id = user_id
        self.engagement = engagement
        self.preferences = preferences
        self.feedback = feedback

def updateListenerStats(user_id, engagement, preferences, feedback):
    global listenerStats
    listenerStats[user_id] = StatsSchema(user_id, engagement, preferences, feedback).__dict__

def trackListenerStats():
    global listenerStats
    while True:
        user_id, engagement, preferences, feedback = get_user_data()
        updateListenerStats(user_id, engagement, preferences, feedback)
        print(f"Updated listener stats at {get_current_time()}")

def get_user_data():
    # This function should interact with the user interface or database to get the required data
    # For the purpose of this example, we will return some dummy data
    return "user123", {"call_ins": 5, "text_messages": 10, "social_media": 15}, {"genre": "rock", "artist": "Metallica"}, {"rating": 4, "comments": "Great show!"}

def save_listener_stats():
    global listenerStats
    with open('listenerStats.json', 'w') as file:
        file.write(json.dumps(listenerStats, default=lambda o: o.__dict__, indent=4))

def load_listener_stats():
    global listenerStats
    try:
        with open('listenerStats.json', 'r') as file:
            listenerStats = json.load(file)
    except FileNotFoundError:
        listenerStats = {}
```
