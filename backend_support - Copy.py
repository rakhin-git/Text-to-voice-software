#background part
import keyboard
import clipboard
import pyttsx3
import pyautogui as pya

wd=pyttsx3.init()
voices=wd.getProperty('voices')
wd.setProperty('voice', voices[1].id)
wd.setProperty('rate',135)

a=["r","R"]
while True:
    if(keyboard.read_key() in a):
        pya.hotkey('ctrl','c')
        dd=clipboard.paste()
        if(dd!=""):
            wd.say(dd)
            wd.runAndWait()
        else:
            wd.say("please select your word frist and press r key")
            wd.runAndWait()
