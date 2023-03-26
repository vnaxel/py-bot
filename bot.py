# se connecter a ce serveur irc en tant que debool-pybot
# et envoyer un message privé a candy en lui disant '!ep1'
# et afficher la réponse

#Hôte	irc.root-me.org
#Protocole	IRC
#Port	6667
#Canal IRC	#root-me_challenge
#Bot	candy

import socket
import time
import math

# se connecter au serveur irc
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# definir le pseudo de mon bot
botnick = "debool-pybot"

# definir le pseudo du bot a contacter
botnick2 = "candy"

# definir le canal irc
channel = "#root-me_challenge"

# definir le serveur irc
server = "irc.root-me.org"

# definir le port
port = 6667

# definir le message a envoyer
message = "!ep1"

def encode(text):
    return text.encode('UTF-8')

def decode(text):
    return text.decode('UTF-8')

# se connecter au serveur irc
irc.connect((server, port))
time.sleep(1)

# envoyer le pseudo au serveur irc
irc.send(encode("USER " + botnick + " " + botnick + " " + botnick + "This is a bot \n"))
irc.send(encode("NICK " + botnick + "\n"))

# rejoindre le canal irc
time.sleep(1)
irc.send(encode("JOIN " + channel + "\n"))

#on envoie le message privé au bot candy
time.sleep(1)
irc.send(encode("PRIVMSG " + botnick2 + " :" + message + "\n"))

# recevoir le texte du serveur irc en continu
while 1:
    text = decode(irc.recv(1024))
    print(text)

    # si le serveur nous envoie un message privé, on l'affiche
    if text.find('PRIVMSG') != -1:
        print(text)
    # si le message est de candybot, on recupere les nombres
        if text.find('Candy') != -1:
            # on recupere les nombres
            numbers = text.split(" :")[-1].split(" / ")
            for i in range(len(numbers)):
                print("Nombre numero " + str(i+1) + " : " + numbers[i]  + "\n")
            # on les convertit en entier
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            number = math.floor((math.sqrt(number1)*number2)*100)/100.0
            message = "!ep1 -rep " + str(number)
            irc.send(encode("PRIVMSG " + botnick2 + " :" + message + "\n"))








