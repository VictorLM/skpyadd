from skpy import Skype
import json

user = input("User: ") 

sk = Skype(tokenFile=".tokens-" + user) # Carrega o token

currentUserId = sk.user.id # Pega ID do usuários atual

with open("contacts.json") as json_file:
    data = json.load(json_file)
    for value in data:
        if value["id"] != currentUserId:
            sk.contacts[value["id"]].invite("Poderia me adicionar, por favor?")
