```python
import json
from src.utils import send_message, receive_message

userPreferences = {}
interactionPanel = "#interactionPanel"

def engageWithListeners():
    while True:
        message = receive_message(interactionPanel)
        if message['type'] == 'call-in':
            handle_call_in(message)
        elif message['type'] == 'text':
            handle_text_message(message)
        elif message['type'] == 'social-media':
            handle_social_media_message(message)

def handle_call_in(call_in):
    # Process call-in interaction
    userPreferences[call_in['user_id']] = call_in['preferences']
    send_message('updateUserPreferences', userPreferences)

def handle_text_message(text_message):
    # Process text message interaction
    userPreferences[text_message['user_id']] = text_message['preferences']
    send_message('updateUserPreferences', userPreferences)

def handle_social_media_message(social_media_message):
    # Process social media interaction
    userPreferences[social_media_message['user_id']] = social_media_message['preferences']
    send_message('updateUserPreferences', userPreferences)

if __name__ == "__main__":
    engageWithListeners()
```