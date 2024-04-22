"""
__author__ = "Anaid Rodriguez"
__file__ = "Text Based Game"
__institution__ = "Southern New Hampshire University"
__course__ = "CS-499 Computer Science Capstone"
__assignment__ = "3-2 Milestone Two: Enhancement One: Software Design and Engineering"
__date__ = 03/24/2024
__version__ = "2.0"
"""

import time
# as part of the enhancement, almost all functionality is written outside of the main function, starting with the dictionaries
# nested dictionary that links all the rooms together along with all the evidence for the EASY difficulty level
rooms_easy_mode = {
    "HALL": {"name": "HALL", "go north": "OFFICE", "go west": "CONSERVATORY", "go east": "GUEST RESTROOM", "evidence": "none"},
    "CONSERVATORY": {"name": "CONSERVATORY", "go east": "HALL", "go west": "LIBRARY", "evidence": "Fingerprints"},
    "LIBRARY": {"name": "LIBRARY", "go east": "CONSERVATORY", "go north": "MAIN BEDROOM", "evidence": "Potential weapon"},
    "MAIN BEDROOM": {"name": "MAIN BEDROOM", "go south": "LIBRARY", "evidence": "Cryptic Note"},
    "GUEST RESTROOM": {"name": "GUEST RESTROOM", "go west": "HALL", "go east": "GUEST ROOM", "evidence": "Bloody rag"},
    "GUEST ROOM": {"name": "GUEST ROOM", "go west": "GUEST RESTROOM", "go north": "Room 7", "evidence": "Burner phone"},
    "STORAGE ROOM": {"name": "STORAGE ROOM", "go south": "OFFICE", "go east": "Room 7", "evidence": "Broken glass"},
    "Room 7": {"name": "Room 7", "evidence": "none"},
    "OFFICE": {"name": "The OFFICE", "go south": "HALL", "go north": "STORAGE ROOM", "evidence": "Forced entry"}
}

# as part of the enhancement, a hard mode difficulty level is added to the game
# nested dictionary that holds and links all the rooms and the evidence for the HARD difficulty level
rooms_hard_mode = {
    "HALL": {"name": "HALL", "go north": "CONSERVATORY", "evidence": "none"},
    "CONSERVATORY": {"name": "CONSERVATORY", "go south": "HALL", "go west": "LIBRARY", "go east": "HOME THEATER", "evidence": "Fingerprints"},
    "LIBRARY": {"name": "LIBRARY", "go east": "CONSERVATORY", "go west": "MAIN BEDROOM", "go south": "GUEST RESTROOM", "go north": "Room 3", "evidence": "Potential weapon"},
    "Room 3": {"name": "Room 3", "evidence": "none"},
    "MAIN BEDROOM": {"name": "MAIN BEDROOM", "go east": "LIBRARY", "go north": "GUEST ROOM", "evidence": "Cryptic Note"},
    "GUEST RESTROOM": {"name": "GUEST RESTROOM", "go north": "LIBRARY", "evidence": "Bloody rag"},
    "GUEST ROOM": {"name": "GUEST ROOM", "go south": "MAIN BEDROOM", "go west": "SECOND BEDROOM", "go east": "Room 3", "go north": "OFFICE", "evidence": "Burner phone"},
    "OFFICE": {"name": "OFFICE", "go south": "GUEST ROOM", "go west": "GYM ROOM", "evidence": "Victim's phone"},
    "SECOND BEDROOM": {"name": "SECOND BEDROOM", "go north": "GYM ROOM", "go east": "GUEST ROOM", "evidence": "Forced entry"},
    "GYM ROOM": {"name": "GYM ROOM", "go east": "OFFICE", "go south": "SECOND BEDROOM", "evidence": "Muddy footprints"},
    "HOME THEATER": {"name": "HOME THEATER", "go west": "CONSERVATORY", "go south": "KITCHEN", "go north": "DINNING ROOM", "evidence": "Bullet casings"},
    "KITCHEN": {"name": "KITCHEN", "go north": "HOME THEATER", "evidence": "Freshly brewed coffee"},
    "DINNING ROOM": {"name": "DINNING ROOM", "go south": "HOME THEATER", "go west": "LAUNDRY ROOM", "go north": "THIRD BEDROOM", "evidence": "Burned note"},
    "THIRD BEDROOM": {"name": "THIRD BEDROOM", "go south": "DINNING ROOM", "go west": "SURVEILLANCE ROOM", "evidence": "Broken safe box"},
    "LAUNDRY ROOM": {"name": "LAUNDRY ROOM", "go east": "DINNING ROOM", "go north": "SURVEILLANCE ROOM", "go west": "Room 3", "evidence": "Broken glass"},
    "SURVEILLANCE ROOM": {"name": "SURVEILLANCE ROOM", "go south": "LAUNDRY ROOM", "go north": "BALCONY", "go west": "STORAGE ROOM", "go east": "THIRD BEDROOM", "evidence": "Tampered footage"},
    "BALCONY": {"name": "BALCONY", "go south": "SURVEILLANCE ROOM", "evidence": "Car keys on the floor"},
    "STORAGE ROOM": {"name": "STORAGE ROOM", "go east": "SURVEILLANCE ROOM", "go south": "Room 3", "evidence": "Latex gloves"}
}

# as part of the enhancement, I edited the text in the game to improve readibility and provide a better explanation about the purpose/goal of the game

# explains the background story to the player
def game_story():
    print('''
    You arrive at the crime scene per request of the local police department. 
    They require your detective skills to solve the recent murder of the owner of the manor. 
    You've been assured the house has been searched and there should be no one else inside
    so you can roam freely, gathering much needed evidence. However,
    as you near the front door you swear you see a light flicker, for a split second,
    in one of the windows...\n''')


# menu for the game. It explains the rules the player will be following
def game_rules():
    print('-' * 100)
    print('''Instructions: Explore the manor and gather potential evidence.
    To move from room to room enter any of the following commands:
        go west
        go north
        go east
        go south
    
    To collect evidence, enter the following command when you enter a room:
        collect
    
    To view the evidence you've gathered, type:
        view evidence
    
    To view this menu again throughout the game just enter:
        menu\n''')
    print('-' * 100)


# formally begins the game by giving the player their location and instruction to input directions
def game_beginning():
    print("\nYou open the front door, the first place you find yourself in is the HALL, what would you like to do?")


# function to verify the command inputted by the user is an acceptable one
def accepted_commands(command):
    # an exhaustive list of all the acceptable commands the player can input
    commands = ["go west", "go north", "go east", "go south", "menu", "view evidence"]
    if command in commands:
        return True
    else:
        return False

# as part of the enhancement, I made a function to check for valid moves rather than writing long and nested conditional statements in main
# function that checks if there is a door in the given direction
def accepted_directions(location, direction):
    if direction in location:
        return True
    else:
        return False

# as part of the enhancement, the functionality to gather evidence is written outside of main to produce reusable code
# function to check for and gather evidence from a room
def gather_evidence(location_item, evidence):

    if location_item == "none":  # if there is no evidence in that room
        print("There is no evidence in this room\n")

    elif location_item not in evidence:  # if the evidence in that room has not been collected
        print("Collect any evidence in the room")

        while True:
            player_input = input(">> ").casefold()
            if player_input == "collect":
                evidence.append(location_item)
                time.sleep(0.5)
                print("\nEvidence successfully collected:", location_item, "\n")
                break
            else:
                print("Hmm...there might be some evidence in this room\n")

    else:  # if evidence in that room has already been collected
        print("Evidence already collected from this room\n")


# message that prints out when the player wins
def player_wins():
    print("Congratulations! You collected all the evidence needed and are ready to make an arrest. "
          "Thank you for your help detective.")


# message that prints out when the player loses
def player_loses():
    print('''As you switch on the light in the room, you see a shadow move in your peripheral vision. 
    You turn your head toward it and reach for your weapon. But it's too late. 
    You're knocked off your feet and your back hits the cold floor within a second. 
    You hear the gunshot before you feel it...\n''')
    time.sleep(6)
    print("\nGAME OVER")


# function that checks if the player has won, lost, or neither yet in EASY mode
def enter_new_room_easy_mode(location, evidence):
    if location == rooms_easy_mode["Room 7"]:  # player loses by walking into room 7
        player_loses()
        exit()
    else:
        time.sleep(0.5)
        print("\nYou've entered the", location["name"])
        gather_evidence(location["evidence"], evidence)

        if len(evidence) == 7:  # player wins by collecting all 7 evidence needed
            player_wins()
        else:
            print("What would you like to do?")


# function that checks if the player has won, lost, or neither yet in hard mode
def enter_new_room_hard_mode(location, evidence):
    if location == rooms_hard_mode["Room 3"]:  # player loses by walking into room 3
        player_loses()
        exit()
    else:
        time.sleep(0.5)
        print("\nYou've entered the", location["name"])
        gather_evidence(location["evidence"], evidence)

        if len(evidence) == 16:  # player wins by collecting all 16 evidence needed
            player_wins()
        else:
            print("What would you like to do?")


# function that follows all the user's possible input through gameplay
def input_options(evidence, current_room, evidence_count, difficulty, rooms):

    while len(evidence) != evidence_count:  # loop will continue until all evidence items are collected

        command = input(">> ").casefold()  # user input command

        if accepted_commands(command):  # if player input is an acceptable command

            if command == "menu":  # if player wants to view the main menu
                game_rules()
                print("What would you like to do?")

            elif command == "view evidence":  # if the player wants to view their evidence list
                print(evidence)
                print("What would you like to do?")

            elif accepted_directions(current_room, command):  # if the player moves to a new room
                current_room = rooms[current_room[command]]
                difficulty(current_room, evidence)

            elif not accepted_directions(current_room, command):  # if direction is not valid
                print(" No door that way\n", "What would you like to do?")

        else:  # if player input is not an acceptable command
            print("Not a valid command")


# function that returns the difficulty level selected by the player
def difficulty_level():
    time.sleep(3)

    print("Mode: Easy (E) or Hard (H)")
    difficulty = input(">> ").casefold()
    while True:
        if difficulty == "e":  # input of 'e' is for easy mode
            return 1
        elif difficulty == 'h':  # input of 'h' is for hard mode
            return 2
        else:
            print("Please select a difficulty. Easy (E) or Hard (H)")  # loop will continue if there is no valid input
            difficulty = input(">> ").casefold()

# as part of the enhancement, the main function is greatly condensed and opts for calling functions rather than writing the whole program inside main
# main function
def main():

    evidence = []  # declare an empty evidence list
    game_story()
    game_rules()  # set up the start of the game

    difficulty = difficulty_level()  # call the function to ask the user to select difficulty level

    if difficulty == 1:  # if the player choose EASY mode to play
        game_beginning()
        current_room = rooms_easy_mode["HALL"]  # set the players initial location
        input_options(evidence, current_room, 7, enter_new_room_easy_mode, rooms_easy_mode)

    elif difficulty == 2:  # if the player choose HARD mode to play
        game_beginning()
        current_room = rooms_hard_mode["HALL"]  # set the players initial location
        input_options(evidence, current_room, 16, enter_new_room_hard_mode, rooms_hard_mode)

    else:
        print("Please select a difficulty level")


# run the program
if __name__ == '__main__':
    main()
