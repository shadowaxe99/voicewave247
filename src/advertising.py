```python
import json
from src.utils import get_user_preferences

def displayAds(userPreferences):
    """
    Function to display dynamic and personalized ads based on user preferences and listening habits.
    """
    # Load the advertising data
    with open('data/advertising.json', 'r') as file:
        advertising_data = json.load(file)

    # Get user preferences
    preferences = get_user_preferences(userPreferences)

    # Filter ads based on user preferences
    personalized_ads = [ad for ad in advertising_data if ad['genre'] in preferences['genres']]

    # Display the personalized ads
    for ad in personalized_ads:
        print(f"Advertisement: {ad['name']}")
        print(f"Genre: {ad['genre']}")
        print(f"Description: {ad['description']}")
        print("--------------------------------------------------")

def updateAdvertisingData(new_ad_data):
    """
    Function to update the advertising data with new ads.
    """
    # Load the existing advertising data
    with open('data/advertising.json', 'r') as file:
        advertising_data = json.load(file)

    # Add the new ad data
    advertising_data.append(new_ad_data)

    # Write the updated advertising data back to the file
    with open('data/advertising.json', 'w') as file:
        json.dump(advertising_data, file)

    print("Advertising data updated successfully.")
```