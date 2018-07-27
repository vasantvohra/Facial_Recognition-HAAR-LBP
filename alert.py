from pygame import mixer
import time
def alert():
    mixer.init()
    alert = mixer.Sound('beep-07.wav')
    alert.play()
    time.sleep(0.1)
    alert.play()
alert()
