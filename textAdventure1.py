print('''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
''')

user_input = input("Type 'left' to go left or 'right' to go right. ")

if user_input == "left":
    print("You decide to go left and you approach a lake. Do you swim across or go around?")
    done = True

    user_input = input("Type 'across' to go across or 'around' to go around. ")
    
    if user_input == "across":
        print("You decide to go across and you are attacked by a shark!")
        done = True
        
        print("Do you fight or try to swim away?")
        user_input = input("Type 'fight' to fight the shark or 'swim' to try to flee. ")

        if user_input == "fight":
            print("You decide to fight the shark and are successful in finding an underwater maze exit - YOU WON!")
            done = True

        elif user_input == "swim":
            print("You decide to swim and the shark catches up to you and eats you - GAME OVER")
            done = True
	
    elif user_input == "around":
        print("You decide to go around and make it safely to the other side of the lake.")
        done = True
        
        print("You've crossed the lake - do you turn left or right")
        user_input = input("Type 'left' to turn left or 'right' to turn right. ")

        if user_input == "left":
            print("You turn right and there's a giant abyss in front of you.")
            done = True
            
            print("There's a giant abyss in front of you - do you jump across or try to walk around?")
            user_input = input("Type 'jump' to jump across or 'walk' to walk around. ")

            if user_input == "jump":
                print("You make it across and exit the maze - YOU WON!")
                done = True

            elif user_input == "walk":
                print("You lose your balance and fall into the abyss, leading to the Forbidden Forest, where you are killed by centaurs - GAME OVER!")
                done = True

        elif user_input == "right":
            print("You turn right and lose your soul to the Dementor's kiss after failing to produce a Patronus - GAME OVER!")
            done = True

if user_input == "right":
    print("You decide to go right and you approach a lake. Do you swim across or go around?")
    done = True

    user_input = input("Type 'across' to go across or 'around' to go around. ")
    
    if user_input == "across":
        print("You decide to go across and you are attacked by a shark!")
        done = True
        
        print("Do you fight or try to swim away?")
        user_input = input("Type 'fight' to fight the shark or 'swim' to try to flee. ")

        if user_input == "fight":
            print("You decide to fight the shark and are successful in finding an underwater maze exit - YOU WON!")
            done = True

        elif user_input == "swim":
            print("You decide to swim and the shark catches up to you and eats you - GAME OVER")
            done = True
	
    elif user_input == "around":
        print("You decide to go around and make it safely to the other side of the lake.")
        done = True
        
        print("You've crossed the lake - do you turn left or right")
        user_input = input("Type 'left' to turn left or 'right' to turn right. ")

        if user_input == "left":
            print("You turn right and there's a giant abyss in front of you.")
            done = True
            
            print("There's a giant abyss in front of you - do you jump across or try to walk around?")
            user_input = input("Type 'jump' to jump across or 'walk' to walk around. ")

            if user_input == "jump":
                print("You make it across and exit the maze - YOU WON!")
                done = True

            elif user_input == "walk":
                print("You lose your balance and fall into the abyss, leading to the Forbidden Forest, where you are killed by centaurs - GAME OVER!")
                done = True

        elif user_input == "right":
            print("You turn right and lose your soul to the Dementor's kiss after failing to produce a Patronus - GAME OVER!")
            done = True
