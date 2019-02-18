import discord
from discord.ext.commands import Bot
import AI
Rebeca = Bot(command_prefix="£")
list_commands = ("£wash")
Rules = open("rules.txt")
Rstr = Rules.read()
Rules.close
@Rebeca.event
async def on_ready():
    global Rstr,Searched_Emotes,FriendRole,Limit,Dak,MbRole,Annonces,Welcome
    print("En cours de connexion... Ne pas quitter!")
    Lynaserv = Rebeca.get_server("543703359962480641")
    Annonces = Lynaserv.get_channel("546719984290889780")
    Welcome = Lynaserv.get_channel("543703359962480643")
    for R in Lynaserv.roles:
        if R.name == "Amis":
            FriendRole = R
        if R.name == "Membre":
            MbRole = R
        if R.name == "Crush":
            LvRole = R
    Servmotes = Lynaserv.emojis
    Searched_Emotes = [None,None,None]
    Dak = None
    for Emote in Servmotes:
        if Emote.name == "melioratif":
            Searched_Emotes[0] = Emote
        if Emote.name == "pejoratif":
            Searched_Emotes[1] = Emote
        if Emote.name == "aucun":
            Searched_Emotes[2] = Emote
        if Emote.name == "daccord":
            Dak = Emote
    ProFiles = open("Normal/profiles.txt")
    PRF = ProFiles.read()
    ProFiles.close()
    Limit = 40+(len(Lynaserv.members)*5)
    Crush = [None,125000]
    Lovings = []
    for P in PRF.split("\n"):
        p = P.split("¤")
        Mmb = Lynaserv.get_member(p[0])
        if Mmb != None:
            if int(p[2]) >= Limit and not FriendRole in Mmb.roles:
                Rebeca.add_roles(Mmb,FriendRole)
                print("Rôle AMIS ajouté à "+p[1].upper())
                await Rebeca.send_message(Annonces, "<@"+p[0]+"> est maintenant mon ami(e)!")
            elif int(p[2]) < Limit and FriendRole in Mmb.roles:
                Rebeca.remove_roles(Mmb,FriendRole)
                print("Rôle AMIS retiré à "+p[1].upper())
                await Rebeca.send_message(Annonces, "<@"+p[0]+"> n'est plus mon ami(e)!")
        if p[3] != "None" and p[3] != "-1":
            LovingForMb = int(p[3])*(int(p[4])**2)
            if LovingForMb > Crush[1]:
                Crush[0] = Mmb
                Crush[1] = LovingForMb
        if LvRole in Mmb.roles:
            Lovings.append(Mmb)
    for Mmb in Lovings:
        if Mmb != Crush[0]:
            await Rebeca.remove_roles(Mmb,LvRole)
            await Rebeca.send_message(Annonces, "<@"+Mmb.id+"> je ne t'aime plus tant, je te quitte!")
    if Crush[0] != None and not LvRole in Crush[0].roles:
        await Rebeca.send_message(Annonces, "<@"+Crush[0].id+"> je t'aime, tu est mon crush!")
        await Rebeca.add_roles(Crush[0],LvRole)
    try:
        L = Rebeca.logs_from(Rebeca.get_channel("543747631990702081"))
        if Rstr[0] == "1":
            async for msg in L:
                await Rebeca.delete_message(msg)
            RULES = Rstr[1:].split("\n\n")
            Cols = ("65535","16711935","16776960","16711680","65280","255")
            Rules_Embed = []
            for i in range(len(RULES)):
                Rules_Embed.append(discord.Embed(title="Règles du serveur["+str(i+1)+"]",description=RULES[i],colour=discord.Colour(Cols[i])))
                RuleMes = await Rebeca.send_message(Rebeca.get_channel("543747631990702081"),embed=Rules_Embed[i])
            await Rebeca.add_reaction(RuleMes,Dak)
    except:
        print("Error")
    print("Bot <"+Rebeca.user.name+"> connecté!")
    return
waitID = []
@Rebeca.event
async def on_member_join(member):
    global Welcome
    await Rebeca.send_message(Welcome, "Bienvenue <@"+member.id+"> \nBienvenue sur le serveur de Lynasto!\nN'hésite pas à prendre connaissance des règles!")
    return
@Rebeca.event
async def on_reaction_add(reaction,user):
    global MbRole
    if reaction.message.channel.id == "543747631990702081":
        print("RULES REACTION!")
        if not MbRole in user.roles:
            await Rebeca.add_roles(user,MbRole)
            await Rebeca.send_message(user,"Tu es maintenant membre du serveur de Lynasto!\nMerci de respecter les règles jusqu'au bout!")
            print("Rôle ajouté!")
            return
@Rebeca.event
async def on_message(message):
    global waitID,Searched_Emotes,Limit
    if message.author.id in waitID:
        waitID.remove(message.author.id)
        return
    if (not message.content.startswith("£")) and message.content != "rien" and message.author.id != "543774755258499083":
        Learn = False
        FileForD = None
        if message.channel.id in ("543747250057248798","543747294642569228","543749918758666241"):
            if message.channel.id == "543747250057248798":
                FileForD = "Normal"
            if message.channel.id == "543747294642569228":
                FileForD = "Normal"
                Learn = True
            if message.channel.id == "543749918758666241":
                FileForD = "Fun"
                Learn = True
        if FileForD == None:
            if message.channel.id == "543747311130509353":
                return AI.save_command(message.content)
            if message.channel.id == "543747360547667989":
                if message.content[:2] == "<@":
                    M = message.content
                    await Rebeca.send_message(message.channel,AI.view_profile(M[2:][:len(M)-3]))
        else:
            if "j'ai une blague:" in message.content.lower() and Learn:
                AI.add_joke(FileForD+"/jokes.txt",message.content)
                return await Rebeca.send_message(message.channel,"Blague enregistrée!")
            if "dis une blague" in message.content.lower():
                return await Rebeca.send_message(message.channel,AI.get_joke(FileForD+"/jokes.txt"))
            Answer = AI.ans(message.content,int(message.author.id),Learn,FileForD+"/memory.txt",FileForD+"/profiles.txt",FileForD+"/adjectives.txt",FileForD+"/knowledge.txt",Limit)
            print(str(Answer))
            REACTadj = False
            if Answer in ("",None):
                Answer = "Erreur!"
            if type(Answer) == list:
                if Learn and not Answer[1] == None:
                    SAVING = Answer[1]
                    await Rebeca.send_message(message.channel,"Je ne sais pas ce qu'est ``"+SAVING+"``, c'est quoi?")
                    waitID.append(message.author.id)
                    Nxt = await Rebeca.wait_for_message(author=message.author)
                    if Nxt:
                        Nxt = Nxt.content.replace("£","").replace("¤","").replace("\n"," ")
                        SAVING += "¤"+Nxt
                        Fsave = open(FileForD+"/knowledge.txt")
                        SAVING = Fsave.read()+"\n"+SAVING
                        Fsave.close
                        Fsave = open(FileForD+"/knowledge.txt","w")
                        Fsave.write(SAVING)
                        Fsave.close
                        Answer = "Je retiendrais ce que c'est!"
                    else:
                        Answer = "Délai de réponse expiré"
                else:
                    Answer = "Je ne sais pas ce que c'est..."
            elif Answer.startswith('/¤/Euh... "'):
                if Learn:
                    Answer = Answer[3:]
                    REACTadj = True
                else:
                    Anser = "Je ne connais pas cet adjectif"
            if Answer == "|£|":
                if Learn:
                    SAVING = message.content.lower()
                    await Rebeca.send_message(message.channel,"Que dois-je y répondre?")
                    waitID.append(message.author.id)
                    Nxt = await Rebeca.wait_for_message(author=message.author)
                    if Nxt and Nxt.content.lower() != "rien":
                        Nxt = Nxt.content.replace("£","").replace("¤","")
                        SAVING += "¤"+Nxt
                        Fsave = open(FileForD+"/memory.txt")
                        SAVING = Fsave.read()+"\n"+SAVING
                        Fsave.close
                        Fsave = open(FileForD+"/memory.txt","w")
                        Fsave.write(SAVING)
                        Fsave.close
                        await Rebeca.send_message(message.channel,"Réponse enregistrée")
                    elif Nxt == None:
                        await Rebeca.send_message(message.channel,"Délai de réponse expiré")
                else:
                    waitID.append(message.author.id)
                    await Rebeca.send_message(message.channel,"Je ne connais pas de réponse pour ça...")
            else:
                LastMesBot = await Rebeca.send_message(message.channel,Answer)
                if REACTadj:
                    await Rebeca.add_reaction(LastMesBot,Searched_Emotes[0])
                    await Rebeca.add_reaction(LastMesBot,Searched_Emotes[1])
                    await Rebeca.add_reaction(LastMesBot,Searched_Emotes[2])
                    react = await Rebeca.wait_for_reaction(Searched_Emotes,user=message.author,message=LastMesBot)
                    print("Réaction captée!")
                    if react == None:
                        await Rebeca.send_message(message.channel,"Temps écoulé pour réagir!")
                    else:
                        if react[0].emoji == Searched_Emotes[0]:
                            AI.add_adj(LastMesBot.content.split(" ")[1],0,FileForD)
                            await Rebeca.send_message(message.channel,"Nouvel adjectif enregistré comme étant mélioratif!")
                        if react[0].emoji == Searched_Emotes[1]:
                            AI.add_adj(LastMesBot.content.split(" ")[1],1,FileForD)
                            await Rebeca.send_message(message.channel,"Nouvel adjectif enregistré comme étant péjoratif!")
                        if react[0].emoji == Searched_Emotes[2]:
                            AI.add_adj(LastMesBot.content.split(" ")[1],2,FileForD)
                            await Rebeca.send_message(message.channel,"Nouvel adjectif enregistré comme n'étant ni mélioratif ni péjoratif!")
    elif message.author.id != "543774755258499083":
        print("OK!")
        #£wash
        if message.content.startswith("£wash") and message.author.id == "358520708932042754":
            tmp = await Rebeca.send_message(message.channel, "J'efface tout de suite!")
            M = []
            async for msg in Rebeca.logs_from(message.channel):
                M.append(msg)
            await Rebeca.delete_messages(M)
        if message.content.startswith("£dif") and message.author.id == "358520708932042754":
            print("OKEEE!")
            M = message.content[5:]
            Chan = M.split(" ")[0]
            print(Chan)
            M = M[len(Chan)+1:]
            Chan = Rebeca.get_channel(Chan)
            if Chan == None:
                await Rebeca.send_message(message.channel,"Salon non trouvé")
            else:
                await Rebeca.send_message(Chan,M)
    return
Rebeca.run("NTQzNzc0NzU1MjU4NDk5MDgz.D0BfQQ.1rWPGT4JqnBvl1tCqc3hniBmRRg")
