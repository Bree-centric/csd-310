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

    print("\n-- DISPLAYING Employee RECORDS --")
    cursor.execute("SELECT * FROM employee")
    for row in cursor.fetchall():
        print("Employee ID: {}\nFirst Name: {}\nLast Name: {}\nEmail: {}\n".format(row[0], row[1], row[2], row[3]))

    print("\n-- DISPLAYING Customer RECORDS --")
    cursor.execute("SELECT * FROM customer")
    for row in cursor.fetchall():
        print("Customer ID: {}\nFirst Name: {}\nLast Name: {}\nPhone: {}\nAddress: {}\n".format(row[0], row[1], row[2], row[3], row[4]))

    print("\n-- DISPLAYING Trip RECORDS --")
    cursor.execute("SELECT * FROM trip")
    for row in cursor.fetchall():
        print("Trip ID: {}\nTrip Name: {}\nDestination: {}\nRegion: {}\nStart Date: {}\nEnd Date: {}\nPlanned By: {}\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    print("\n-- DISPLAYING Booking RECORDS --")
    cursor.execute("SELECT * FROM booking")
    for row in cursor.fetchall():
        print("Booking ID: {}\nCustomer ID: {}\nTrip ID: {}\nBooking Date: {}\nChecklist Reviewed: {}\n".format(
            row[0], row[1], row[2], row[3], row[4]))

    print("\n-- DISPLAYING Equipment RECORDS --")
    cursor.execute("SELECT * FROM equipment")
    for row in cursor.fetchall():
        print("Equipment ID: {}\nName: {}\nType: {}\nStatus: {}\nPurchase Date: {}\n".format(
            row[0], row[1], row[2], row[3], row[4]))

    print("\n-- DISPLAYING Transaction RECORDS --")
    cursor.execute("SELECT * FROM `transaction`")
    for row in cursor.fetchall():
        print("Transaction ID: {}\nCustomer ID: {}\nEquipment ID: {}\nType: {}\nDate: {}\nAmount: ${:.2f}\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5]))

    print("\n-- DISPLAYING Marketing Campaign RECORDS --")
    cursor.execute("SELECT * FROM marketing_campaign")
    for row in cursor.fetchall():
        print("Campaign ID: {}\nName: {}\nStart Date: {}\nEnd Date: {}\nRegion: {}\nManaged By: {}\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5]))

    print("\n-- DISPLAYING Campaign Recipient RECORDS --")
    cursor.execute("SELECT * FROM campaign_recipient")
    for row in cursor.fetchall():
        print("Campaign ID: {}\nCustomer ID: {}\nSent Date: {}\n".format(row[0], row[1], row[2]))

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

    print("\n-- DISPLAYING Employee RECORDS --")
    cursor.execute("SELECT * FROM employee")
    for row in cursor.fetchall():
        print("Employee ID: {}\nFirst Name: {}\nLast Name: {}\nEmail: {}\n".format(row[0], row[1], row[2], row[3]))

    print("\n-- DISPLAYING Customer RECORDS --")
    cursor.execute("SELECT * FROM customer")
    for row in cursor.fetchall():
        print("Customer ID: {}\nFirst Name: {}\nLast Name: {}\nPhone: {}\nAddress: {}\n".format(row[0], row[1], row[2], row[3], row[4]))

    print("\n-- DISPLAYING Trip RECORDS --")
    cursor.execute("SELECT * FROM trip")
    for row in cursor.fetchall():
        print("Trip ID: {}\nTrip Name: {}\nDestination: {}\nRegion: {}\nStart Date: {}\nEnd Date: {}\nPlanned By: {}\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    print("\n-- DISPLAYING Booking RECORDS --")
    cursor.execute("SELECT * FROM booking")
    for row in cursor.fetchall():
        print("Booking ID: {}\nCustomer ID: {}\nTrip ID: {}\nBooking Date: {}\nChecklist Reviewed: {}\n".format(
            row[0], row[1], row[2], row[3], row[4]))

    print("\n-- DISPLAYING Equipment RECORDS --")
    cursor.execute("SELECT * FROM equipment")
    for row in cursor.fetchall():
        print("Equipment ID: {}\nName: {}\nType: {}\nStatus: {}\nPurchase Date: {}\n".format(
            row[0], row[1], row[2], row[3], row[4]))

    print("\n-- DISPLAYING Transaction RECORDS --")
    cursor.execute("SELECT * FROM `transaction`")
    for row in cursor.fetchall():
        print("Transaction ID: {}\nCustomer ID: {}\nEquipment ID: {}\nType: {}\nDate: {}\nAmount: ${:.2f}\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5]))

    print("\n-- DISPLAYING Marketing Campaign RECORDS --")
    cursor.execute("SELECT * FROM marketing_campaign")
    for row in cursor.fetchall():
        print("Campaign ID: {}\nName: {}\nStart Date: {}\nEnd Date: {}\nRegion: {}\nManaged By: {}\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5]))

    print("\n-- DISPLAYING Campaign Recipient RECORDS --")
    cursor.execute("SELECT * FROM campaign_recipient")
    for row in cursor.fetchall():
        print("Campaign ID: {}\nCustomer ID: {}\nSent Date: {}\n".format(row[0], row[1], row[2]))

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


query = """
SELECT name, type, status, purchase_date
FROM equipment
WHERE purchase_date <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR);
"""

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"\nInventory Older Than 5 Years")
    print("Name | Type | Status | Purchase Date")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")
finally:
    cursor.close()
    conn.close()

query = """
SELECT e.Name AS equipment_name,
       COUNT(DISTINCT t.Customer_ID) AS unique_buyers,
       COUNT(*) AS total_purchases,
       SUM(t.Amount) AS total_revenue
FROM transaction t
JOIN equipment e ON t.Equipment_ID = e.Equipment_ID
WHERE t.Transaction_Type = 'purchase'
GROUP BY e.Name
ORDER BY total_revenue DESC;
"""

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nEquipment Sales Summary")
    print("Equipment Name | Unique Buyers | Total Purchases | Total Revenue")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | ${row[3]:.2f}")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")
finally:
    cursor.close()
    conn.close()