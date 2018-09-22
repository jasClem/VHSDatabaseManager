__author__ = 'Jason'
# DONE
from addVHS import *
from createVHSdatabase import *
from deleteVHS import *
from displayVHScollection import *
from displayVHS import *
from updateVHS import *
# Import functions


def main():

    while True:
        print(" ------------------------------    _________________________________________\n"
              "|/////// VHS Database /////////|  | ___________________^___________________ |\n"
              "|///////   Manager    /////////|  |/                                       \|\n"
              "|------------------------------|  |   ______   _________________   ______   |\n"
              "| 1 - Create VHS Database      |  |  /  ####| || ------------- || |##    \  |\n"
              "| 2 - Add a VHS to Database    |  | |  ####/| || ------------- || |\##    | |\n"
              "| 3 - Update a VHS             |  | | ####| | || ----V/H/S---- || | |##   | |\n"
              "| 4 - Delete a VHS             |  | | ####| | || ------------- || | |##   | |\n"
              "| 5 - Display VHS collection   |  | |  ####\| || ------------- || |/##    | |\n"
              "| 6 - Display a VHS            |  |  \__####| ||_______________|| |##____/  |\n"
              "| 7 - Quit                     |  |                                         |\n"
              " ------------------------------   |_________________________________________|")
        # Display menu

        while True:
            try:
                menu_choice = int(input("Which function would you like to use? (1-7): "))
                # Get user input for menu choice

            except ValueError:
                print("\n//ERROR//:Please choose a valid number (1-7)//")
            else:
                if menu_choice < 1 or menu_choice > 7:
                    print("\n//ERROR//:Please choose a valid number (1-7)//")
                else:
                    break
                    # Check for valid menu choice option

        if menu_choice == 1:
            create_vhs_database()
            # Menu option 1 - create database

        elif menu_choice == 2:
            add_vhs()
            # Menu option 2 - add VHS to database

        elif menu_choice == 3:
            update_vhs()
            # Menu option 3 - update VHS in database

        elif menu_choice == 4:
            delete_vhs()
            # Menu option 4 - delete VHS from database

        elif menu_choice == 5:
            display_vhs_collection()
            # Menu option 5 - display all VHS in database

        elif menu_choice == 6:
            display_vhs()
            # Menu option 6 - display single VHS from database

        elif menu_choice == 7:
            break
            # Menu option 7 - Quit program


main()
