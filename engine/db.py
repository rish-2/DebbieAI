import sqlite3


conn = sqlite3.connect("debbie.db")

cursor = conn.cursor()

#query = "CREATE TABLE IF NOT EXISTS appointments(id INTEGER PRIMARY KEY, title TEXT, date TEXT, time TEXT, description TEXT)"
#cursor.execute(query)

# to insert values
# query = "INSERT INTO sys_command VALUES (null,'OneNote', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done


# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# to insert values
#query = "INSERT INTO web_command VALUES (null,'navigation', 'https://www.google.com/maps/')"
#cursor.execute(query)
#conn.commit()
# conn.close()  # Don't forget to close the connection when done
