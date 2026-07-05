import json
import webbrowser
import requests
import pyttsx3, pyaudio, vosk


tts = pyttsx3.init('nsss')
voices = tts.getProperty('voices')
tts.setProperty('voices', 'en')

class Speech():
    def __init__(self):
        self.speaker = 0
        self.tts = pyttsx3.init('nsss')

    def set_voice(self, speaker):
        for count, voice in enumerate(voices):
            if speaker == count:
                id = voice.id
        return id

    def text2voice(self, speaker=0, text='ready'):
        self.tts.setProperty('voice', self.set_voice(speaker))
        self.tts.say(text)
        self.tts.runAndWait()


class Recognize:
    def __init__(self):
        model = vosk.Model('vosk-model-small-ru-0.4')
        self.record = vosk.KaldiRecognizer(model, 16000)
        self.stream()

    def stream(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(format=pyaudio.paInt16,
                              input = True,
                              channels=1,
                              rate=16000,
                              frames_per_buffer=8000)

    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.record.AcceptWaveform(data):
                answer = json.loads(self.record.Result())
                if answer.get('text'):
                    yield answer['text']

def speak(text):
    speech = Speech()
    speech.text2voice(0, text=text)


#Ввод и обработка команд
def input_word(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    res = requests.get(url)
    return res.json()

def data_pharse(data):
    try:
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', 'No example')
        return meaning, example
    except:
        return None, None

rec = Recognize()
rec.stream.start_stream()
text_gen = rec.listen()
saved_word = None
saved_data = None

for text in text_gen:
    print("You said:", text)

    if text.startswith("find"):
        word = text.split(" ")[1]
        data = input_word(word)

        if data:
            saved_word = word
            saved_data = data
            print(f"Word '{word}' found")
            speak(f"Word '{word}' found")
        else:
            print("Word not found")
            speak("Word not found")

    elif text == "meaning" and saved_data:
        meaning, _ = data_pharse(saved_data)
        print("Meaning:", meaning)
        speak(meaning)

    elif text == "example" and saved_data:
        _, example = data_pharse(saved_data)
        print("Example:", example)
        speak(example)

    elif text == "link" and saved_word:
        webbrowser.open(f"https://api.dictionaryapi.dev/api/v2/entries/en/{saved_word}")

    elif text == "save" and saved_word:
        with open("words.txt", "a") as f:
            f.write(saved_word + "\n")
        print("Saved!")
        speak("Saved!")

    elif text == 'close':
        quit()