from skpy import Skype
from getpass import getpass

user = input("User: ") 

Skype(user, getpass(), ".tokens-" + user)
