__author__ = "Jason"
# DONE
import sqlite3
# Import sqlite3 for database


def add_vhs():

    vhs_database = "VHSDatabase.db"
    # Create variable for VHS database

    cur_con = sqlite3.connect(vhs_database)
    cur_cur = cur_con.cursor()
    print("\n//VHS Database connected//\n")
    # Create connection to VHS database

    while True:
        try:
            while True:
                vhs_title = str(input("\nEnter VHS Title: "))
                # Get user input for title of VHS

                if vhs_title == "":
                    print("\n//ERROR//:VHS Title cannot be blank//")
                    # Check for blank VHS title

                else:
                    break

            vhs_genre = str(input("\nEnter the VHS Genre for " + vhs_title + ": "))
            # Get user input for VHS genre

            while True:
                try:
                    price_paid = float(input("\nEnter the Price Paid for " + vhs_title + ": $"))
                    # Get user input for price paid

                except ValueError:
                    print("\n//ERROR//:Price Paid must be dollar value or zero//")
                    # Check for valid Price Paid

                else:
                    price_paid = (round(price_paid, 2))
                    break
                    # Round Price Paid to 2 decimal places

            while True:
                try:
                    price_worth = float(input("\nEnter the Price Worth for " + vhs_title + ": $"))
                    # Get user input for price worth

                except ValueError:
                    print("\n//ERROR//:Price Worth must be dollar value or zero//")
                    # Check for valid Price Worth

                else:
                    price_worth = (round(price_worth, 2))
                    break
                    # Round Price Worth to 2 decimal places

            notes = str(input("\nEnter any notes for " + vhs_title + " (or leave blank): "))
            # Get user input for notes

            while True:
                try:
                    rentals = int(input("\nEnter the amount of " + vhs_title + " rentals: "))
                    # Get user input for number of rentals

                except ValueError:
                    print("\n//ERROR//:Rentals must be an integer or zero)//")
                    # Check for valid rental number

                else:
                    break

            do_what = "INSERT INTO VHS_TAPES (TITLE, GENRE, PRICE_PAID, PRICE_WORTH, NOTES, RENTALS) \
                         VALUES (?, ?, ?, ?, ?, ?)"
            do_how = (vhs_title, vhs_genre, price_paid, price_worth, notes, rentals)
            # Variables for VHS database entries

            cur_cur.execute(do_what, do_how)
            # Enter variables into VHS database

        except sqlite3.OperationalError:
            print("\n//ERROR//:VHS table does not exist, please create//")
            break
            # Check for VHS_TAPES table

        else:
            cur_con.commit()
            cur_con.close()
            print("\n//" + vhs_title + " added to database//\n")
            break
            # Commit changes to VHS database and close






