```python
import json
from src.utils import get_user_data, update_user_data

def hostVirtualMeetAndGreets():
    user_data = get_user_data()
    meet_and_greet_data = user_data.get('virtualMeetAndGreets', [])

    print("Welcome to the Virtual Meet and Greets!")
    print("Here are the upcoming meet and greets:")

    for event in meet_and_greet_data:
        print(f" - {event['celebrity']} on {event['date']} at {event['time']}")

    print("Would you like to join any of these sessions?")
    user_choice = input("Enter the name of the celebrity: ")

    for event in meet_and_greet_data:
        if event['celebrity'].lower() == user_choice.lower():
            print(f"You have successfully joined the meet and greet with {event['celebrity']}!")
            event['participants'].append(user_data['username'])
            update_user_data(user_data)
            break
    else:
        print("Sorry, we couldn't find a meet and greet with that celebrity.")

if __name__ == "__main__":
    hostVirtualMeetAndGreets()
```