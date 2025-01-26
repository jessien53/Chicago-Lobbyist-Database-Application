#
# main
#
# This is a console-based application that interacts with a database
# of Chicago lobbyists. The user can choose from 5 operations,
# each providing information about lobbyists or modifying the database.
# Results are displayed in the console.
#
# Author: Jessie Nouna
#
import sqlite3
from objecttier import (get_lobbyists, get_lobbyist_details, get_top_N_lobbyists,
                        num_lobbyists, num_clients, num_employers, add_lobbyist_year,
                        set_salutation)


##################################################################
#
# command1:
#
# Prompts the user to input a lobbyist's name (first or last, with optional
# wildcards). Searches for matching lobbyists in the database and prints
# the number of lobbyists found and their basic details.
# If more than 100 lobbyists are found, the user is asked to narrow the search.
#
# Returns: None
#
def command1():
    # prompt user for lobbyist's name, allowing for sql wildcards
    name = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ")
    # fetch matching lobbyists from the database based on the input
    lob_list = get_lobbyists(dbConn, name)
    # print the number of lobbyists found and if there are more than 100 lobbyists found,
    # ask user to narrow search
    print("\nNumber of lobbyists found: ", len(lob_list), "\n")
    if len(lob_list) > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...")
    else:
        # otherwise, print each lobbyist's basic information
        for lobbyist in lob_list:
            print(
                f"{lobbyist.Lobbyist_ID} : {lobbyist.First_Name} {lobbyist.Last_Name} Phone: {lobbyist.Phone}")


##################################################################
#
# command2:
#
# Prompts the user to input a lobbyist's ID. Searches the database for the
# detailed information of the lobbyist with the given ID and prints these details.
# If the lobbyist is not found, an error message is printed.
#
# Returns: None
#
def command2():
    # prompt user for the lobbyist's ID
    lob_id = input("\nEnter Lobbyist ID: ")
    # fetch detailed lobbyist information based on the provided ID
    lobbyist = get_lobbyist_details(dbConn, lob_id)
    # if no lobbyist is found, print error message
    if lobbyist is None:
        print("\nNo lobbyist with that ID was found.")
    else:
        # otherwise, print the detailed information about the lobbyist found
        print(f"\n{lob_id} :")
        print(f"  Full Name: {lobbyist.Salutation} {lobbyist.First_Name} {lobbyist.Middle_Initial} "
              f"{lobbyist.Last_Name} {lobbyist.Suffix}")
        print(f"  Address: {lobbyist.Address_1} {lobbyist.Address_2} , {lobbyist.City} , "
              f"{lobbyist.State_Initial} {lobbyist.Zip_Code} {lobbyist.Country}")
        print(f"  Email: {lobbyist.Email}")
        print(f"  Phone: {lobbyist.Phone}")
        print(f"  Fax: {lobbyist.Fax}")
        print("  Years Registered: ", end="")
        for year in lobbyist.Years_Registered: print(f"{year}, ", end="")
        print("\n  Employers: ", end="")
        for employer in lobbyist.Employers: print(f"{employer}, ", end="")
        print(f"\n  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")


##################################################################
#
# command3:
#
# Prompts the user for a year and a number (N). Retrieves the top N lobbyists
# based on total compensation for the given year and prints their details.
# If N is less than 1, an error message is printed.
#
# Returns: None
#
def command3():
    # prompt user for the numer of top lobbyists to display
    N = int(input("\nEnter the value of N: "))
    if N < 1:  # ensure the value is positive
        print("Please enter a positive value for N...")
    else:
        # prompt user for year and fetch top lobbyists for that year
        year = input("Enter the year: ")
        lob_list = get_top_N_lobbyists(dbConn, N, year)
        # print the details of the top N lobbyists
        num = 0
        for lobbyist in lob_list:
            num += 1
            print(f"\n{num} . {lobbyist.First_Name} {lobbyist.Last_Name}")
            print(f"  Phone: {lobbyist.Phone}")
            print(f"  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")
            print(f"  Clients: ", end="")
            for client in lobbyist.Clients: print(f"{client}, ", end="")


##################################################################
#
# command4:
#
# Prompts the user for a lobbyist's ID and a year. Attempts to register the lobbyist
# for the given year in the database. Prints whether the registration was successful.
#
# Returns: None
#
def command4():
    # prompt user for lobbyist ID and year to register
    year = input("\nEnter year: ")
    lob_id = input("Enter the lobbyist ID: ")
    # attempt to register the lobbyist for the specified year
    success = add_lobbyist_year(dbConn, lob_id, year)
    # print a success or failure message based on the result
    if success == 1:
        print("\nLobbyist successfully registered.")
    else:
        print("\nNo Lobbyist with that ID was found.")


##################################################################
#
# command5:
#
# Prompts the user for a lobbyist's ID and a salutation. Attempts to set the salutation
# for the lobbyist in the database. Prints whether the salutation was successfully updated.
#
# Returns: None
#
def command5():
    # prompt user for lobbyist ID and new salutation
    lob_id = input("\nEnter the lobbyist ID: ")
    sal = input("Enter the salutation: ")
    # attempt to update the salutation for the given lobbyist
    success = set_salutation(dbConn, lob_id, sal)
    # print a success or failure message based on result
    if success == 1:
        print("\nSalutation successfully set.")
    else:
        print("\nNo lobbyist with that ID was found.")


##################################################################
#
# main
#

# connect to the Chicago Lobbyists database
dbConn = sqlite3.connect("Chicago_Lobbyists.db")

# print welcome message and display general statistics about the database
print('** Welcome to the Chicago Lobbyist Database Application **')
print("\nGeneral Statistics:")
print(f"  Number of Lobbyists: {num_lobbyists(dbConn):,}")
print(f"  Number of Employers: {num_employers(dbConn):,}")
print(f"  Number of Clients: {num_clients(dbConn):,}")

command = ''
# continuously prompt the user for a command until 'x' is entered to exit
while command != 'x':
    command = input("\nPlease enter a command (1-5, x to exit): ")

    # execute the corresponding command based on user input
    if command == '1':
        # find and print basic information for lobbyists based on the user's input
        command1()
    elif command == '2':
        # retrieve and print detailed information for a lobbyist by their ID
        command2()
    elif command == '3':
        # display the top N lobbyists based on total compensation for a given year
        command3()
    elif command == '4':
        # register a lobbyist for a new year
        command4()
    elif command == '5':
        # set the salutation of a lobbyist
        command5()
    else:
        # handle unrecognized commands, except for 'x' which exits the loop
        if command != 'x': print("**Error, unknown command, try again...")

#
# done
#
