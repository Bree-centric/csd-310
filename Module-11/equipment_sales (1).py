import mysql.connector
from dotenv import dotenv_values

secrets = dotenv_values(".env")

config = {
    "user": secrets.get("USER"),
    "password": secrets.get("PASSWORD"),
    "host": secrets.get("HOST"),
    "database": secrets.get("DATABASE")
}

query = """
SELECT trip.region,
       YEAR(booking.booking_date) AS year,
       COUNT(*) AS total_bookings
FROM booking
JOIN trip ON booking.trip_id = trip.trip_id
GROUP BY trip.region, year
ORDER BY trip.region, year;
"""

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"\nBooking Trends by Region and Year")
    print("Region | Year | Total Bookings")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")
finally:
    cursor.close()
    conn.close()
\