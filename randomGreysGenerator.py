import random

married = ["Mark Sloan", "Addison Montgomery", "Callie Torres", "Arizona Robbins", "Derek Shepherd", "Meredith Grey", "Preston Burke", "Denny Duquette", "Alex Karev"]
kid = ["Lexie Grey", "Sloan Reilly", "George O'Malley", "Jo Wilson", "Maggie Pierce", "Sophia Sloan", "Izzie Stevens", "Amelia Shepherd"]
person = ["Christina Yang", "Christina Yang", "Ellis Grey"]

print("Keep going to see your Grey's Anatomy future!")

m = random.choice(married)
print("You're married to " + m)

if m == "Denny Duquette":
    print("Sorry, you've been committed to the psych ward at the Grey Sloan Memorial Hospital.")
elif m == "Preston Burke":
    print("Be prepared to be abandoned at the altar.")
elif m == "Addison Montgomery":
    print("You get cheated on with Mark Sloan.")
elif m == "Mark Sloan":
    print("You get cheated on with Lexie Grey.")

k = random.choice(kid)
print("Your child is " + k)

if k == "Lexie Grey":
    print("Teach your child not to sleep with attendings, especially not the Head of Plastics.")
elif k == "Sloan Reilly":
    print("Be prepared to tell your spouse you slept with Mark Sloan.")
elif k == "Izzie Stevens":
    print("Your child is seriously sick - do something!")


p = random.choice(person)
print("Your person is " + p)

if p == "Ellis Grey":
    print("Sorry! Ellis forgot who you are and stabbed you!")
