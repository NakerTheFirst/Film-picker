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

# TODO: Go through git course, find out why you're committing to master even though main is the default one

def main():

    movies = []
    close = False

    menu = "1. Generate a film \n2. See the watchlist \n3. Add a film to the watchlist \n" \
           "4. Delete a film from the watchlist \n5. Exit\n"

    while not close:

        print(menu)

        action = int(input("What action do you want to take? "))

        match action:
            case 1:
                print(action)
            case 2:
                print(action)
            case 3:
                print(action)
            case 4:
                print(action)
            case 5:     # Quitting case
                close = True
                print("Goodbye!")

    return 0


if __name__ == '__main__':
    main()
