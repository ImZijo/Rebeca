from tkinter import*
import AI
fen = Tk()
UserMvalue = StringVar()
UserMinput = Entry(fen,textvariable=UserMvalue,width=30)
Chat = Text(fen,height=20,width=30)
Chat.pack()
WhoUser = Listbox(fen)
WhoUser.insert(1,"Le Créateur")
WhoUser.insert(2,"Le Gars Random")
WhoUser.insert(3,"La Meilleure Pote")
WhoUser.insert(4,"Le Petit Copain")
WhoUser.insert(5,"L'ami")
WhoUser.pack(side=RIGHT)
def UWget():
    global WhoUser,UW
    UW = WhoUser.curselection()[0]
WU = Button(text="Valider Utilisateur", command=UWget)
WU.pack(side=BOTTOM)
Chan = Listbox(fen)
Chan.insert(1,"Apprentissage")
Chan.insert(2,"Pratique")
Chan.insert(3,"Déconne")
Chan.pack(side=RIGHT)
def CHget():
    global Chan,CH
    CH = Chan.curselection()[0]
HC = Button(text="Valider Salon", command=CHget)
HC.pack(side=BOTTOM)
ListChan = ("Normal","Normal","Fun")
def Enter(event):
    global UserMinput,WhoUser,Chan,ListChan,Ch,CH,UW
    USER = UW
    CHANNEL = CH
    Learning = (CHANNEL != 2)
    FileM = ListChan[CHANNEL] + "/memory.txt"
    FileP = ListChan[CHANNEL] + "/profiles.txt"
    INP = UserMinput.get()
    Chat.insert(END, "Moi: "+INP+"\n")
    Chat.insert(END, "Rebecca: "+AI.ans(INP,USER,Learning,FileM,FileP)+"\n")
UserMinput.bind("<Return>",Enter)
UserMinput.pack()
fen.mainloop()
