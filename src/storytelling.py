```python
import json
from src.utils import get_user_input, send_message

class Storytelling:
    def __init__(self):
        self.story_data = []
        self.current_story = None

    def load_story_data(self):
        with open('data/story_data.json', 'r') as file:
            self.story_data = json.load(file)

    def start_story(self, story_id):
        for story in self.story_data:
            if story['id'] == story_id:
                self.current_story = story
                break

        if self.current_story is None:
            print("Story not found.")
            return

        print(self.current_story['start'])
        self.next_step(self.current_story['start'])

    def next_step(self, step_id):
        for step in self.current_story['steps']:
            if step['id'] == step_id:
                current_step = step
                break

        user_input = get_user_input(current_step['options'])
        next_step_id = current_step['next_steps'][user_input]
        self.next_step(next_step_id)

    def end_story(self):
        print(self.current_story['end'])
        send_message('#storytellingSegments', 'Story ended.')

def conductStorytelling():
    storytelling = Storytelling()
    storytelling.load_story_data()
    storytelling.start_story('story_1')
```