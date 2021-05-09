# Author - Joshua Comstock
# CSC119 Spring 2021
# This code is a text adventure game with notes explaining the diferent code purposes to make the code easy to read

# Importing libraries
import time		# Used to add wait time during printing
from termcolor import cprint 	# Used to print in different colors

# Defining first room function
def room1(inventory):
    UserChoice = None

    # Entering the first room
    print('You have entered the first room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "4":
        # Wait 2 seconds
        time.sleep(2)
        print('\nYou have now stopped after entering the first room. You notice a small oil lamp and turn it on for light. After you realize the lamp does not work you take out your flashlight and turn it on. "click" Now that you are ready, you start exploring the first room.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...')
            time.sleep(2)
            # User procedes to room2
            room2(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            time.sleep(1)
            # User procedes to room3
            room3(inventory)
            # User choses '3'
        elif UserChoice == '3':
            print('You have chosen to look around...')
            time.sleep(1)
            print('You have found the broken lamp. Do you want to keep it?\n1. Yes\n2. No')
            lampChoice = input()
            if lampChoice == '1':
                inventory.append('Broken Lamp')
                cprint('Broken lamp added to inventory', 'green')
            else:
                continue
        # User choses '4' and the game ends
        elif UserChoice == '4':
            quit()
        
        else:
            cprint('Please select a valid answer.', 'red')

# Defining second room function
def room2(inventory):
    UserChoice = None
    # Entering the second room
    print('You have entered the second room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 2. The second room is also dark so you keep your flashlight on. You notice old carvings on the wall as you observe your suroundings.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...')
            # Waits 1 second
            time.sleep(1)
            # User hits a dead end, returns to room 2
            cprint('You cannot go left, there is a wall blocking your way.', 'red')
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # User procedes back to room 1
            room1(inventory)
            # User choses '3'
        elif UserChoice == '3':
            print('You have chosen to look around...')
            time.sleep(1)
            cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            if 'Pick axe' in inventory:
                print('You have chosen to go forward...')
                # Wait 1 second
                time.sleep(1)
                # Procede to room 6
                room6(inventory)
            else:
                # Wait 1 second
                time.sleep(1)
                cprint('You cannot procede forward because the wall has collapsed. You need a pick axe in your inventory to procede forward.','red')
        # User goes backwards
        elif UserChoice == '5':
            cprint('You cannot go backwards, there is a wall blocking your way.', 'red')
        # User choses '5' and the game ends
        elif UserChoice == '6':
            quit()
        
        else:
            cprint('Please select a valid answer.', 'red')

# Defining third room function
def room3(inventory):
    UserChoice = None
    # Entering the second room
    print('You have entered the third room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 3. The third room is also dark so you keep your flashlight on.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...')
            # Waits 1 second
            time.sleep(1)
            # User returns to room 1
            room1(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            cprint('You cannot go right, there is a wall blocking your way.', 'red')
            # User choses '3'
        elif UserChoice == '3':
            if 'Pick axe' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find a pick axe\n')
                cprint('Pick axe added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Pick axe')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            room5(inventory)
        # User choses to go backwards
        elif UserChoice ==  '5':
            cprint('You cannot go backwards, there is a wall blocking your way.', 'red')
        # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        
        else:
            cprint('Please select a valid answer.', 'red')


# Defining fourth room function
def room4(inventory):
    UserChoice = None
    # Entering the fourth room
    print('You have entered the fourth room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 4. This second room is faintly lit with a small window letting the moonlight in.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            if 'Pick axe' not in inventory:
                # Wait 1 second
                time.sleep(1)
                cprint('You cannot procede left because the wall has collapsed. You need a pick axe in your inventory to procede forward.','red')
            elif 'pick axe' in inventory:
                print('You have chosen to go forward...')
                # Wait 1 second
                time.sleep(1)
                # Procede to room 6
                room6(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # User moves to room 5
            room5(inventory)
            # User choses '3'
        elif UserChoice == '3':
            if 'Mag Glass' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find a magnifing glass\n')
                cprint('Mag glass added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Mag Glass')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            time.sleep(1)
            # User moves to room 7
            room7(inventory)
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User moves back to room 1
            room1(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining fifth room function
def room5(inventory):
    UserChoice = None
    # Entering the fifth room
    print('You have entered the Fifth room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 5. This room is dark and a little more damp than the other rooms.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # Procede to room 4
            room4(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            cprint('You cannot go right, there is a wall blocking your way.', 'red')
            # User choses '3'
        elif UserChoice == '3':
            if 'Gem' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find a glowing gem\n')
                cprint('Gem added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Gem')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            time.sleep(1)
            # User moves to room 8
            room8(inventory)
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User moves back to room 3
            room3(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining sixth room function
def room6(inventory):
    UserChoice = None
    # Entering the sixth room
    print('You have entered the sixth room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # Cannot continue left
            cprint('You cannot go left, there is a wall blocking your way.', 'red')
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # User goes right to room 4
            room4(inventory)
            # User choses '3'
        elif UserChoice == '3':
            if 'Gold Key' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find a golden key\n')
                cprint('Golden Key added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Gold Key')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            time.sleep(1)
            # User moves to room 9
            room8(inventory)
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User moves back to room 3
            room3(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining seventh room function
def room7(inventory):
    UserChoice = None
    # Entering the seventh room
    print('You have entered the seventh room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 7. This room has a nasty oder, you think of going back. However your urge for adventure keeps you moving forward.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # Continues left
            print('You chose to go left...')
            # Continues to room 9
            room9(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # User goes right to room 8
            room8(inventory)
            # User choses '3'
        elif UserChoice == '3':
            if 'Gloves' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find gloves.\n')
                cprint('Gloves added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Gloves')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            time.sleep(1)
            # User moves to room 10
            room10(inventory)
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User moves back to room 4
            room4(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining eighth room function
def room8(inventory):
    UserChoice = None
    # Entering the eighth room
    print('You have entered the eighth room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 8. Room 8 is full of empty powder kegs. You asume it must have been a storage room or armory.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # Continues left
            print('You chose to go left...')
            # Continues to room 7
            room7(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # Cannot continue right
            cprint('You cannot go right, there is a wall blocking your way.', 'red')
        elif UserChoice == '3':
            if 'Pistol' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find pistol.\n')
                cprint('Pistol added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Pistol')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            time.sleep(1)
            # User moves to room 11
            room11(inventory)
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User moves back to room 5
            room5(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining nineth room function
def room9(inventory):
    UserChoice = None
    # Entering the eighth room
    print('You have entered the nineth room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 9. Room 9 is dark and has a old coat of arms on the wall.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # Cannot continue left
            cprint('You cannot go left, there is a wall blocking your way.', 'red')
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # User continues right to room 7
            room7(inventory)
            # User choses to look around
        elif UserChoice == '3':
            # There is nothing to find in this room
            cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward.')
            # Wait 1 second
            time.sleep(1)
            # User moves to room 12 if proper items are in inventory
            if 'Gold Key' and 'Pistol' and 'Gem' and 'Potion' in inventory:
                room12(inventory)
            else:
                cprint('You do not have all the needed items to continue to this room.', 'red')
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User moves back to room 6 if pick axe in inventory
            if 'Pick axe' in inventory:
                room5(inventory)
            else:
                cprint('You need a pick axe to enter this room.')
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining tenth room function
def room10(inventory):
    UserChoice = None
    # Entering the tenth room
    print('You have entered the tenth room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 10. Room 10 is an old wiches chamber. You see various brewing stands and potions.\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # User moves to room 12 if proper items are in inventory
            if 'Gold Key' and 'Pistol' and 'Gem' and 'Potion' in inventory:
                room12(inventory)
            else:
                cprint('You do not have all the needed items to continue to this room.', 'red')
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # User continues right to room 11
            room11(inventory)
            # User choses to look around
        elif UserChoice == '3':
            if 'Potion' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find a strength potion.\n')
                cprint('Potion added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Potion')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward...')
            # Waits 1 second
            time.sleep(1)
            # Cannot continue forward
            cprint('You cannot go forward, there is a wall blocking your way.', 'red')
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User goes back
            room7(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining eleventh room function
def room11(inventory):
    UserChoice = None
    # Entering the eleventh room
    print('You have entered the eleventh room!\n')
    # Wait 1 second
    time.sleep(1)

    # Looping code for users inputs
    while UserChoice != "6":
        # Wait 2 seconds
        time.sleep(2)
        print('You have now entered room 11. In this room you can hear an angry beast near by. You are nearing the end!\n')
        cprint("Inventory:" + str(inventory), "yellow")

        # Asking the user how they would like to continue
        print('\nWhat would you like to do? \nHint: Enter the number corresponding with the action you would like to make.\n1. Go left\n2. Go right\n3. Look around\n4. Go forward\n5. Go back\n6. Quit the game\n')

        # Asking the user for the input
        UserChoice = input()
        # User choses '1'
        if UserChoice == '1':
            print('You have chosen to go left...\n')
            # Waits 1 second
            time.sleep(1)
            # User procedes to room 10
            room10(inventory)
        # User choses '2'
        elif UserChoice == '2':
            print('You have chosen to go right...')
            # Waits 1 second
            time.sleep(1)
            # Cannot continue right
            cprint('You cannot go right, there is a wall blocking your way.', 'red')
            # User choses to look around
        elif UserChoice == '3':
            if 'Lightning Rod' not in inventory:
                print('You have chosen to look around...')
                # Wait for 1 second
                time.sleep(1)
                print('You look around and find a lightning rod.\n')
                cprint('Lightning Rod added to your inventory.', 'green')
                # Adds a pick axe to the inventory
                inventory.append('Lightning Rod')
            else:
                cprint('You found nothing of value.', 'grey', 'on_white')
        # User choses to go forward
        elif UserChoice == '4':
            print('You have chosen to go forward...')
            # Waits 1 second
            time.sleep(1)
            # Cannot continue forward
            cprint('You cannot go forward, there is a wall blocking your way.', 'red')
        # User choses to go backwards
        elif UserChoice ==  '5':
            print('You have gone back...')
            # Wait 1 second
            time.sleep(1)
            # User goes back
            room8(inventory)
         # User choses '6' and the game ends
        elif UserChoice == '6':
            quit()
        else:
            cprint('Please select a valid answer.', 'red')

# Defining twelfth room function
def room12(inventory):
    cprint('Congratulations! You have found the treasure and killed the beast with the pistol. You have won the game!', 'green')  
    quit()
# Def start function is going to be the function call for the start of the game, this will be called each time the game is reset. 
def start():
    # Game description
    inventory = ['Flashlight']
    # print game rules
    cprint('Welcome to my first text adventure game. The purpose of this game is to collect items throughout twelve rooms. The last room has an angry beast awaiting you. Make sure you are prepared with a weapon and with your strength. You will have an inventory where you will collect your items. Also, I suggest you have a piece of paper nearby to write down were you have been. Maybe even sketch out your rooms on the paper and create a map. Good luck!\n', 'green')
    # Wait 18 seconds 
    time.sleep(18)
    room1(inventory)
    
start()
