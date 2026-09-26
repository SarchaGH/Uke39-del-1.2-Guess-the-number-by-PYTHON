
import random#random
import os#clear
os.system("cls")

low=1#less
high=0#max

guesses=0#guesses
guesses2=0#round

point=0

#greeting
Hitext=("Hello!","Hei på deg!","Let's start!")
Hi=random.choice(Hitext)
print(Hi)

#name
playername=(input(f"pls enter your name : "))

"""============================================================================================================================================="""

#level
level=int(input(f"pls enter difficulty level 1,2,3,4 /4 is recommended:) : "))

if level==1:
  high=100

elif level==2:
  high=200

elif level==3:
  high=500

elif level==4:
  high=10000

else:
   print("No level selected:(")
   quit()

"""===================================================================1========================================================================="""
number=random.randint(low,high)#random the number

while True:
 guesses=int(input(f"Enter number between({low}-{high})"))
 guesses2 += 1

 if guesses < number:
   os.system("cls")
   print(f"{guesses} is too low try again!")
   
 elif guesses > number:
   os.system("cls")
   print(f"{guesses} is too high try again!")
  
 else:
   options=("nice!","correct!","Good job!","You got it!","MOOOOO~~~", "That KUU","67")
   
   Ku1=random.choice(options)
   print(Ku1)
   print(r'     \   ^__^')
   print(r'      \  (oo)\_______')
   print(r'         (__)\       )')
   print(r'             ||----W |')
   print(r'             ||     ||')
  
   if guesses2 <= 4:
    print(f"Unbelievable! You guessed it in just{guesses2} time.")
    point+=4
   elif guesses2 <= 7:
    print(f"Pretty good! This round took you {guesses2} guesses.")
    point+=2
   else:
    print(f"Finally! It took you {guesses2} guesses.")
    point+=1
   break
"""=================================================================2========================================================================="""
play_again = input("Play again? (y/n): ").lower()

if play_again == "y":
 os.system("cls")
 guesses2 = 0
 point = 0
 number = random.randint(low, high)
 while True:
  guesses=int(input(f"Enter number between({low}-{high})"))
  guesses2 += 1

  if guesses < number:
   os.system("cls")
   print(f"{guesses} is too low try again!")
   
  elif guesses > number:
   os.system("cls")
   print(f"{guesses} is too high try again!")
  
  else:
   options=("nice!","correct!","Good job!","You got it!","MOOOOO~~~", "That KUU","67")
   
   Ku1=random.choice(options)
   print(Ku1)
   print(r'     \   ^__^')
   print(r'      \  (oo)\_______')
   print(r'         (__)\       )')
   print(r'             ||----W |')
   print(r'             ||     ||')
  
   if guesses2 <= 4:
    print(f"Unbelievable! You guessed it in just{guesses2} time.")
    point+=4
   elif guesses2 <= 7:
    print(f"Pretty good! This round took you {guesses2} guesses.")
    point+=2
   else:
    print(f"Finally! It took you {guesses2} guesses.")
    point+=1
   break

else:
   print(f"Good bye {playername} you got {point}/4 points!")
   quit()

"""=================================================================3==========================================================================="""
play_again = input("Play again? (y/n): ").lower()

if play_again == "y":
 os.system("cls")
 guesses2 = 0
 point = 0
 number = random.randint(low, high)
 while True:
  guesses=int(input(f"Enter number between({low}-{high})"))
  guesses2 += 1

  if guesses < number:
   os.system("cls")
   print(f"{guesses} is too low try again!")
   
  elif guesses > number:
   os.system("cls")
   print(f"{guesses} is too high try again!")
  
  else:
   options=("nice!","correct!","Good job!","You got it!","MOOOOO~~~", "That KUU","67")
   
   Ku1=random.choice(options)
   print(Ku1)
   print(r'     \   ^__^')
   print(r'      \  (oo)\_______')
   print(r'         (__)\       )')
   print(r'             ||----W |')
   print(r'             ||     ||')
  
   if guesses2 <= 4:
    print(f"Unbelievable! You guessed it in just{guesses2} time.")
    point+=4
   elif guesses2 <= 7:
    print(f"Pretty good! This round took you {guesses2} guesses.")
    point+=2
   else:
    print(f"Finally! It took you {guesses2} guesses.")
    point+=1
   break

else:
   print(f"Good bye {playername} you got {point}/8 points!")
   quit()

"""===================================================================4========================================================================"""   
play_again = input("Play again? (y/n): ").lower()

if play_again == "y":
 os.system("cls")
 guesses2 = 0
 point = 0
 number = random.randint(low, high)
 while True:
  guesses=int(input(f"Enter number between({low}-{high})"))
  guesses2 += 1

  if guesses < number:
   os.system("cls")
   print(f"{guesses} is too low try again!")
   
  elif guesses > number:
   os.system("cls")
   print(f"{guesses} is too high try again!")
  
  else:
   options=("nice!","correct!","Good job!","You got it!","MOOOOO~~~", "That KUU","67")
   
   Ku1=random.choice(options)
   print(Ku1)
   print(r'     \   ^__^')
   print(r'      \  (oo)\_______')
   print(r'         (__)\       )')
   print(r'             ||----W |')
   print(r'             ||     ||')
  
   if guesses2 <= 4:
    print(f"Unbelievable! You guessed it in just{guesses2} time.")
    point+=4
   elif guesses2 <= 7:
    print(f"Pretty good! This round took you {guesses2} guesses.")
    point+=2
   else:
    print(f"Finally! It took you {guesses2} guesses.")
    point+=1
   break

else:
   print(f"Good bye {playername} you got {point}/12 points!")
   quit()

"""===================================================================5========================================================================"""   
play_again = input("Play again? (y/n): ").lower()

if play_again == "y":
 os.system("cls")
 guesses2 = 0
 number = random.randint(low, high)
 while True:
  guesses=int(input(f"Enter number between({low}-{high})"))
  guesses2 += 1

  if guesses < number:
   os.system("cls")
   print(f"{guesses} is too low try again!")
   
  elif guesses > number:
   os.system("cls")
   print(f"{guesses} is too high try again!")
  
  else:
   options=("nice!","correct!","Good job!","You got it!","MOOOOO~~~", "That KUU","67")
   
   Ku1=random.choice(options)
   print(Ku1)
   print(r'     \   ^__^')
   print(r'      \  (oo)\_______')
   print(r'         (__)\       )')
   print(r'             ||----W |')
   print(r'             ||     ||')
  
   if guesses2 <= 4:
    print(f"Unbelievable! You guessed it in just{guesses2} time.")
    point+=4
   elif guesses2 <= 7:
    print(f"Pretty good! This round took you {guesses2} guesses.")
    point+=2
   else:
    print(f"Finally! It took you {guesses2} guesses.")
    point+=1
   print(f"Good bye {playername} you got {point}/20 points and the game is Over!")
   break
  
else:
   print(f"Good bye {playername} you got {point}/ 16 poins!")
   quit()

"""##############################################################ENDDDDDD#######################################################################"""