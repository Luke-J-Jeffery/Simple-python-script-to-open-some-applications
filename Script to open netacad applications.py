# script to open netacad resources for class
import os 
import webbrowser
import subprocess
import pyautogui
import time
import AppOpener

pyautogui.FAILSAFE = True

print ("Running Netacad resources for your class, please wait, do not touch your mouse!.")

#this opens the applications
AppOpener.open("obs studio 64bit", match_closest=True)
webbrowser.open("https://www.netacad.com/dashboard")
time.sleep(3)

#clicks the login button
pyautogui.moveTo(2552, 1347)
pyautogui.click()
time.sleep(3)

#clicks the email to login with
pyautogui.moveTo(2099, 1059)
pyautogui.click()
time.sleep (2)
 
webbrowser.open("")

#Interaction with Teams link to "accept" the link
time.sleep(2)

pyautogui.moveTo(1979, 1220)
pyautogui.click()

#This opens OBS for recording 
time.sleep(2)


