__author__ = 'Jason'
# DONE
import sqlite3
# Import sqlite3 for database


def create_vhs_database():

        cur_con = sqlite3.connect('VHSDatabase.db')
        print("\n//VHS Database connected//\n")
        # Open/create VHS database

        while True:
                try:
                    cur_con.execute("CREATE TABLE VHS_TAPES \
                    (UPC INTEGER PRIMARY KEY NOT NULL, \
                    TITLE TEXT NOT NULL, \
                    GENRE TEXT, \
                    PRICE_PAID INT, \
                    PRICE_WORTH REAL NOT NULL, \
                    NOTES CHAR(50), \
                    RENTALS INT);")
                    # Create VHS_TAPES table

                except sqlite3.OperationalError:
                        print("\n//ERROR//:VHS Table already exists//")
                        # Check for preexisting VHS_TAPES table

                else:
                    cur_con.close()
                    print("//VHS Table created//\n")
                    # Close VHS database

                break


