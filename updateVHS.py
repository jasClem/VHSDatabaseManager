__author__ = "Jason"
# DONE
import sqlite3


# Import sqlite3 for database


def update_vhs():
    vhs_database = "VHSDatabase.db"
    # Create variable for VHS database

    cur_con = sqlite3.connect(vhs_database)
    cur_cur = cur_con.cursor()
    print("\n//VHS Database connected//\n")
    # Create connection to VHS database

    vhs_queries = {"vhs_title_q": "UPDATE VHS_TAPES SET TITLE = ? WHERE UPC = ?",
                   "vhs_genre_q": "UPDATE VHS_TAPES SET GENRE = ? WHERE UPC = ?",
                   "vhs_p_p_q": "UPDATE VHS_TAPES SET PRICE_PAID = ? WHERE UPC = ?",
                   "vhs_p_w_q": "UPDATE VHS_TAPES SET PRICE_WORTH = ? WHERE UPC = ?",
                   "vhs_notes_q": "UPDATE VHS_TAPES SET NOTES = ? WHERE UPC = ?",
                   "vhs_rentals_q": "UPDATE VHS_TAPES SET RENTALS = ? WHERE UPC = ?"}
    # Create variables for queries

    while True:
        try:

            while True:
                try:
                    vhs_id = int(input("\nEnter UPC of the VHS to update: "))
                    # Get user input for VHS UPC number

                except ValueError:
                    print("\n//ERROR//:VHS UPC must be a valid integer//")
                    # Check for valid UPC number
                else:
                    break

            while True:
                try:
                    print(" ------------------------ \n"
                          "|//// UPDATE OPTIONS ////|\n"
                          "|------------------------|\n"
                          "| 1 - Rename VHS         |\n"
                          "| 2 - Change VHS Genre   |\n"
                          "| 3 - Update Price Paid  |\n"
                          "| 4 - Update Price Worth |\n"
                          "| 5 - Edit VHS Notes     |\n"
                          "| 6 - Update VHS Rentals |\n"
                          " ------------------------ ")
                    # Display menu

                    menu_choice = int(input("\nWhich function would you like to use? (1-6): "))
                    # Get user input for menu choice

                except ValueError:
                    print("\n//ERROR//:Please choose a valid number (1-6)//")
                else:
                    if menu_choice < 1 or menu_choice > 6:
                        print("\n//ERROR//:Please choose a valid number (1-6)//")
                        # Check for valid menu choice option

                    else:
                        if menu_choice == 1:
                            do_what = vhs_queries["vhs_title_q"]
                            # Menu option 1 - VHS title edit

                            while True:
                                vhs_update = str(input("\nEnter new VHS Title: "))
                                # Get user input for new title

                                if vhs_update == "":
                                    print("\n//ERROR//:VHS Title cannot be blank//")
                                    # Check for blank VHS title

                                else:
                                    break

                        elif menu_choice == 2:
                            do_what = vhs_queries["vhs_genre_q"]
                            # Menu option 2 - VHS genre edit

                            vhs_update = str(input("\nEnter new VHS Genre: "))
                            break
                            # Get user input for VHS genre

                        elif menu_choice == 3:
                            do_what = vhs_queries["vhs_p_p_q"]
                            # Menu option 3 = update VHS price paid

                            while True:
                                try:
                                    vhs_update = float(input("\nUpdate the price paid: $"))
                                    # Get user input for price paid

                                except ValueError:
                                    print("\n//ERROR//:Price paid must be dollar value or zero//")
                                    # Check for valid price paid

                                else:
                                    vhs_update = (round(vhs_update, 2))
                                    break
                                    # Round Price to 2 decimal places

                        elif menu_choice == 4:
                            do_what = vhs_queries["vhs_p_w_q"]
                            # Menu option 4 - update VHS price worth

                            while True:
                                try:
                                    vhs_update = float(input("\nUpdate the price worth: $"))
                                    # Get user input for price worth

                                except ValueError:
                                    print("\n//ERROR//:Price worth must be dollar value or zero//")
                                    # Check for valid price worth

                                else:
                                    vhs_update = (round(vhs_update, 2))
                                    break
                                    # Round price to 2 decimal places

                        elif menu_choice == 5:
                            do_what = vhs_queries["vhs_notes_q"]
                            # Menu option 5 - notes

                            vhs_update = str(input("\nEnter any notes or leave blank: "))
                            break
                            # Get user input for notes

                        elif menu_choice == 6:
                            do_what = vhs_queries["vhs_rentals_q"]
                            # Menu option 6 - update VHS rentals

                            while True:
                                try:
                                    vhs_update = int(input("\nEnter number of rentals: "))

                                except ValueError:
                                    print("\n//ERROR//:Rentals must be an integer or zero)//")
                                    # Check for valid rental number

                                else:
                                    break
                        break

            do_how = (vhs_update, vhs_id)
            # Variables for updated database entries

            cur_cur.execute(do_what,do_how)
            # Enter updated variables into database

        except sqlite3.OperationalError:
            print("\n//ERROR//:VHS table does not exist, please create//")
            break
            # Check for VHS_TAPES table

        else:
            cur_con.commit()
            cur_con.close()
            print("\n//Updates added to database//\n")
            break
            # Commit changes to VHS database and close

