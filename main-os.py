import os
from select import select
import time
import socket
import sys
import datetime

login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

print("""
██╗░░░░░██╗░░░██╗██╗░░░░░░█████╗░███████╗░█████╗░░██████╗
██║░░░░░██║░░░██║██║░░░░░██╔══██╗██╔════╝██╔══██╗██╔════╝
██║░░░░░██║░░░██║██║░░░░░██║░░╚═╝█████╗░░██║░░██║╚█████╗░
██║░░░░░██║░░░██║██║░░░░░██║░░██╗██╔══╝░░██║░░██║░╚═══██╗
███████╗╚██████╔╝███████╗╚█████╔╝███████╗╚█████╔╝██████╔╝
╚══════╝░╚═════╝░╚══════╝░╚════╝░╚══════╝░╚════╝░╚═════╝░
""")
print("Welcome " + l_n + "!")

print("""
[1] Open Lulce-Pad
[2] Open Lulce-Explorer
[3] Open Lulce-Time
[4] Quit Lulce-Os Safley
""")
select = input("[?]: ")

if select == '1':
    os.startfile('notepad.pyw')

if select == '2':
    os.startfile('explorer.pyw')

if select == '3':
    os.startfile('time.pyw')

if select == '4':
    os.startfile('bye.py')
