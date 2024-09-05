import os
import time

print("""
██╗░░░░░██╗░░░██╗██╗░░░░░░█████╗░███████╗░█████╗░░██████╗
██║░░░░░██║░░░██║██║░░░░░██╔══██╗██╔════╝██╔══██╗██╔════╝
██║░░░░░██║░░░██║██║░░░░░██║░░╚═╝█████╗░░██║░░██║╚█████╗░
██║░░░░░██║░░░██║██║░░░░░██║░░██╗██╔══╝░░██║░░██║░╚═══██╗
███████╗╚██████╔╝███████╗╚█████╔╝███████╗╚█████╔╝██████╔╝
╚══════╝░╚═════╝░╚══════╝░╚════╝░╚══════╝░╚════╝░╚═════╝░
""")

print("""
[1] Continue with the setup
[2] I've already done the setup
""")
setup = input("[?]: ")

if setup == '1':
    name = input(str("Please enter your Username: "))
    pas = input(str("Please enter your password to login: "))

    with open('user/username.txt', "w") as f:
        f.writelines(name)

    with open('user/password.txt', "w") as f:
        f.writelines(pas)
    print("Setup completed!")
    time.sleep(3)
    os.startfile('main-os.py')
    quit()

elif setup == '2':
    try:
        with open('user/password.txt', 'r') as login_pass, open('user/username.txt', 'r') as login_name:
            l_p = login_pass.read().strip()
            l_n = login_name.read().strip()
    except FileNotFoundError:
        print("Error: Setup files not found. Please run the setup first.")
        quit()
else:
    print("Invalid option selected. Exiting.")
    quit()

while True:
    login = input("Please enter the password for " + l_n + " Username: ")
    if login == l_p:
        os.startfile('main-os.py')
        quit()
    else:
        print("Wrong Password!")




