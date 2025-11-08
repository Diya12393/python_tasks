"""
IPL GAME : 2025

    CSK  RCB  KKR  MI  KXIP

    Enter your team :

Opp.Team : Randomly  (not same as your team)

-----------------------------------------------
Toss Time : 

     Enter your choice : H/T

     Actual Toss : (Randomly)

     if you win toss - choose bat or bowl
-----------------------------------------------
"""

print("IPL GAME  :  2025")

import random

teams = ["CSK","RCB","KKR","KI","KXIP"]

opp_team = 0

team = input("Enter your team  : ")

print=(random.choice(teams))

if team == "RCB" and opp_team == "KKR":
    print("RCB")

elif team == "KKR" and opp_team == "RCB":
    print("KKR")

elif team == "KKR" and opp_team == "RCB":
    print("KKR")


elif team == "KI" and opp_team == "KXIP":
    print("KXIP")


elif team == "KXIP" and opp_team == "KI":
    print("KI")

else:
    print("Enter your team")
    
    
    
