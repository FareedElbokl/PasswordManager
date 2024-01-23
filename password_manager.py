from database import connect_db

def print_existing_websites():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT website FROM passwords')
    websites = cursor.fetchall() #cursor.fetchall() will take all the rows displayed from the previous query and place them in a list as tuples containing a single element, the website.
    if not websites: #if empty list, means no existing websites
        print("\nNo existing websites.\n")
    else:
        print("\nList of websites: \n")
        for website in websites:
            print(website[0])  #'website' points to a tuple, and website[0] is the first elem in the tuple, which is the website.
        print() 


def clear_table():
    conn = connect_db() #'conn' is the connection object to the sql database
    cursor = conn.cursor() #conn.cursor() creates and returns a cursor object, the cursor is used to write sql commands for our specific table
    cursor.execute('DELETE FROM passwords') #this deletes all rows in the table
    conn.commit() #commits the changes to the sql database
    conn.close() #closes the connection after committing the changes

def website_exists(website):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM passwords WHERE website = ?', (website,)) #this query will count the number of records in the passwords table, the ? is a placeholder, which is provided in the second argument in a tuple
    count = cursor.fetchone()[0] #cursor.fetchone()  will take the results from the sql query in the previous line (which is just one row one column containing the count) and place it in a tuple, in this case itll look like this (some_num,) by saying [0] we acess that value and store it in the count variable
    conn.close()
    return count > 0 #if this statement returns true, then that means the website name the user is attempting to add to the database is already in it.

def update_password(website, new_password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE passwords SET password = ? WHERE website = ?', (new_password, website))
    conn.commit()
    conn.close()

def add_password(website, username, password):
    if website_exists(website):
        print(f"A password for {website} already exists. Choose a different website.\n")
        return False
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''') #will create the table within the database, if table passwords already exists then it does not create it.
    cursor.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)', (website, username, password)) #the ?'s are placeholders for the elements in the second argument which are in a tuple
    conn.commit()
    conn.close()
    return True

def get_password(website):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM passwords WHERE website = ?', (website,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None