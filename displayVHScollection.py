__author__ = "Jason"
# DONE
import sqlite3
# Import sqlite3 for database


def display_vhs_collection():

    while True:
        try:
            vhs_database = "VHSDatabase.db"
            # Get VHS database

            current_conn = sqlite3.connect(vhs_database)
            cur_cur = current_conn.cursor()
            print("\n//VHS Database connected//\n")
            # Connect to VHS database

            cur_cur.execute("SELECT * FROM VHS_TAPES")
            # Query to display VHS database

        except sqlite3.OperationalError:
            print("\n//ERROR//:VHS Database needs to be created//")
            break
            # Check for valid database

        else:
            for row in cur_cur:
                print("\nUPC = ", row[0])
                print("TITLE = ", row[1])
                print("GENRE = ", row[2])
                print("PRICE_PAID = ", row[3])
                print("PRICE_WORTH = ", row[4])
                print("NOTES = ", row[5])
                print("RENTALS = ", row[6], "\n")
                # Display each VHS_TITLE in VHS database

            current_conn.commit()
            current_conn.close()
            break
            # Commit changes to VHS database and close

