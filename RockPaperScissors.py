#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')

while (1<2):
    print ("\n")
    print ("Rock Paper Scissors - Shoot")
    userChoice = input("Choose your weapon [R]ock, [P]aper or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter")
        print ("[R]ock, [P]aper or [S]cissors")
        continue
        
#Echo user's choice

    print ("You chose",userChoice)
    choices = ['R','P','S']
    opponentChoice = random.choice(choices)
    print ("l chose: ",userChoice)
    
    if opponentChoice == str.upper(userChoice):
        print ("Tie")
    
    elif opponentChoice == 'R' and userChoice.upper()=='S':
        print ("Scissors beat Rock, I win")
        continue
    elif opponentChoice == 'S' and userChoice.upper() =='P':
        print ("Scissors beats paper, I win")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beat rock, I win")
        continue
    else:
        print ("Win")


# In[ ]:




