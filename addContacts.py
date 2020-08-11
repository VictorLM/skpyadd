from skpy import Skype
import json
import time

user = input("User: ") 

message = input("Mensagem a ser enviada nos convites: ") 

sk = Skype(tokenFile=".tokens-" + user) # Carrega o token

currentUserId = sk.user.id # Pega ID do usuários atual

with open("contacts.json") as json_file:
    data = json.load(json_file)
    print ("Cada contato leva 5 segundos para ser adicionado, para evitar bloqueios e exceções.")
    for value in data:
        if value["id"] != currentUserId:
            sk.contacts[value["id"]].invite(message)
            print ("Adicionado o contato: " + value["nome"]) # Se seu contacts.json não tiver as chaves "nome", comente essa linha
            time.sleep(5) # Para não levantar uma SkypeAuthException "Auth rate limit exceeded"
