"""
__author__ = "Anaid Rodriguez"
__file__ = "Binary Search Tree Enhancement"
__institution__ = "Southern New Hampshire University"
__course__ = "CS-499 Computer Science Capstone"
__assignment__ = "4-2 Milestone Three: Enhancement Two: Algorithms and Data Structure
__date__ = 03/30/2024
__version__ = "2.0"
"""

import csv


# function that will display the formatted main menu to the user to show them the program options
def main_menu():
    print("\n", '*' * 75)
    print(''' Please select an option from the menu below
    Main Menu:
    1. Display all Bids
    2. Find Bid
    3. Delete Bid
    4. Display all Bids InOrder
    5. Display all Bids PreOrder
    6. Display all Bids PostOrder
    7. Exit''')
    print('*' * 75, "\n")


# function that will load the csv file
def load_bids(csv_file):
    file = open(csv_file)
    document = csv.reader(file)  # use the csv reader to read the file. BigO = O(n)
    header = []  # hold all the headers of the file in this list
    header = next(document)
    rows = []  # hold all the rows in the file (these are the bids) in this list
    bids = []  # this list will hold the bids individually for easier access

    for row in document:  # for loop to append all the rows from the csv file into a list
        rows.append(row)  # BigO = 0(1)

    for bid in rows:  # for loop to separate each bid with its own information
        bid = Bid(int(bid[1]), bid[0], bid[8], bid[4])  # bid information: id, title, fund, amount
        bids.append(bid)  # add each individual bid to the bids list

    return bids  # the function will return the list of all the bids

    # time complexity for the function above is O(n)


# define the class for the Bids
class Bid:
    def __init__(self, id, title, fund, amount):
        self.id = id  # bid id
        self.title = title  # bid title
        self.fund = fund  # bid fund type
        self.amount = amount  # bid amount total


# define the class for the tree nodes
class Node:
    def __init__(self, bid):
        self.left = None   # the left child
        self.right = None  # the right child
        self.bid = bid     # the bid data stored in the nodes

    #  function that will insert data into a node
    def insert(self, bid):

        if self.bid is None:  # the conditional statement checks if the node is empty first
            self.bid = bid   # if the node is empty, then the data is entered into the node

        else:  # if the node being checked is not empty

            if self.bid.id > bid.id:  # if the id of the new bid is less than the id in the current node
                if self.left is None:  # if there is no child to the left
                    self.left = Node(bid)  # insert the new bid
                else:
                    self.left.insert(bid)  # otherwise, make a recursive call to insert the bid in the left

            elif self.bid.id < bid.id:  # if the id of the new bid is greater than the id in the current node
                if self.right is None:  # if there is no child to the right
                    self.right = Node(bid)  # insert the new bid
                else:
                    self.right.insert(bid)  # otherwise, make a recursive call to insert the bid on the right


# function to format the way bids will be printed
def print_bids(bid):
    print(bid.id, "|", bid.title, "|", bid.fund, "|", bid.amount)


# print the tree in ascending order according to the bid id
def inOrder(current_node):
    if current_node is None:  # checks that the node it is currently on is not empty
        return  # end function by returning if the node is empty
    else:  # else, traverse through the tree
        inOrder(current_node.left)
        print_bids(current_node.bid)
        inOrder(current_node.right)


# print the tree in preorder
def preOrder(current_node):
    if current_node is None:  # checks if current node is not empty
        return
    else:  # else, traverse through the tree
        print_bids(current_node.bid)
        preOrder(current_node.left)
        preOrder(current_node.right)


#  print the tree in postorder
def postOrder(current_node):
    if current_node is None:  # checks if the current node is not empty
        return
    else:  # else, traverse through the tree
        postOrder(current_node.left)
        postOrder(current_node.right)
        print_bids(current_node.bid)

# overall, because each method requires visiting each node
# the time complexity for all traversal methods
# is of O(n)


# function that will load the bids into the tree
def load_tree(bids, root, display_bids):
    for i in bids:
        root.insert(i)  # inserts all the bids into the tree

        if display_bids:  # if display_bids parameter is true,
            print_bids(i)  # print all the bids as they are entered

        else:  # otherwise, continue inserting into the tree without printing
            continue

    # time complexity for inserting the bids can be O(log n) in best case scenario or O(n) in worse case
    # therefore the time complexity is O(n) overall


# function to search for a bid with a given bid id
def search(root):
    current_node = root  # set the root as the first node

    while True:  # initiate while loop

        try:  # exception handling for the input to ensure only an integer is entered
            bid_id = int(input("Please enter the ID of the Bid you are looking for: "))  # convert input to int

            while current_node is not None:  # verify the current node is not empty

                if current_node.bid.id == bid_id:  # if the id's match, print out bid information and return to end the loop
                    print("\nBid found: ")
                    print_bids(current_node.bid)
                    return current_node.bid

                elif current_node.bid.id > bid_id:  # else if current node id is greater, reassign left child as the current node
                    current_node = current_node.left

                else:  # otherwise, reassign the right child as the current node
                    current_node = current_node.right

            print("\nThat Bid does not exist")  # if the tree is traversed and no match was found, the bid does not exist
            return  # return to end the loop when bid does not exist

        except ValueError:  # if the input is anything other than an integer, a value error exception will be thrown
            print("\nPlease enter a Bid id using ONLY numbers\n")  # let the user know their input is not valid

    # time complexity for searching the tree is of O(n) overall due to it being the time complexity for worst case scenario


# function to delete a bid
def delete(current_node, bid_to_delete):

    if current_node is None:  # if the tree is empty, return nothing
        return current_node

    elif current_node is not None:  # if the tree is not empty

        if current_node.bid.id > bid_to_delete:  # if the bid id to delete is less than the current bid id
            current_node.left = delete(current_node.left, bid_to_delete)  # move down the tree to the left and do a recursive call

        elif current_node.bid.id < bid_to_delete:  # if the bid id to delete is greater than the current bid id
            current_node.right = delete(current_node.right, bid_to_delete)  # move down the tree to the right and do a recursive call

        else:  # if the bid id is a match
            if current_node.left is None and current_node.right is None:  # if the node has no children
                del current_node  # delete the node
                print("\nBid", bid_to_delete, " has been deleted")

            elif current_node.left is not None and current_node.right is None:  # if the node has only one child, on the left side
                placeholder = current_node  # set the node data in a place holder variable
                current_node = current_node.left  # reassign the current node as the child on the left
                del placeholder  # then delete the node
                print("\nBid", bid_to_delete, " has been deleted")

            elif current_node.left is None and current_node.right is not None:  # if the node has only one child, on the right side
                placeholder = current_node  # set the node data in a place holder variable
                current_node = current_node.left  # reassign the current node as the child on the right
                del placeholder  # then delete the node
                print("\nBid", bid_to_delete, " has been deleted")

            else:  # if the node has two children
                successor = current_node.right
                while successor.left is None:
                    successor = successor.left  # move the node down the tree
                current_node.bid = successor.bid
                current_node.right = delete(current_node.right, bid_to_delete)  # delete the node when it's at the bottom of the tree

        return current_node

    else:  # else, the tree is not empty but the bid does not exist, return and end function
        return

    #  worst case scenario for delete would take O(n) time therefore the time complexity overall would be O(n)


# main function
# --------------------------------------------------------------------------
# In the main function, there are no new functions created, instead, it calls on any
# functions it needs that were declared and defined in the program above.
# The program uses these numerous functions to increase efficiency by making as much reusable code as possible.
# This helps ensure the main function is not overloaded and that the program can read any CSV file
# as long as it follows the basic template as the one used for this example. Error handling and input validation
# are also used throughout as well as fair-good time complexity sorting algorithms to ensure the best possible
# run time.
# -----------------------------------------------------------------------------------

def main():
    bids = load_bids('eBid_Monthly_Sales_Dec_2016.csv')  # open the csv file that contains the bids
    root = Node(bids[0])  # declare the first bid as the root of the tree
    load_tree(bids, root, False)  # load all the bids into the tree

    # initiate while loop that will continue until user inputs '7'
    while True:
        main_menu()  # display the menu options to the user
        match input(">> "):  # ask for user input for the match case statement

            case '1':  # case 1 displays the bids in the order they are added
                print("Displaying Bids...\n")
                load_tree(bids, root, True)

            case '2':  # case 2 searches and returns bid information if it exists
                search(root)

            case '3':  # case 3 searches for and deletes bid if the bid exists
                bid_to_delete = search(root)

                if bid_to_delete is not None:
                    delete(root, bid_to_delete.id)
                else:
                    continue

            case '4':  # case 4 displays all the bids inOrder
                print("Displaying Bids InOrder...\n")
                inOrder(root)
            case '5':  # case 5 displays all the bids preOrder
                print("Displaying Bids PreOrder...\n")
                preOrder(root)

            case '6':  # case 6 displays all the bids postOrder
                print("Displaying Bids PostOrder...\n")
                postOrder(root)

            case '7':  # case 7 exits the loop and the program
                print('Goodbye!')
                exit()

            case default:  # any other input is invalid
                print("Please select a valid option")

# the time complexity of the program overall in the worst case scenario is of liner time O(n).
# the time complexity of the program overall in the best case scenario would be of O(log n)


# call main function
if __name__ == '__main__':
    main()

