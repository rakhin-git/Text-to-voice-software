#GUI part
import pyttsx3
from tkinter import*
import subprocess
import clipboard

clipboard.copy("")
wd=pyttsx3.init()
voices=wd.getProperty('voices')
wd.setProperty('voice', voices[1].id)
wd.setProperty('rate',135)

wd.say("please select your words and press the r key on your keyboard, I will speak automatically.")
wd.runAndWait()

subprocess.call(['cscript.exe','start.vbs'])

    
def rules():
    wd.say("Just select your words and press the r key on your keyboard, I will speak automatically. to listen to the words again, press the r key again on your keyboard.")
    wd.runAndWait()
    
def close():
    subprocess.call("TASKKILL /F /IM rakhin_text_voice.exe", shell=True)
    rakhin.destroy()

rakhin=Tk()
rakhin.title("Eng.Rakhin.babu")
rakhin.minsize(260,60)
rakhin.maxsize(260,60)
rakhin.iconbitmap("rakhinbabu.ico")

lb=Label(rakhin,text="*New, Text to voice offline.",font=("times new roman",13),fg="#D35400")
lb.pack()
btn=Button(rakhin,text="Rules, press(R)",font=("times new roman",13),fg="black",bd=1,command=rules)
btn.pack()
label=Label(rakhin)

rakhin.protocol("WM_DELETE_WINDOW",close)
rakhin.mainloop()
