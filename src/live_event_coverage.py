```python
import requests
from src.config import API_URL
from src.utils import update_live_events

def coverLiveEvents():
    response = requests.get(f"{API_URL}/live_events")
    if response.status_code == 200:
        liveEvents = response.json()
        update_live_events(liveEvents)
        return liveEvents
    else:
        return None

def getEventDetails(event_id):
    response = requests.get(f"{API_URL}/live_events/{event_id}")
    if response.status_code == 200:
        eventDetails = response.json()
        return eventDetails
    else:
        return None

def updateLiveEvents():
    liveEvents = coverLiveEvents()
    if liveEvents:
        for event in liveEvents:
            eventDetails = getEventDetails(event['id'])
            if eventDetails:
                event.update(eventDetails)
    return liveEvents
```