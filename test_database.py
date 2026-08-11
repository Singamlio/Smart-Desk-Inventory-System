import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO items (barcode, name, quantity, location)
VALUES (?, ?, ?, ?)
""", ("X003W1595L", "Red LED", 25, "A1"))

connection.commit()
connection.close()

print("Item added!")