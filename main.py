"""
The goal of the programme is to store films to watch (watchlist) and to generate a watch proposal
The user can type in a name of films from watchlist and the programme saves it
The programme will remember the data input during the last runtime after rerunning
The programme stores the film data in a .txt file locally (and possibly on a web based server in the future)

Base the program on OOP

Additionally, besides films being divided into typical film categories,
they also have medium/high energy absorption category.
"""
import random
import time
from os.path import exists


# Picks a random item from a list
def pick_item(item, lst):
    pass


def check_if_exists(file):
    if exists(file):
        return True

    if not exists(file):
        print("Nothing to show")
        return False


# Prints contents of a file
def view_items(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        if content == "":
            print("\nThe list is empty")
        if content != "":
            print(content)


# Append an item to file contents
def add_item(item, lst):
    # Create file if it doesn't exist already
    if not exists("films.txt"):
        f = open("films.txt", "a")


# Delete an item from file contents
def del_item(item, lst):
    pass


def main():
    close = False
    films_file = "films.txt"

    menu = "\n1. Pick a film to watch \n2. View the watchlist \n3. Add a film to the watchlist \n" \
           "4. Delete a film from the watchlist \n5. Exit"

    while not close:
        print(menu)
        action = int(input("\nWhat action do you want to take? "))

        match action:
            case 1:
                print(action)
            case 2:
                view_items(films_file)
            case 3:
                print(action)
            case 4:
                print(action)
            case 5:
                close = True
                print("Goodbye!")

        # time.sleep(1.5)
    return 0


if __name__ == '__main__':
    main()
