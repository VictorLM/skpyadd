from skpy import Skype
import json

user = input("User: ") 

sk = Skype(tokenFile=".tokens-" + user)

with open("contacts.json") as json_file:
    data = json.load(json_file)
    for value in data:
        sk.contacts[value["id"]].invite("Poderia me adicionar, por favor?")
