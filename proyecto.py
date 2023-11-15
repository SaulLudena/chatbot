
from rivescript import RiveScript
from tkinter import *
from tkinter import ttk
class Chat:
    def __init__(self,ventana):
        self.bot = RiveScript()
        self.bot.load_file('proyecto.rive')
        self.bot.sort_replies()

        self.ventana=ventana
        self.ventana.title("ChatBot Movistar")

        marco=LabelFrame(self.ventana,text="ChatBot Movistar")
        marco.grid(row=0,column=0,columnspan=3,pady=20)

        Label(marco,text="Respuestas").grid(row=0,column=0)

        self.entRespuesta=Text(marco)
        self.entRespuesta.grid(row=0,column=1,padx=10,pady=10,ipady=60)
        self.entRespuesta.focus()

        Label(marco,text="Preguntas").grid(row=1,column=0)
        self.entPregunta=Entry(marco)
        self.entPregunta.grid(row=1,column=1,padx=10,pady=10,ipady=7,ipadx=120)
        self.entPregunta.bind('<Return>', self.preguntar)
        self.entPregunta.focus()

        btnPreguntarCrear=Button(marco,text="Preguntar",command=self.preguntar,bg="green",fg="white")
        btnPreguntarCrear.grid(row=2,columnspan=2,sticky=W+E)

    def preguntar(self,event=None):
        reply = self.bot.reply("localuser", self.entPregunta.get())
        reply = reply.replace("\\n", "\\\n")
        reply = reply.replace("\\", "")
        self.entRespuesta.insert(END,"Tu: "+self.entPregunta.get()+"\n\n")
        self.entRespuesta.insert(END,"Movistar: "+reply+"\n")
        self.entPregunta.delete(0,END)

if __name__=="__main__":
    ventana=Tk()
    Chat(ventana)
    ventana.mainloop()