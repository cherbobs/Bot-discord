#pip install discord.py 
#pip install nest_asyncio 


#La classe meme permet de definir les questions, indices et réponses
class meme:

  def __init__(self):
    self.question = ""
    self.indice = ""
    self.reponse = ""


#La classe blague permet de definir les blagues et les reponses
class blague:
  def __init__(self):
    self.question = ""
    self.reponse = ""


#On crée des liste pour les questions, indices et reponses pour les énigmes.

Question1 = [meme(), meme(), meme(), meme(), meme(), meme()]#"meme()"" definit la classe meme.

#Initialisation des questions, indices et des reponses 
Question1[0].question = "J'ai 32 faces: 20 hexagones et 12 pentagones, que suis-je?"
Question1[0].indice = "Je suis un objet blanc et noir"
Question1[0].reponse = "ballon"

Question1[1].question = "Je m'interroge mais je ne suis pas une question, que suis-je?"
Question1[1].indice = "Je suis le synonyme de dialogue, entretien et conversation"
Question1[1].reponse = "interview"

Question1[2].question = "Mon premier est un étendu de terre dans lequel on sème des céréales. Mon deuxième est la première personne du singulier. Mon troisième ne dit pas la vérité. Que suis-je?"
Question1[2].indice = "Mon tout est une modification, une transformation"
Question1[2].reponse = "changement"

Question1[3].question = 'https://i.pinimg.com/750x/15/20/cf/1520cf76794c4c9e3e1342431e64cab7.jpg'
Question1[3].indice = "C'est un homme"
Question1[3].reponse = "mbappe"

Question1[4].question = "Trouve le nom du meme"
Question1[4].indice = "Reprends tous les mots"
Question1[4].reponse = "le football il a changé"

Question1[5].question = 'https://www.youtube.com/watch?v=RRLZdX-GVu4'
Question1[5].reponse = ""
Question1[5].indice = ""

Question2 = [meme(), meme(), meme(), meme(), meme(), meme()]
Question2[0].question = "Quel est le contraire de ce matin?"
Question2[0].indice = "Quand la nuit tombe"
Question2[0].reponse = "ce soir"

Question2[1].question = "Quelle est l'action pour se nourrir?"
Question2[1].indice = "Ce qu'on fait au restaurant"
Question2[1].reponse = "manger"

Question2[2].question = "Quel est le céréal de la famille des poacée cultivé dans les région tropical?"
Question2[2].indice = "C'est un ingrédient de la paëlla"
Question2[2].réponse = "riz"

Question2[3].question = "Quel est l'examen qu'on passe au lycée?"
Question2[3].indice ="C'est un examen créé en 1808, mais sa premiere édition n'a lieu qu'en 1809"
Question2[3].reponse = "bac"

Question2[4].question = "Trouve le nom du meme"
Question2[4].indice = "Regroupe les réponses"
Question2[4].reponse = "ce soir on va manger du riz"

Question2[5].question = 'https://www.youtube.com/watch?v=YTS1ekPGCYc'
Question2[5].indice = ""
Question2[5].reponse = ""

Question3 = [meme(), meme(), meme(), meme(), meme(), meme()]
Question3[0].question = "Quel est le synonyme de cogner"
Question3[0].indice = "On le fait avant de rentrer dans une pièce"
Question3[0].reponse = "frapper"

Question3[1].question = "Quel personne font l'armée?"
Question3[1].indice = "Je suis un soldat"
Question3[1].reponse = "militaire"

Question3[2].question = "Comment donner un coup de pression?"
Question3[2].indice = "Intimider une personne"
Question3[2].reponse = "menacer"

Question3[3].question = "Quel est le synonyme d'absorber un produit toxique?"
Question3[3].indice = "Donner la mort avec du poison"
Question3[3].reponse = "empoisonner"

Question3[4].question = "Trouve le nom de meme?"
Question3[4].indice = "Utilise les réponses"
Question3[4].reponse = "frappe moi je t'empoisonne"

Question3[5].question = 'https://www.youtube.com/watch?v=SHkqSfQcyw0'
Question3[5].indice = ""
Question3[5].reponse = ""

Question = [Question1, Question2, Question3]

#On crée des liste pour les blagues et des reponses aux blagues
Blague = [blague(), blague(), blague(), blague(), blague()]

#Initialisation des questions et des indices
Blague[0].question = "Quel est l’arbre préféré du chômeur ?"
Blague[0].reponse = "le bouleau"

Blague[1].question = "Qu’est-ce qu’une frite enceinte ?"
Blague[1].reponse = "une patate sautée"

Blague[2].question = "Pourquoi est-ce qu'on met tous les crocos en taule ?"
Blague[2].reponse = "parce que les crocos dealent (crocodiles)"

Blague[3].question = "Où vont les biscottes pour danser ? "
Blague[3].réponse = "en biscothèque"

Blague[4].question = "Pourquoi les bières sont toujours stressées ? "
Blague[4].reponse = "parce qu'elles ont la pression"

#Les liens des GIF
Giphy= ['https://media3.giphy.com/media/5zhrKLEMIMS9oYicAi/giphy.gif?cid=ecf05e47613e9b024d7fd48be0bf276ca7021ce82a308262&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/IDMdMQ09Zf4782jiKd/giphy.gif?cid=ecf05e479801968c6e82de51d5c18b1700706e591e86f0cb&rid=giphy.gif&ct=g','https://media3.giphy.com/media/rrmf3fICPZWg1MMXOW/giphy.gif?cid=ecf05e4777a8bd5aee90e147970403c5ebf58861bedf1de4&rid=giphy.gif&ct=g','https://media2.giphy.com/media/g1m0KWxQOMZPUYiTGB/giphy.gif?cid=ecf05e47caa290a65aab1f3f60d70d7cae2a175f8f5a33b2&rid=giphy.gif&ct=g','https://media4.giphy.com/media/Ane45y5p7y0HZokoBw/giphy.gif?cid=790b761178526d7a138fed7f309a7b976b94e00869fcf166&rid=giphy.gif&ct=g','https://media3.giphy.com/media/3owzW9t7Fgt7JiFHfW/giphy.gif?cid=790b7611594e582cdab2639819558371d7f7419786615d0c&rid=giphy.gif&ct=g','https://media3.giphy.com/media/26FfaNt17wFTxUIrm/giphy.gif?cid=790b7611a7f43d08f564837b501b6c08ae8f4c3d254803a1&rid=giphy.gif&ct=g']

#Liste des insultes a ne pas dire 
insulte = ["pute","nike","niker","gueule", "nique", "niquer", "salope", "putain", "ptn"]

#Liste des mots à trouver pour le pendu
niveau1 = ["chat", "clair", "clou", "ciel", "velo", "jour", "nuit", "date"]
niveau2 = ["chasse", "doigts", "billet", "citron", "rosier", "saisir", "ballet", "entree"]

gif_fete = ['https://media2.giphy.com/media/Iqv8t7CZfszqbepTmi/giphy.gif?cid=790b761171bbe2becc9ce226fdbd036cfe75b19c02f00ee3&rid=giphy.gif&ct=g','https://media3.giphy.com/media/E1y9lqOznMwsYQa15m/giphy.gif?cid=790b761184cb7d2d445affb2a0d81beb967762c9382ee695&rid=giphy.gif&ct=g','https://media2.giphy.com/media/Ib07Kxbll4zVzbtZyJ/giphy.gif?cid=790b7611b0b2aed0778a01e8e27eaf44caf9807e3d84965c&rid=giphy.gif&ct=g','https://media1.giphy.com/media/XHXmd7Oq65kwDcvoni/giphy.gif?cid=790b7611bd3370806812fd0731f3c9fc10a1c154904f585f&rid=giphy.gif&ct=g','https://media4.giphy.com/media/32GBIdHx6g4Nfuuwrl/giphy.gif?cid=790b7611e9269a810173bcbc4e1c7d008e4c19df5ec2d7f9&rid=giphy.gif&ct=g']




import discord 
import nest_asyncio 
from discord.ext import commands
import random

nest_asyncio.apply()


intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.typing = True
client = discord.Client(intents=intents)


@client.event #C'est le client qui va les appeler
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044971326319902793) #nombre est l'ID du channel
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name + "/n J'éspère que tu vas bien. /n Je te propose plusieurs façons de t'amuser. /n Tu peux venir me voir pour jouer à différents jeux. /n Ecris ``quizz`` ou ``pendu`` si tu veux. /n Tu peux aussi avoir des ``blagues`` ou des ``gif``. /n Si tu ne te rappelles pas des différents jeux envoie ``help``.")


@client.event
async def on_message(message):
  
  global i , score, Blague, insulte, Question
  global niveau,niveau1, niveau2, nombre_lettre, tentatives, affichage, lettres_trouvees
  
  
  message.content = message.content.lower()
  
  if message.author == client.user:
    return
#Commande "help" sert à expliquer ce que le bot fait et propose 
  if "help" in message.content:
     await message.channel.send("Je te propose plusieurs façons de t'amuser. \n Tu peux venir me voir pour jouer à différents jeux. \n Ecris ``quizz`` ou ``pendu`` si tu veux. \n Tu peux aussi avoir des ``blagues`` ou des ``gif``.")

#Boucle qui permet de faire afficher "il ne faut pas dire ça" en cas d'insulte  
  for j in range (0,len(insulte)):
    if insulte[j] in message.content: 
      await message.channel.send("il ne faut pas dire ça")

#Permet d'afficher un gif aléatoire 
  if "gif" in message.content:
    b = random.randint(0, len(Giphy))
    await message.channel.send(Giphy[b])

#Permet d'afficher une blague aléatoire 
  if "blague" in message.content:
    a = random.randint(0,len(Blague))
    await message.channel.send(Blague[a].question)
    message = await client.wait_for("message")
    await message.channel.send(Blague[a].reponse)
 
 #Commencement du quizz 
  if "quizz" in message.content:
    i = 0
    score = 0
    await message.channel.send("Je vais te poser 4 questions et la dernière tu devras trouver le meme. \n Tu pourras chercher sur internet mais ne t'inquiètes pas je peux t'aider avec la fonction ``indice`` mais tu perdras 1 point. \n Trouver la réponse te rapporte 2 points. Tu peux à tout moment ``skip`` la question mais tu ne gagneras aucuns points. Si tu veux recommencer le test, tu auras juste à envoyer ``restart``. \n Veux-tu commencer le quizz?")
    d = random.randint(0,2)
    question = Question[d]
    message = await client.wait_for("message")
    if "oui" in message.content:
      await message.channel.send(question[i].question)
      i = i + 1
    else:
      return
    while i < 6:
      message = await client.wait_for("message")
      if message.author == client.user:
        return

      #Condition qui permet d'afficher l'indice de la question
      if "indice" in message.content:
        await message.channel.send(question[i-1].indice)
        score = score - 1
      elif question[i-1].reponse in message.content:

        await message.channel.send("bien joué")
        await message.channel.send(gif_fete[i - 1])
        score = score + 2
        await message.channel.send("ton score est de " + str(score))
        if i==6:
          await message.channel.send(question[5].question)
        await message.channel.send(question[i].question)
        i = i + 1
        
      #Condition qui permet de skip une question 
      elif "skip" in message.content:
        await message.channel.send("dommage, la réponse était " + question[i - 1].reponse)
        await message.channel.send("ton score est de " + str(score))
        await message.channel.send(question[i].question)
        i = i + 1

      #Condition qui permet de recommencer le quizz 
      elif "restart" in message.content:
        await message.channel.send("Allez on recommence")
        score = 0
        i = 0
        await message.channel.send(question[i].question)
        i = i + 1

  if "quoi"  in message.content or "koi" in message.content:
    await message.channel.send("feur")

  if "qui" in message.content:
    await message.channel.send("c'est kiki la vache qui rit")

#Jeu du pendu 
  if "pendu" in message.content:
    await message.channel.send("Il y a deux niveaux: ``facile`` et ``difficile``. \n Tu choisis ton niveau et tu es prêt à jouer. \n Le niveau facile ce sont des mots de 4 lettres et le niveau difficile ce sont des mots de 6 lettres. Pour les deux niveaux tu as 7 essais pour trouver les mots.")
    message = await client.wait_for("message")
    niveau = []
    nombre_lettre = 0
    affichage = ""

    #L'utilisatteur peut choisir entre un niveau difficile ou facile 
    if "facile" in message.content:
      niveau = niveau1
      affichage = "_ _ _ _ "
      nombre_lettre = 4
    elif "difficile" in message.content:
      niveau = niveau2
      affichage = "_ _ _ _ _ _ "
      nombre_lettre = 6
    solution = random.choice(niveau)
    print(solution)
    tentatives = 7
    lettres_trouvees = ""

    #commencement du jeu du pendu 
    await message.channel.send(">> Bienvenue dans le pendu << ")
    while tentatives > 0:
      await message.channel.send("\nMot à deviner : " + affichage)
      print(affichage)
      await message.channel.send("proposez une lettre : ")
      message = await client.wait_for("message")
      print(message)

      if message.content in solution:
        lettres_trouvees = lettres_trouvees + message.content
        await message.channel.send("-> Bien vu!")
      else:
        tentatives = tentatives - 1
        await message.channel.send("-> Nope\n")
        if tentatives==0:
          await message.channel.send(" ==========Y= ")
        if tentatives<=1:
          await message.channel.send(" ||/       |  ")
        if tentatives<=2:
          await message.channel.send(" ||        0  ")
        if tentatives<=3:
          await message.channel.send(" ||       /|\ ")
        if tentatives<=4:
          await message.channel.send(" ||       /|  ")
        if tentatives<=5:                    
          await message.channel.send("/||           ")
        if tentatives<=6:
          await message.channel.send("==============\n")
      affichage = ""
      for x in solution:
          if x in lettres_trouvees:
            affichage += x + " "
          else:
            affichage += "_ "

      if "_" not in affichage:
        await message.channel.send(">>> Gagné! <<<")
        tentatives = 0
#Fin du jeu du pendu 
    await message.channel.send("\n    * Fin de la partie *    ")


client.run("MTA0NDk2ODQwMDEwMDgwMjYxMA.GIdUFq.xRvYwdK2gjYcPG9aiUNCi3eNfSxueKfsKO9q34")


