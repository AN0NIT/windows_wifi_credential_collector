## Windows_Wifi_Credential_Collector v2

## This python program collects saved wifi passwords in Windows system and copies them to a json format and can send it to your discord server via webhook.
## This script only works on Windows.

## Pre-requisites: python3 should be installed on the windows machine.
## Usage:	pip3 install -r requirements.txt
			python3 wifi_pass.py

## The credentials of the saved Wifi password will be available in json file in the same directory where the script has ran.
## The json file will be saved with a random name.
## You can set the SELF_DESTRUCT to 'True' if you dont want the file to be seen after running it.
## The json file will have the name of the System you got the file from and will be sent to your discord server if you change the 'DISCORD_WEBHOOK'.



## To create your Server Webhook(NOTE this can be done only via PC):
	1) Go to your server
	2) Select any channel
	3) Edit channel>Integrations>Webhooks>New Webhook
	4) Copy the Webhook url and paste it to the 'DISCORD_WEBHOOK' variable in the script and you are good to go.
	
	
## Warning:
## This script is meant for educational purpose ONLY.
## I am NOT responsible for any illegal activities done with the help of this script.
## Make sure you have PERMISSION to run this script on your victims machine before doing so.


## Feel free to edit this script to your liking and let me know if any changes I should make to the script from my side.
