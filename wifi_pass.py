import subprocess

def string_convert(s):
    stri = ""
    for w in s:
        stri += w
    return stri


subprocess.os.system("ipconfig > info.txt")
flag = 0
file = open("info.txt","r")

for w in file:
    if "Windows" in w:
        flag = 1
        break
    else:
        continue

if flag == 0:
    print("This script runs only on Windows!")
    subprocess.os.system("rm info.txt")
    exit()

file.close()

subprocess.os.system("echo "" > creds.txt")
subprocess.os.system("netsh wlan show profiles > pass.txt")

print("[+]Gathering SSID's saved in the system")
fhandle = open("pass.txt","r")

for words in fhandle:

    if "All" in words:
        line = words.split()
        user = line[4]
        s = "netsh wlan show profile ",user," key=clear >> paste.txt"
        str = string_convert(s)
        subprocess.os.system(str)

fhandle.close()

fh = open("paste.txt","r")
fhand = open("creds.txt","w")

print("[+]Gathering passwords")

for w in fh:
    if "Name" in w or "Content" in w or "Absent" in w:
        line = w.split()
        if "Name" in line:
            user = line[2]
            s = "    SSID:",user
            str = string_convert(s)
            fhand.write(str)
            fhand.write("\n")
        elif "Content" in line:
            passwd = line[3]
            s = "password:",passwd
            str = string_convert(s)
            fhand.write(str)
            fhand.write("\n\n")
            continue
        elif "Absent" in line:
            fhand.write("password:-NA-")
            fhand.write("\n\n")
            continue

fhand.close()
fh.close()

print("[+]The credentials are saved in:'creds.txt'")
subprocess.os.system("del pass.txt")
subprocess.os.system("del paste.txt")
subprocess.os.system("del info.txt")
