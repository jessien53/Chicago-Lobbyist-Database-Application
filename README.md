# Chicago Lobbyist Database Application

This project is a **console-based application** that interacts with a database of Chicago lobbyists. It allows users to retrieve, display, and modify information about lobbyists, their clients, and employers. The app offers five main operations, each providing insight into the lobbyist data, with all results displayed in the console.

## Features

- Search for lobbyists by name (supports wildcards).
- View detailed information about individual lobbyists by ID.
- Display the top N lobbyists based on total compensation for a specific year.
- Register a lobbyist for a new year.
- Update the salutation for a specific lobbyist.

## Technologies Used

- **Python 3**
- **SQLite3** for database management
- Custom Python modules:
  - `objecttier.py`: Handles interactions between the console and the database.
  - `datatier.py`: Provides lower-level SQL execution support, including select and action queries.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jessien53/Chicago-Lobbyist-Database-Application.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Chicago-Lobbyist-Database-Application
    ```

3. **Ensure Python 3 is installed**. You can check the version with:
    ```bash
    python --version
    ```

4. **Install required dependencies** (if any). For example, if the project uses external libraries:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: If no external dependencies exist, this step can be omitted.)

5. **Setup the database**:
    Ensure the `Chicago_Lobbyists.db` SQLite database is placed in the root directory of the project.

## Usage

To run the application, execute the following command from the project directory:

```bash
python main.py
```

Upon launching the app, you'll be presented with a menu that allows you to perform various operations related to lobbyists. Each command corresponds to a specific functionality:

1. **Search for lobbyists** by name (supports wildcards `_` and `%`).
2. **Retrieve detailed information** about a lobbyist by ID.
3. **Display the top N lobbyists** based on compensation for a given year.
4. **Register a lobbyist for a new year.
5. **Set or update a lobbyist’s salutation**.

Type `'x'` at any time to exit the application.

### Example

```plaintext
** Welcome to the Chicago Lobbyist Database Application **

General Statistics:
  Number of Lobbyists: 1,254
  Number of Employers: 230
  Number of Clients: 875

Please enter a command (1-5, x to exit): 1

Enter lobbyist name (first or last, wildcards _ and % supported): Smith

Number of lobbyists found: 2

1001 : John Smith Phone: 312-555-1234
1002 : Jane Smith Phone: 312-555-5678
```

## File Structure

```
├── Chicago_Lobbyists.db   # SQLite database file
├── main.py                # Main program with the application loop
├── objecttier.py          # Module for higher-level database interactions
├── datatier.py            # Module for lower-level SQL execution
├── README.md              # This file
```

---

## Author

Jessie Nouna  
*Project maintained by Jessie Nouna.*
