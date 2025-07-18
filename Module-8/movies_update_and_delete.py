import mysql.connector

# Configure database connection
config = {
    "user": "root",  # change this if your username is different
    "password": "yourpassword",  # replace with your actual MySQL password
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# Function to display films
def show_films(cursor, title):
    query = """
        SELECT film_name AS Name,
               film_director AS Director,
               genre_name AS Genre,
               studio_name AS Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()

    print("\n-- {} --".format(title))
    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre: {}".format(film[2]))
        print("Studio: {}\n".format(film[3]))

try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Initial display
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film (use a valid studio_id and genre_id from your DB)
    cursor.execute("""
        INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES ('Star Wars', '1977', 121, 'George Lucas', 2, 2)
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update 'Alien' to be a Horror film (genre_id = 1)
    cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete 'Gladiator'
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    print("Database error:", err)

finally:
    cursor.close()
    db.close()
