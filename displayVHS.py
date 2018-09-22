__author__ = "Jason"
# DONE
import sqlite3
# Import sqlite3 for database


def display_vhs():
    while True:
        try:
            vhs_database = "VHSDatabase.db"
            # Create variable for VHS database

            while True:
                try:
                    vhs_upc = int(input("\nEnter the UPC of the VHS to view: "))
                    # Get user input for VHS UPC number

                except ValueError:
                    print("\n//ERROR//:VHS UPC must be a valid integer//")
                    # Check for valid UPC number
                else:
                    break

            cur_con = sqlite3.connect(vhs_database)
            cur_cur = cur_con.cursor()
            print("\n//VHS Database connected//\n")
            # Create connection to VHS database

            do_what = "SELECT * FROM PRODUCTS WHERE UPC = ?"
            do_how = (vhs_upc,)
            # Variables for VHS database entries

            cur_cur.execute(do_what, do_how)
            # Query to display VHS

        except sqlite3.OperationalError:
            print("\n//ERROR//:VHS table does not exist, please create//")
            break
            # Check for VHS_TAPES table

        else:
            for row in cur_cur:
                print("\nUPC = ", row[0])
                print("TITLE = ", row[1])
                print("GENRE = ", row[2])
                print("PRICE_PAID = ", row[3])
                print("PRICE_WORTH = ", row[4])
                print("NOTES = ", row[5])
                print("RENTALS = ", row[6], "\n")
                # Display all rows for current VHS

            cur_con.commit()
            cur_con.close()
            break
            # Commit changes to VHS database and close
