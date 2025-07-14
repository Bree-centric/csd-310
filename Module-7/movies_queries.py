import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Load login info from .env file
secrets = dotenv_values(".env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    for row in cursor.fetchall():
        print("Studio ID: {}\nStudio Name: {}\n".format(row[0], row[1]))

    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    for row in cursor.fetchall():
        print("Genre ID: {}\nGenre Name: {}\n".format(row[0], row[1]))

    print("\n-- DISPLAYING Short Film Names (less than 2 hours) --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    for row in cursor.fetchall():
        print("Film Name: {}\nRuntime: {} minutes\n".format(row[0], row[1]))

    print("\n-- DISPLAYING Films Grouped by Director --")
    cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director")
    for row in cursor.fetchall():
        print("Director: {}\nFilm Name: {}\n".format(row[0], row[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)

finally:
    cursor.close()
    db.close()
