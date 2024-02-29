from sunau import AUDIO_FILE_MAGIC
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from tkinter import *
import time
import smtplib
import pygame
pygame.mixer.init()
root=Tk()
txt=Text(root)
txt.grid(row=0,column=0)
e=Entry(root,width=50)
e.grid(row=1,column=0)
s=""
c=""
def send():
    global s
    global c
    send="Ajay kumar: "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hi" or e.get()=="hello"):
        txt.insert(END,"\n"+"Crappy: "+"hello Good Evening")
        s=s+"\n"+e.get()+" "
        s=s+"\n"+"hello good evening"
        c=c+"\n"+"Ajay Kumar: "+e.get()+" "
        c=c+"\n"+"Crappy: "+"hello good evening"
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"Crappy: "+"I am great,what about you?")
        s=s+"\n"+e.get()+" "
        s=s+"\n"+"i am great,what about you?"
        c=c+"\n"+"Ajay kumar: "+e.get()+" "
        c=c+"\n"+"Crappy: "+"I am great,what about you?"
    elif(e.get()=="i am fine"):
        txt.insert(END,"\n"+"Crappy: "+"good to hear that!")
        s=s+"\n"+e.get()+" "
        s=s+"\n"+"good to hear that!"
        c=c+"\n"+"Ajay kumar: "+e.get()+" "
        c=c+"\n"+"Crappy: "+"good to hear that!"
    elif(e.get()=="what's your name"):
        txt.insert(END,"\n"+"Crappy: "+"my name is crappy,and yours?")
        s=s+"\n"+e.get()+" "
        s=s+"\n"+"my name is crappy,and yours?"
        c=c+"\n"+"Ajay kumar: "+e.get()+" "
        c=c+"\n"+"Crappy: "+"my name is crappy,and yours?"
    elif(e.get()=="my name is Ajay kumar"):
        txt.insert(END,"\n"+"Crappy: "+"Glad to meet you Ajay kumar!")
        s=s+"\n"+e.get()+" "
        s=s+"\n"+"Glad to meet you Ajay kumar!"
        c=c+"\n"+"Ajay kumar: "+e.get()+" "
        c=c+"\n"+"Crappy: "+"Glad to meet you Ajay kumar"
    else:
        txt.insert(END,"\n"+"Crappy: "+"i did'nt get you")
        s=s+"\n"+e.get()+" "
        s=s+"\n"+"i did'nt get you"
        c=c+"\n"+"Ajay kumar: "+e.get()+" "
        c=c+"\n"+"Crappy: "+"i did'nt get you"
    e.delete(0,END)
def convert():
    api=IAMAuthenticator("nLqDtaRUm9qskFiFtDmLnbhlhbeoIzGN-w-2GKRmcRdQ")
    text_2_speech=TextToSpeechV1(authenticator=api)
    text_2_speech.set_service_url("https://api.us-south.assistant.watson.cloud.ibm.com/instances/3aef7a1b-5e30-47e1-aa24-524f55999df8")
    with open("welcome.mp3","wb") as audiofile:
        audiofile.write(text_2_speech.synthesize(s,accept="audio/mp3").get_result().content)
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play(loops=0)
def exit():
    end=Label(root,text="The session is ended!")
    end.place(x=500,y=350)
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("Eswarnimmaluri@my.unt.edu","5808129128")
    server.sendmail("ajaykumarsathri@gmail.com","ajaykumarsathri@gmail.com",c)
    server.quit()


def start():
    start=Label(root,text="The session started")
    start.place(x=0,y=0)

buttonsub=Button(root,text="END",command=exit,bg="black",fg="light gray")
buttonsub.place(x=580,y=380)
start=Button(root,text="Start",command=start,bg="blue",fg="light gray").place(x=15,y=380)

send=Button(root,text="Send",command=send).place(x=500,y=380)
convert=Button(root,text="Voice",command=convert).place(x=80,y=380)
root.title("CHATBOT")
root.mainloop()