import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM items")

items = cursor.fetchall()

for item in items:
    print(item)

connection.close()