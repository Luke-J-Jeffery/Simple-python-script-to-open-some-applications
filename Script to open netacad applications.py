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
 
webbrowser.open("https://teams.microsoft.com/l/meetup-join/19%3ameeting_NzQ5NTcwYWYtYTdjZi00NjNlLTkwMDUtYTJlNTU0OWI1YzE2%40thread.v2/0?context=%7b%22Tid%22%3a%222ea71e92-b4ae-4606-b26e-515040700cb5%22%2c%22Oid%22%3a%2206553a61-09da-41f2-9c58-543c671c3cbc%22%7d")

#Interaction with Teams link to "accept" the link
time.sleep(2)

pyautogui.moveTo(1979, 1220)
pyautogui.click()

#This opens OBS for recording 
time.sleep(2)

