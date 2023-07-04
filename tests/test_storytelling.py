```python
import unittest
from src import storytelling

class TestStorytelling(unittest.TestCase):

    def setUp(self):
        self.storytelling = storytelling.conductStorytelling()

    def test_story_creation(self):
        story = self.storytelling.create_story("Test Story", "This is a test story.")
        self.assertEqual(story.title, "Test Story")
        self.assertEqual(story.content, "This is a test story.")

    def test_story_interaction(self):
        story = self.storytelling.create_story("Test Story", "This is a test story.")
        interaction = self.storytelling.interact_with_story(story, "This is a test interaction.")
        self.assertEqual(interaction.story, story)
        self.assertEqual(interaction.content, "This is a test interaction.")

    def test_story_update(self):
        story = self.storytelling.create_story("Test Story", "This is a test story.")
        updated_story = self.storytelling.update_story(story, "Updated Test Story", "This is an updated test story.")
        self.assertEqual(updated_story.title, "Updated Test Story")
        self.assertEqual(updated_story.content, "This is an updated test story.")

    def test_story_deletion(self):
        story = self.storytelling.create_story("Test Story", "This is a test story.")
        self.storytelling.delete_story(story)
        self.assertNotIn(story, self.storytelling.stories)

if __name__ == '__main__':
    unittest.main()
```