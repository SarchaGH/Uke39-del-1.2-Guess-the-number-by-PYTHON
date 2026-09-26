# Uke39-del2-Guess-the-number-by-PYTHON

## In this repo is a game that call ***Guesses the number***

This game was made by **Python**, game play is the program will random a mystery number that player have to guess that number to get a **POINT**.
I also add a feature that player can chose the difficulty level between level 1-3, it also that me use the **coadding art(KUPRAT)** that will randomly the word to say when player success the game.

## This is EXP. for the coadding art

```python
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

  ```
