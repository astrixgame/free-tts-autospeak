from pygame import mixer
from time import sleep
import io, sys, requests

if len(sys.argv[1:]) > 0:
    r = requests.post("https://ttsmp3.com/makemp3_new.php", data={'msg': sys.argv[1:][0], 'lang': 'Matthew', 'source': 'ttsmp3'})
    rj = r.json()
    if rj['Error'] == 0:
        res = requests.get(rj['URL'])
        res.raise_for_status()
        mixer.init()
        mixer.music.load(io.BytesIO(res.content))
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(1)
