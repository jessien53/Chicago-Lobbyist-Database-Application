#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
# Edited by: Jessie Nouna
#
from datatier import select_one_row, select_n_rows, perform_action


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    def __init__(self, lobbyist_id, first_name, last_name, phone):
        self._id = lobbyist_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone

    @property
    def Lobbyist_ID(self):
        return self._id

    @property
    def First_Name(self):
        return self._first_name

    @property
    def Last_Name(self):
        return self._last_name

    @property
    def Phone(self):
        return self._phone


##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, lobbyist_id, salutation, first_name, middle_initial,
                 last_name, suffix, address_1, address_2, city, state_initial,
                 zip_code, country, email, phone, fax, years_registered,
                 employers, total_compensation):
        self._lobbyist_id = lobbyist_id
        self._salutation = salutation
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._suffix = suffix
        self._address_1 = address_1
        self._address_2 = address_2
        self._city = city
        self._state_initial = state_initial
        self._zip_code = zip_code
        self._country = country
        self._email = email
        self._phone = phone
        self._fax = fax
        self._years_registered = years_registered
        self._employers = employers
        self._total_compensation = total_compensation

    @property
    def Lobbyist_ID(self):
        return self._lobbyist_id

    @property
    def Salutation(self):
        return self._salutation

    @property
    def First_Name(self):
        return self._first_name

    @property
    def Middle_Initial(self):
        return self._middle_initial

    @property
    def Last_Name(self):
        return self._last_name

    @property
    def Suffix(self):
        return self._suffix

    @property
    def Address_1(self):
        return self._address_1

    @property
    def Address_2(self):
        return self._address_2

    @property
    def City(self):
        return self._city

    @property
    def State_Initial(self):
        return self._state_initial

    @property
    def Zip_Code(self):
        return self._zip_code

    @property
    def Country(self):
        return self._country

    @property
    def Email(self):
        return self._email

    @property
    def Phone(self):
        return self._phone

    @property
    def Fax(self):
        return self._fax

    @property
    def Years_Registered(self):
        return self._years_registered

    @property
    def Employers(self):
        return self._employers

    @property
    def Total_Compensation(self):
        return self._total_compensation


##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(self, lobbyist_id, first_name, last_name, phone,
                 total_compensation, clients):
        self._lobbyist_id = lobbyist_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._total_compensation = total_compensation
        self._clients = clients

    @property
    def Lobbyist_ID(self):
        return self._lobbyist_id

    @property
    def First_Name(self):
        return self._first_name

    @property
    def Last_Name(self):
        return self._last_name

    @property
    def Phone(self):
        return self._phone

    @property
    def Total_Compensation(self):
        return self._total_compensation

    @property
    def Clients(self):
        return self._clients


##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    # define and execute sql query to get number of lobbyists in database
    sql = "select count(*) from LobbyistInfo"
    result = select_one_row(dbConn, sql)
    # if execution fails, return -1, otherwise return result
    if result is None:
        return -1
    else:
        return int(result[0])


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    # define and execute sql query to get number of employers in database
    sql = "select count(*) from EmployerInfo"
    result = select_one_row(dbConn, sql)
    # if execution fails, return -1, otherwise return result
    if result is None:
        return -1
    else:
        return int(result[0])


##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    # define and execute sql query to get number of clients in database
    sql = "select count(*) from ClientInfo"
    result = select_one_row(dbConn, sql)
    # if execution fails, return -1, otherwise return result
    if result is None:
        return -1
    else:
        return int(result[0])


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    # define and execute sql query to get list of lobbyists matching the given pattern
    sql = """ select Lobbyist_ID, First_Name, Last_Name, Phone
    from LobbyistInfo
    where First_Name like ? or Last_Name like ?
    order by Lobbyist_ID asc
    """
    results = select_n_rows(dbConn, sql, (pattern, pattern,))
    # create list of lobbyists from thr table produced
    lobbyists = []
    if results:
        for row in results:
            lobbyists.append(Lobbyist(row[0], row[1], row[2], row[3]))

    # return the list of lobbyists (empty list if no data was retrieved
    return lobbyists


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    # define and execute an sql query for lobbyist info
    lobbyist_sql = "select * from LobbyistInfo where Lobbyist_ID = ?"
    lobbyist_result = select_one_row(dbConn, lobbyist_sql, (lobbyist_id,))

    # if no lobbyist was found, return None
    if lobbyist_result == () or lobbyist_result is None:
        return None

    # create list of years
    years_sql = "select Year from LobbyistYears where Lobbyist_ID = ?"
    years_result = select_n_rows(dbConn, years_sql, (lobbyist_id,))
    years = []
    for year in years_result:
        years.append(year[0])
    # create list of employer names
    employers_sql = """select distinct Employer_Name from EmployerInfo
    join LobbyistAndEmployer on EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
    where Lobbyist_ID = ?
    order by Employer_Name asc
    """
    employers_result = select_n_rows(dbConn, employers_sql, (lobbyist_id,))
    employers = []
    for employer in employers_result:
        employers.append(employer[0])

    # find total compensation for lobbyist
    comp_sql = """select sum(Compensation_Amount) from Compensation 
    join LobbyistInfo on Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
    where Compensation.Lobbyist_ID = ?
    """
    comp_result = select_one_row(dbConn, comp_sql, (lobbyist_id,))
    if comp_result[0] is None:
        comp = 0
    else:
        comp = comp_result[0]

    # return LobbyistDetails object with all the information
    return LobbyistDetails(lobbyist_result[0], lobbyist_result[1], lobbyist_result[2], lobbyist_result[3],
                           lobbyist_result[4], lobbyist_result[5], lobbyist_result[6], lobbyist_result[7],
                           lobbyist_result[8], lobbyist_result[9], lobbyist_result[10], lobbyist_result[11],
                           lobbyist_result[12], lobbyist_result[13], lobbyist_result[14], years, employers,
                           comp)


##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    # sql query to get the top N lobbyists with their total compensation
    sql = """ select Compensation.Lobbyist_ID, First_Name, Last_Name, Phone, sum(Compensation_Amount) as Total_Compensation
    from Compensation join LobbyistInfo on LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
    where strftime('%Y',Period_End) = ?
    group by Compensation.Lobbyist_ID
    order by Total_Compensation desc
    limit ?
    """
    results = select_n_rows(dbConn, sql, (year, N,))

    # create list of LobbyistClients if data was found
    lobbyistClients = []
    if results != ():
        for row in results:
            # create list of clients for each lobbyist
            curClients = []
            clients_sql = """select distinct Compensation.Client_ID, Client_Name from ClientInfo
            join Compensation on ClientInfo.Client_ID = Compensation.Client_ID
            where Lobbyist_ID = ? and strftime('%Y',Period_End) = ?
            order by Client_Name asc
            """
            clients = select_n_rows(dbConn, clients_sql, (row[0], year,))
            for client in clients:
                curClients.append(client[1])  # append client IDs to curClients
            # append the LobbyistClients object with the current clients
            lobbyistClients.append(LobbyistClients(row[0], row[1], row[2], row[3], row[4], curClients))

    return lobbyistClients


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    # check if the lobbyist exists
    sql_check = "select count(*) from LobbyistInfo where Lobbyist_ID = ?"
    result = select_one_row(dbConn, sql_check, (lobbyist_id,))

    if result is None or result[0] == 0:
        # lobbyist doesn't exist or an error occurred
        return 0

    # insert the year into the database for the lobbyist
    sql_insert = "insert into LobbyistYears (Lobbyist_ID, Year) values (?, ?)"
    # execute the insertion (assuming execute_query handles the insertion)
    execution = perform_action(dbConn, sql_insert, (lobbyist_id, year))
    if execution == -1:
        return 0  # execution fail
    else:
        return 1  # execution success


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    # check if the lobbyist exists
    sql_check = "select count(*) from LobbyistInfo where Lobbyist_ID = ?"
    result = select_one_row(dbConn, sql_check, (lobbyist_id,))

    if result is None or result[0] == 0:
        # lobbyist doesn't exist or an error occurred
        return 0

    # insert the year into the database for the lobbyist
    sql_insert = "update LobbyistInfo set Salutation = ? where Lobbyist_ID = ?"
    # execute the insertion (assuming execute_query handles the insertion)
    execution = perform_action(dbConn, sql_insert, (salutation, lobbyist_id))
    if execution == -1:
        return 0  # execution fail
    else:
        return 1  # execution success
