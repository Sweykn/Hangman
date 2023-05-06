import random
import hangmanart
import hangmanwords
import os
print(hangmanart.logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
chosen_word = random.choice(hangmanwords.word_list)
display=[]
for let in chosen_word:
      display.append("_")
print(display)
lives=6
count=0

while "_" in display and lives>0:
  guess = input("Guess a letter: ").lower()
  os.system('cls')
  i=0
  if guess in display:
    print(f"Enter a different letter {guess} is already filled.")
  while i<len(chosen_word):
        if guess==chosen_word[i]:
           display[i]=guess
           count+=1
        i=i+1
  if count==0:
        lives=lives-1
        print(stages[lives])
        print(f"{guess} is not the answer. Sorry You lose a life")
  count=0
  print(display)
if "_" not in display and lives>0:
  print(f"You WIN🤩The answer is {chosen_word}")
elif lives==0:#else: also can be written
  print("You are out!!😶‍🌫️No more lives🥁")
  print(f"The answer is {chosen_word}")
