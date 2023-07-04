```python
import json
from src.utils import send_message

liveEvents = []

def hostVirtualConcerts():
    global liveEvents
    # Load the live events data
    with open('data/liveEvents.json', 'r') as f:
        liveEvents = json.load(f)

    # Filter out the concerts and performances
    concerts = [event for event in liveEvents if event['type'] == 'concert' or event['type'] == 'performance']

    # Host the virtual concerts
    for concert in concerts:
        # Send a message to the user about the concert
        send_message(f"Hosting virtual concert: {concert['name']} by {concert['artist']}")
        # Update the live events data
        concert['status'] = 'live'
        updateLiveEvents()

def updateLiveEvents():
    global liveEvents
    # Save the updated live events data
    with open('data/liveEvents.json', 'w') as f:
        json.dump(liveEvents, f)

    # Send a message to update the live events data in other modules
    send_message('updateLiveEvents', liveEvents)
```