import random

#Yingqi "Cheech" Li, 8/13/2024, Flash Karate Game, AI Camp, Created in under 90 minutes

#Array of Names
karateMovesNames = [
  "Oizuki",
  "Gyaku-zuki",
  "Age-zuki",
  "Mae Geri",
  "Mawashi Geri",
  "Yoko Geri",
  "Ushiro Geri",
  "Gedan Barai",
  "Uchi Uke",
  "Soto Uke",
  "Age Uke",
  "Empi",
  "Tetsui",
  "Kiba Dachi",
  "Zenkutsu Dachi",
  "Kokutsu Dachi",
  "Heian Shodan",
  "Pinan Shodan",
  "Bassai Dai",
  "O Goshi"
]

#Array of Explanations
karateMovesExplanations = [
  "Straight Punch",
  "Reverse Punch",
  "Uppercut",
  "Front Kick",
  "Roundhouse Kick",
  "Side Kick",
  "Back Kick",
  "Downward Block",
  "Inside Block",
  "Outside Block",
  "High Block",
  "Elbow Strike",
  "Hammerfist Strike",
  "Horse Stance",
  "Front Stance",
  "Back Stance",
  "Peaceful Mind",
  "Peaceful And Safe",
  "Break The Fortress",
  "Hip Throw"
]

#Game
points = 0
playAgain = True
print("Welcome to Flash Dojo!")
print("Student, What is your name?")
name = input()
print(name + "!" + " Let us Begin!")
while playAgain:
  #Shuffle Array
  temp = list(zip(karateMovesNames, karateMovesExplanations))
  random.shuffle(temp)
  karateMovesNames, karateMovesExplanations = zip(*temp)
  karateMovesNames = list(karateMovesNames)
  karateMovesExplanations = list(karateMovesExplanations)
  
  #Question
  for i in range(len(karateMovesNames)):
    print("What is the definition of: " + karateMovesNames[i])
    answer = input()
    if answer == karateMovesExplanations[i]:
      points += 1
      print("Correct!")
      if (points == 1):
        print("Current Score: " + str(points) + " point")
      else:
        print("Current Score: " + str(points) + " points")
    else:
      print("Incorrect!")
      if (points == 1):
        print("Current Score: " + str(points) + " point")
      else:
        print("Current Score: " + str(points) + " points")
        
  #End game statistics and taunts
  print("You got " + str(points) + " out of " + str(len(karateMovesNames)))
  if points == len(karateMovesNames):
    print("You are a Karate Master!")
  elif points >= len(karateMovesNames)/2 and points != len(karateMovesNames):
    print("You are pretty good at Karate!")
  elif points <= len(karateMovesNames)/2 and points != 0:
    print("You need to work on your Karate skills!")
  elif points == 0:
    print("SPEND MORE TIME AT THE DOJO PAL!")
    
  #Read statistics into scores file
  with open("scores.txt", "a") as f:
    f.write("Student: " + name + " " + "Score: " + str(points) + "\n")
    f.close()
    
  #Play again?
  print("Do you want to play again? (y/n)")
  answer = input()
  playAgain = bool(answer == "y" or answer == "Y")