# Basic programming concepts
# Try it out at trinket.io

# We're using Python, but these concepts are the same for any programming language
# But the syntax might be different

# variables

x = 5

# if/else

if x > 3:
  print("x is really big! x =", x)
  
x = 6

if x == 3:
  print("x is still 3")
else:
  print("x is not 3")
  
if x != 3:
  print("x != 3")
  
if x == 6:
  print("x is 6")

# lists

scores = [100, 93, 65, 78, 92, 34, 55]

print("Scores:", scores)

average = sum(scores) / len(scores)

print("Average:", average)

print("Max:", max(scores))

print("Min:", min(scores))
	

# loops (for, while)

for value in scores:
  if value >= 90:
    print(value, "A")
  elif value >= 80:
    print(value, "B")
  elif value >= 70:
    print(value, "C")
  elif value >= 60:
    print(value, "D")
  else:
    print(value, "F")

# functions

# A function has can have parameters and a return value

# Parameters variables that you pass into the function
# so you can execute code on different values

# Return can be used to send a result back

def letter_grade(value):
  if value >= 90:
    return "A"
  elif value >= 80:
    return "B"
  elif value >= 70:
    return "C"
  elif value >= 60:
    return "D"
  else:
    return "F"
  
for value in scores:
  print(value, letter_grade(value))

# classes

# Classes are like a template of how to store data.
# An "instance" of a class can be created with specific data.

class Pokemon:
	
	def __init__(self, name, hp, atk, defense, speed):
		# Store the variable on the instance of the pokemon
		self.name = name
		self.hp = hp
		self.atk = atk
		self.defense = defense
		self.speed = speed
		
	def pretty_print(self):
	  print(self.name, "hp:", self.hp, "atk:", self.atk, "defense:", self.defense, "speed:", self.speed)
	  
	def speed_check(self, otherPok):
	  if (self.speed == otherPok.speed):
	    print("Speed tie!")
	  elif (self.speed > otherPok.speed):
	    print(self.name, "is faster")
	  else:
	    print("Enemy", otherPok.name, "is faster")

pok1 = Pokemon("Bulbasaur", 30, 15, 18, 20)
pok2 = Pokemon("Charizard", 100, 30, 28, 30)

print(pok1)
print(pok1.name)


pok1.pretty_print()
pok1.speed_check(pok2)
pok2.speed_check(pok1)
pok1.speed_check(pok1)

# libraries

# instead of sum(scores) / len(scores), we can use a library

# import statistics
#print("library average:", statistics.mean(scores))	




# pygame
# Run platformer.py

# Improvement ideas:
# Change the level
# Add a different level
# Switch between the levels
# Move code that creates platforms out of Level1 and into a reusable function
# Add an image for the Player sprite
# Add enemies
# Change the sprite direction when moving left/right