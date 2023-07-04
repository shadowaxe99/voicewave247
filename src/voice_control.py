```python
import speech_recognition as sr

class VoiceControl:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                return command
            except sr.UnknownValueError:
                print("Sorry, I did not get that.")
                return self.listen_command()

    def controlVoiceWave(self, command):
        if 'play' in command:
            # Call function to play music
            pass
        elif 'pause' in command:
            # Call function to pause music
            pass
        elif 'next' in command:
            # Call function to play next song
            pass
        elif 'previous' in command:
            # Call function to play previous song
            pass
        elif 'volume up' in command:
            # Call function to increase volume
            pass
        elif 'volume down' in command:
            # Call function to decrease volume
            pass
        else:
            print("Sorry, I did not get that.")
            return self.listen_command()

if __name__ == "__main__":
    voice_control = VoiceControl()
    while True:
        command = voice_control.listen_command()
        voice_control.controlVoiceWave(command)
```