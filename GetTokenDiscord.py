'# MADE BY Buraca 27
import requests
import time
import sys
import subprocess
import os

print("Any Question Ask Buraca 27#2714")


while True:
    email = str(input("E-mail: "))
    password = str(input("Password: "))

    payload = {
                "email": email,
                "password": password
              }

    r = requests.post('https://discord.com/api/v8/auth/login', json=payload).json()
    if "captcha_key" in r:
        print("A captcha is requested, the email entered is invalid or has been attempted too many times on connection. Rewrite your information.")
        time.sleep(1)
    elif "errors" in r:
        print("An error has occurred. Rewrite your information.")
    elif r["token"] == None:
        break
    else:
        print("-----------TOKEN-----------")
        print("Token: " + r["token"])
        time.sleep(5)
        sys.exit()

while True:
    if r["token"] == None:
        print("-----------2FA Authentication-----------")
        code = input("Enter the 2FA authentication code: ")
        mfa_payload = {
                        "code": code,
                        "ticket": r["ticket"]
                      }
        r2 = requests.post('https://discord.com/api/v8/auth/mfa/totp', json=mfa_payload).json()
        if "message" in r2:
            print("The 2FA authentication code is incorrect. Rewrite the code.")
            time.sleep(1)
        else:
            print("-----------TOKEN-----------")
            print("Token: " + r2["token"])
            time.sleep(5)
            sys.exit()