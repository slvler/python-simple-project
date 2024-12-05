#!/usr/bin/env python3

import hashlib
import os

# ___| |_   _| | ___ _ __
#/ __| \ \ / / |/ _ \ '__|
#\__ \ |\ V /| |  __/ |
#|___/_| \_/ |_|\___|_|
#A script written by slvler in November 2024 under GNU GENERAL PUBLIC LICENSE
#

base64="base64"
md5="md5"
sha1="sha1"
sha224="sha224"
sha256="sha256"
sha384="sha384"
sha512="sha512"

# Background Colors
REDBg = "\033[0;41m"
GREENBg = "\033[0;42m"
YELLOWBg = "\033[0;43m"
BLUEBg = "\033[0;44m"
PINKBg = "\033[0;45m"
CYANBg = "\033[0;46m"
WHITEBg = "\033[0;47m"

# Text Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
GRAY = "\033[38;5;242m"

# Underline Text Colors
URED = "\033[4;31m"
UGREEN = "\033[4;32m"
UYELLOW = "\033[4;33m"
UBLUE = "\033[4;34m"
UPINK = "\033[4;35m"
UCYAN = "\033[4;36m"
UWHITE = "\033[4;37m"

# Reset
RESET = "\033[0m"

# Help
def help():
    print("")
    print("a script for storing passwords in a secure format")
    print(f'to make it work {GREEN}sudo python3 generator-password.py{RESET}')
    print("----------------------------------------------------------")
    print(f'{CYAN}Create by {WHITE}: {RED} slvler {RESET}')
    print(f'{CYAN}Developer {WHITE}: {RED} https://github.com/slvler {RESET}')
    print(f'{CYAN}Version   {WHITE}: {RED} v1.0.0 {RESET}')

def qt():
    os.system('clear')
    print("")
    print("----------------------------------------------------------")
    print(f'{RED}EXİT{RESET}')
    print("")
    exit()


def menu():
    print("password creation menu")
    print("1- password")
    print("2- help")
    print("3- exit")

    choice = input("please make a choice: ")

    if choice == "1":
        password = str(input("enter the password: "))

        base64 = "base64"
        md5 = "md5"
        sha1 = "sha1"
        sha224 = "sha224"
        sha256 = "sha256"
        sha384 = "sha384"
        sha512 = "sha512"
        blake2b = "blake2b"
        blake2s = "blake2s"
        sha3_224 = "sha3_224"
        sha3_256 = "sha3_256"
        sha3_384 = "sha3_384"
        sha3_512 = "sha3_512"

        print(base64)
        print(md5)
        print(sha1)
        print(sha224)
        print(sha256)
        print(sha384)
        print(sha512)
        print(blake2b)
        print(blake2s)
        print(sha3_224)
        print(sha3_256)
        print(sha3_384)
        print(sha3_512)

        type = input("choose encryption type: ")

        if type == 'md5':
            print(f'hash: {hashlib.md5(password.encode()).hexdigest()}')
        elif type == 'sha1':
            print(f'hash: {hashlib.sha1(password.encode()).hexdigest()}')
        elif type == 'sha224':
            print(f'hash: {hashlib.sha224(password.encode()).hexdigest()}')
        elif type == 'sha256':
            print(f'hash: {hashlib.sha256(password.encode()).hexdigest()}')
        elif type == 'sha384':
            print(f'hash: {hashlib.sha384(password.encode()).hexdigest()}')
        elif type == 'sha512':
            print(f'hash: {hashlib.sha512(password.encode()).hexdigest()}')
        elif type == 'blake2b':
            print(f'hash: {hashlib.blake2b(password.encode()).hexdigest()}')
        elif type == 'blake2s':
            print(f'hash: {hashlib.blake2s(password.encode()).hexdigest()}')
        elif type == 'sha3_224':
            print(f'hash: {hashlib.sha3_224(password.encode()).hexdigest()}')
        elif type == 'sha3_256':
            print(f'hash: {hashlib.sha3_256(password.encode()).hexdigest()}')
        elif type == 'sha3_384':
            print(f'hash: {hashlib.sha3_384(password.encode()).hexdigest()}')
        elif type == 'sha3_512':
            print(f'hash: {hashlib.sha3_512(password.encode()).hexdigest()}')
        else:
            print("error")
            exit()
    elif choice == "2":
        help()
    elif choice == "3":
        qt()
    else:
        qt()

menu()
