error = False
try:
    import os
    from os import system
    system("title " + "Webhook Sniper")
except:
    pass
try:
    import requests
    import colorama
except:
    error = True
if error == True:
    print("Missing Modules, Press Enter To Start Repair Process")
    input("")
    try:
        import os
        os.system("pip install requests")
        os.system("pip install colorama")
        print("Problem May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Error While Fixing")
        input("")
        exit()


import random, time, threading
colorama.init(autoreset=True)
choice = "1234567890"
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def sniper():
    while True:
        id = random.choices(choice, k=18)
        id = "".join(id)
        code = random.choices(choices, k=68)
        code = "".join(code)
        webhook = "https://discord.com/api/webhooks/"+str(id)+"/"+str(code)
        r = requests.get(webhook)
        if "200" in str(r):
            print(colorama.Fore.GREEN + "Valid Webhook! "+webhook)
            if save == "y":
                valid = open("valid_webhooks.txt", "a")
                valid.write(webhook+"\n")
                valid.close()
        else:
            print(colorama.Fore.RED + "Invalid Webhook! "+webhook)
            if save == "y":
                invalid = open("invalid_webhooks.txt", "a")
                invalid.write(webhook+"\n")
                invalid.close()
        time.sleep(float(delay))
def valid():
    print("Enter A Valid Choice")
    return
while True:
    try:
        threads = input("Enter How Many Threads You Want: ")
        threads = int(threads)
        break
    except:
        valid()
while True:
    save = input("Wanna Auto Save Webhooks (y/n): ")
    if save == "y" or save == "n":
        break
    else:
        valid()
while True:
    try:
        delay = input("Enter Delay For Each Thread (0=NONE): ")
        delay = float(delay)
        break
    except:
        valid()
for u in range(int(threads)):
    threading.Thread(target=sniper).start()
    print("Started Thread")
