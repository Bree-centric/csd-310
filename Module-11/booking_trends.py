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
SELECT e.name AS equipment_name,
       COUNT(DISTINCT t.customer_id) AS customers_bought,
       COUNT(t.transaction_id) AS total_purchases,
       SUM(t.amount) AS total_revenue
FROM `transaction` t
JOIN equipment e ON t.equipment_id = e.equipment_id
WHERE t.transaction_type = 'Purchase'
GROUP BY e.name
ORDER BY total_purchases DESC;
"""

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"\nEquipment Purchase Summary")
    print("Equipment | Customers Bought | Total Purchases | Total Revenue")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | ${row[3]:.2f}")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")
finally:
    cursor.close()
    conn.close()
