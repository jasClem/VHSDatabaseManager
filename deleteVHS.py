__author__ = "Jason"
# DONE
import sqlite3
# Import sqlite3 for database


def delete_vhs():

    vhs_database = "VHSDatabase.db"
    # Get VHS database

    while True:
        try:
            while True:
                try:
                    vhs_upc = int(input("\nEnter UPC of the VHS to delete: "))
                    # Get user input for VHS UPC number

                except ValueError:
                    print("\n//ERROR//:VHS UPC must be a valid integer//")
                    # Check for valid UPC number

                else:
                    cur_con = sqlite3.connect(vhs_database)
                    cur_cur = cur_con.cursor()
                    print("\n//VHS Database connected//\n")
                    # Connect to VHS database

                    do_what = "DELETE FROM PRODUCTS WHERE UPC = ?"
                    do_how = (vhs_upc,)
                    # Variables for VHS database entries

                    cur_cur.execute(do_what, do_how)
                    break
                    # Enter variables into VHS database

        except sqlite3.OperationalError:
            print("\n//ERROR//:VHS table does not exist, please create//")
            break
            # Check for VHS_TAPES table

        else:
            cur_con.commit()
            cur_con.close()
            print("//VHS UPC:" + vhs_upc + " deleted//\n")
            break
            # Commit changes to VHS database and close
