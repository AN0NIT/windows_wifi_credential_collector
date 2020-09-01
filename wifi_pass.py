import os,sys

if os.name == 'nt':
    print("[+] Gathering SSID's saved in the system")
else:
    print("This script runs only on Windows!")
    sys.exit()

os.system("echo "" > creds.txt")
os.system("netsh wlan show profiles > pass.txt")


fhandle = open("pass.txt","r")

for words in fhandle:

    if "All" in words:
        line = words.split()
        user = line[4]
        os.system(f"netsh wlan show profile {user} key=clear >> paste.txt")

fhandle.close()

fh = open("paste.txt","r")
fhand = open("creds.txt","w")

print("[+] Gathering passwords")

for w in fh:
    if "Name" in w or "Content" in w or "Absent" in w:
        line = w.split()
        if "Name" in line:
            user = line[2]
            fhand.write(f"    SSID:{user}")
            fhand.write("\n")
        elif "Content" in line:
            passwd = line[3]
            fhand.write(f"password:{passwd}")
            fhand.write("\n\n")
            continue
        elif "Absent" in line:
            fhand.write("password:-NA-")
            fhand.write("\n\n")
            continue

fhand.close()
fh.close()

print("[!] The credentials are saved in:'creds.txt'")
os.system("del pass.txt")
os.system("del paste.txt")
