import io, sys, requests, time, pygame

if len(sys.argv[1:]) > 0:
    r = requests.post("https://ttsmp3.com/makemp3_new.php", data={'msg': sys.argv[1:][0], 'lang': 'Matthew', 'source': 'ttsmp3'})
    rj = r.json()
    if rj['Error'] == 0:
        res = requests.get(rj['URL'])
        res.raise_for_status()
        pygame.mixer.init()
        pygame.mixer.music.load(io.BytesIO(res.content))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
