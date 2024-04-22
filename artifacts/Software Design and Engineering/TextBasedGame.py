# Anaid Rodriguez

def instructions():             # instructions include all possible commands to type in
    print('''Collect all the fingerprints as evidence and try not to end up in a room with the killer.
        You can move around the house when prompted by '>>>' with any of the following commands:
        'Go North, Go South, Go West, Go East'.
        Also, collect evidence in any room, except the Hall, when you see ** by typing in 'collect' ''')


def main():
    evidence = []
    rooms = {            # all the rooms include their connection to other rooms and the 'item' (person), in them
        'Hall': {'go north': 'Library', 'go east': 'Ballroom', 'name': 'Hall'},
        'Library': {'go south': 'Hall', 'go east': 'Kitchen', 'name': 'Library', 'item': 'Miss Scarlett'},
        'Kitchen': {'go west': 'Library', 'go east': 'Conservatory', 'go south': 'Dining Room',
                    'name': 'Kitchen', 'item': 'Dr. Clue'},
        'Conservatory': {'go west': 'Kitchen', 'go south': 'Study', 'name': 'Conservatory', 'item': 'Mrs. Peacock'},
        'Dining Room': {'go north': 'Kitchen', 'go east': 'Study', 'name': 'Dining Room', 'item': 'Dr. Orchid'},
        'Ballroom': {'go west': 'Hall', 'go south': 'Lounge', 'name': 'Ballroom', 'item': 'Mr.Green'},
        'Lounge': {'go north': 'Ballroom', 'name': 'Lounge', 'item': 'Prof. Plum'},
        'Study': {'item': 'Col. Mustard the killer'}
    }
    commands = 'go north', 'go south', 'go west', 'go east'  # the four possible commands the user can input to move
    player_location = rooms['Hall']          # the player starts in the Hall

    def player():           # this function is to show the player their stats: location and their inventory
        print('-' * 24)
        print('You are in the', player_location['name'])
        print('Evidence:', evidence)

    def winning():  # this function is called if the player collects all the items and has won
        print('Evidence:', evidence)
        print()
        print('''Congratulations!
        You collected all the evidence and correctly deduced the killer to be Col. Mustard.
        You've done it again detective, amazing work!''')

    def gathering_evidence():        # this function is called on when the player enters a room with an item
        if player_location['item'] not in evidence:
            print('Collect the fingerprints for evidence')
            while True:
                gather_item = input('**').casefold()
                if gather_item == 'collect':
                    evidence.append(player_location['item'])
                    print("Added {}'s fingerprints to evidence".format(player_location['item']))
                    break
                else:
                    print('-' * 24)
                    print("Don't forget the evidence")
        elif player_location['item'] in evidence:
            print("You already collected {}'s fingerprints".format(player_location['item']))
            print('Go ahead and keep moving')

    instructions()
    player()
    while True:  # if the player has added all items to their evidence list, the game ends, and they win
        if rooms['Library']['item'] in evidence and rooms['Kitchen']['item'] in evidence and rooms['Conservatory'][
            'item'] in evidence and rooms['Ballroom']['item'] in evidence and rooms['Dining Room']['item'] in evidence \
                and rooms['Lounge']['item'] in evidence:
            winning()
            break
        elif player_location == rooms['Study']:   # if the player walks into the study, where the villain is, they lose
            print('Oh no, you walked into the Study and Col. Mustard does not look happy to see you. Game over')
            break
        else:   # if the player hasn't won or lost yet, they will be prompted to walk around and collect evidence
            command = input('>>>').casefold()
            if command in commands:
                if command in player_location:
                    player_location = rooms[player_location[command]]  # places the player in their new room
                    if player_location == rooms['Study']:
                        continue  # if the player walks into the study, the main loop starts again
                    else:
                        player()  # if the player is not in the Study, the loop will print their stats
                        if player_location != rooms['Hall']:
                            print('You see {}'.format(player_location['item']))
                            gathering_evidence()  # function used to collect evidence is called on
                elif command not in player_location:
                    print('-' * 24)
                    print("There's no door that way!")
            else:
                print('Invalid command')


if __name__ == '__main__':
    main()
