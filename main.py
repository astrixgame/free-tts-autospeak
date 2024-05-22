import requests
from pygame import mixer
from time import sleep
import io

def tts(text):
    response = requests.post("https://ttsmp3.com/makemp3_new.php", data={'msg': text, 'lang': 'Matthew', 'source': 'ttsmp3'})
    response_json = response.json()
    if response_json['Error'] == 0:
        response = requests.get(response_json['URL'])
        response.raise_for_status()
        mixer.init()
        mixer.music.load(io.BytesIO(response.content))
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(1)

tts("The answer to the universe is 42")