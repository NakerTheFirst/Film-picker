# Films have medium/high energy absorption category which impact the pseudorandom picking process

from os.path import exists
import random
import time
import Item
import Film


def main():

    close = False
    films_file = "films.txt"

    menu = "\n1. Pick a film to watch \n2. View the watchlist \n3. Add a film to the watchlist \n" \
           "4. Delete a film from the watchlist \n5. Exit"

    while not close:
        print(menu)
        action = int(input("\nWhat action do you want to take? "))
        print()

        match action:
            case 1:
                print(action)
            case 2:
                print("File contents")
            case 3:
                print(action)
            case 4:
                print(action)
            case 5:
                close = True
                print("Goodbye!")

        if not close:
            input("\nPress enter to continue...")

    return 0


if __name__ == '__main__':
    main()
