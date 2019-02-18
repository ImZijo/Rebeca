from datetime import date
from random import randint
StrList = [0]
AddIntList = [1,3]
RepIntList = [4,5]
BaseP = ["",0,None,0,None,"0"]
BaseMeaning = ["name","friendly","attirance","love","age","lastday"]
data = BaseP
def FifthSplit(Spl5,MESSAGE):
    B = False
    for i in Spl5:
        for j in i.split("£"):
            if j in MESSAGE:
                B = True
    return B
def add_joke(file,message):
    M = message.lower().split("j'ai une blague:")[1]
    File = open(file)
    F = File.read()
    File.close()
    M += "\n£§£\n" + F
    File = open(file,"w")
    File.write(M)
    File.close()
def get_joke(file):
    File = open(file)
    F = File.read().split("\n£§£\n")
    File.close()
    return F[randint(0,len(F)-1)]
def add_adj(adj,nb,Folder):
    if adj[0] == '"':
        A = adj[1:]
        A = A[:len(A)-1]
    else:
        A = adj
    File = open(Folder+"/adjectives.txt")
    ADJs = File.read()
    File.close()
    adjectives = list(ADJs.split("\n---\n"))
    adjectives[nb] += "\n" + A
    File = open(Folder+"/adjectives.txt","w")
    File.write(adjectives[0]+"\n---\n"+adjectives[1]+"\n---\n"+adjectives[2])
    File.close()
def EifGIRL(nb):
    if ToInt(nb) == -1:
        return "e"
    else:
        return ""
def DataPut(LIST,Lim=50,Cr=False):
    global data
    if Cr and len(LIST) > 2:
        STR = LIST[2]
    elif int(data[1]) >= Lim and len(LIST) > 1 and LIST[1] != "":
        STR = LIST[1]
    else:
        STR = LIST[0]
    STR = STR.replace("[name]",data[0].upper()).replace("[e]",EifGIRL(data[2])).replace("[age]",str(data[4]))
    return STR 
def OneIn(LIST,STR):
    ok = True
    for q in LIST:
        if not q in STR:
            ok = False
    return ok
ListNbStr = ["zéro","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dis-sept","dix-huit","dix-neuf","vingt","vingt-et-un","vingt-deux","vingt-trois","vingt-quatre","vingt-cinq"]
def ToInt(STR):
    global ListNbStr
    try:
        var = int(STR)
        return var
    except:
        if STR in ListNbStr:
            var = ListNbStr.index(STR)
        else:
            var = 0
        return var
def save_command(com):
    Rebeca.say("Work in progress")
def view_profile(ID):
    global BaseMeaning
    if ID[0] == "!":
        Id = ID[1:]
    else:
        Id = ID
    File = open("Normal/profiles.txt")
    Datas = File.read()
    File.close()
    ProfileData = None
    for P in Datas.split("\n"):
        if P.split("¤")[0] == Id:
            ProfileData = P
    if ProfileData == None:
        return "Ce profil n'a pas été enregistré"
    else:
        S = ""
        D = ProfileData.split("¤")
        for j in range(6):
            S += BaseMeaning[j] + " : " + D[j+1]+"\n"
        return S
#If each : heard¤said¤var1¤var2...
def search(LIST,MESSAGE):
    global data,AddIntList,StrList,RepIntList,adjectives,known
    ANS = None
    for i in LIST:
        MesCode = i.split("¤")
        F = MesCode[0]
        for S in F.split("|£|"):
            Split2 = S.split(" [££] ")
            Split3 = S.split(" [£££] ")
            Split4 = S.split(" [[£]] ")
            Saved = 2
            if len(Split2) > 1:
                if OneIn(Split2,MESSAGE):
                    N = MESSAGE.split(" ")
                    U = list(S.split(" "))
                    nb = 0
                    V = False
                    Er = True
                    for j in range(len(N)):
                        if N[j] in U:
                            nb += 1
                            if V:
                                Saved += 1
                                V = False
                        elif U[nb] == "[££]":
                            if int(MesCode[Saved]) in StrList:
                                if Er:
                                    Er = False
                                    data[int(MesCode[Saved])] = ""
                                if data != "":
                                    data += " "
                                data[int(MesCode[Saved])]+= N[j]
                                V = True
                            if int(MesCode[Saved]) in RepIntList:
                                try:
                                    data[int(MesCode[Saved])]= ToInt(N[j])
                                except:
                                    return "Je n'ai pas compris le nombre!"
                    ANS = MesCode[1]
            elif len(Split3) > 1:
                if OneIn(Split3,MESSAGE):
                    ANS = "Peut-être...\nMon IA ne me permet pas de le savoir"
                    N = MESSAGE.split(" ")
                    U = list(S.split(" "))
                    nb = 0
                    V = ""
                    for j in range(len(N)):
                        if N[j] in U:
                            nb += 1
                        elif U[nb] == "[£££]":
                            if V != "":
                                V += " "
                            V += N[j]
                            if V in adjectives[0].split("\n"):
                                data[1] = int(data[1])+(int(MesCode[2])*2)
                                if data[2] != None:
                                    if int(data[2]) == -1:
                                        print("+pote avec les filles")
                                        data[1] = int(data[1])+int(MesCode[2])
                                    else:
                                        data[3] = int(data[3])+int(MesCode[3])
                                return "Beau compliment!"
                            elif V in adjectives[1].split("\n"):
                                data[1] = int(data[1])-(int(MesCode[2])*2)
                                if data[2] != None:
                                    if int(data[2]) == -1:
                                        data[1] = int(data[1])+int(MesCode[2])
                                    else:
                                        data[3] = int(data[3])-int(MesCode[3])
                                return "Ce n'est pas très gentil"
                            else:
                                if V in adjectives[2].split("\n"):
                                    ANS = MesCode[1]
                                else:
                                    ANS = '/¤/Euh... "' + V +'" est mélioratif ou péjoratif?"'
            else:
                Split5 = S.split(" [£gender£] ")
                if len(Split4) > 1:
                    if OneIn(Split4,MESSAGE):
                        data[1] = str(int(data[1])+2)
                        ANS = ["Non, je ne connais pas",None]
                        N = MESSAGE.split(" ")
                        U = list(S.split(" "))
                        nb = 0
                        V = ""
                        for j in range(len(N)):
                            if N[j] in U:
                                nb += 1
                            elif U[nb] == "[[£]]":
                                if V != "":
                                    V += " "
                                V += N[j]
                        if V[len(V)-1] == "?":
                            V = V[:len(V)-1]
                        ANS[1] = V
                        for k in known:
                            K = k.split("¤")
                            if V == K[0]:
                                ANS = MesCode[1] + K[1]
                elif len(Split5) > 1:
                    if FifthSplit(Split5,MESSAGE):
                        ANS = "Je n'ai pas compris ton genre"
                        if data[2] in ("None",None):
                            for w in Split5[0].split("£"):
                                if w in MESSAGE:
                                    data[2] = -1
                                    ANS = "J'ai enregistré que tu étais une femme"
                            for m in Split5[1].split("£"):
                                if m in MESSAGE:
                                    data[2] = randint(0,100)
                                    ANS = "J'ai enregistré que tu étais un homme"
                        else:
                            ANS = "Tu m'a déjà dit ton genre, c'est une information que je ne peux modifier"
                else:
                    if S in MESSAGE and ANS==None:
                        data[1] = int(data[1])+1
                        if int(data[2]) == -1:
                            data[1] = int(data[1])+1
                        ANS = MesCode[1]
                        if len(MesCode) > 3:
                            if int(MesCode[2]) in AddIntList:
                                data[int(MesCode[2])] += int(MesCode[3])
                            elif int(MesCode[2]) in RepIntList:
                                data[int(MesCode[2])] = int(MesCode[3])
                            else:
                                if int(MesCode[2]) in StrList:
                                    data[int(MesCode[2])] = MesCode[3]
                        if len(MesCode) > 5:
                            if int(MesCode[4]) in AddIntList:
                                data[int(MesCode[4])] += int(MesCode[5])
                            elif int(MesCode[2]) in RepIntList:
                                data[int(MesCode[4])] = int(MesCode[5])
                            else:
                                if int(MesCode[4]) in StrList:
                                    data[int(MesCode[4])] = MesCode[5]
                        if len(MesCode) > 7:
                            if int(MesCode[6]) in AddIntList:
                                data[int(MesCode[6])] += int(MesCode[7])
                            elif int(MesCode[6]) in RepIntList:
                                data[int(MesCode[6])] = int(MesCode[7])
                            else:
                                if int(MesCode[2]) in StrList:
                                    data[int(MesCode[6])] = MesCode[7]
    return ANS
def ans(message,ID,learn_bool,memory,profiles,adj,knowledge,limit):
    global BaseP,data,adjectives,known
    mes = message.replace("¤","")
    mes = mes.replace("£","")
    mes = mes.lower()
    mes = mes.replace("\n"," ")
    identity = str(ID)
    FileData = open(profiles)
    Pstr = FileData.read()
    FileData.close()
    FileData = open(knowledge)
    Kstr = FileData.read()
    FileData.close()
    known = Kstr.split("\n")
    FileData = open(adj)
    ADJstr = FileData.read()
    FileData.close()
    adjectives = ADJstr.split("\n---\n")
    DataSTR = None
    for s in Pstr.split("\n"):
        if s[:len(identity)] == identity:
            DataSTR = s
    if DataSTR == None :
        data = BaseP
    else:
        data = list(DataSTR.split("¤"))
        data.remove(identity)
        while len(data) < len(BaseP):
            data.append(BaseP[len(data)])
    FileAns = open(memory)
    Astr = FileAns.read()
    FileAns.close()
    STR = search(Astr.split("\n"),mes)
    print(str(data))
    if type(STR) == str and STR.startswith("Bonjour"):
        today = date.today()
        if data[5] == today.isoformat():
            STR = "Tu m'a déjà dit Bonjour!"
        else:
            data[1] = int(data[1]) + 1
            data[5] = today.isoformat()
    Wstr = ""
    for s in Pstr.split("\n"):
        if s[:len(identity)] != identity:
            Wstr += s+"\n"
    Wstr += identity + "¤"
    for g in data:
        Wstr += str(g)+"¤"
    Wstr = Wstr[:len(Wstr)-1]
    FileData = open(profiles,"w")
    FileData.write(Wstr)
    FileData.close()
    if STR ==None:
        return "|£|"
    else:
        if type(STR) == list:
            return STR
        else:
            Lstr = STR.split("£")#("amitié<50","amitié > 50")
            return DataPut(Lstr,limit)
