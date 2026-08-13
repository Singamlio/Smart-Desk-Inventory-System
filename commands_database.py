import sqlite3

DATABASE_PATH = "inventory.db"


def _get_connection():
    return sqlite3.connect(DATABASE_PATH)


def ensure_database():
    connection = _get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL DEFAULT 0,
        location TEXT
    )
    """)
    connection.commit()
    connection.close()


def add_item(barcode, item_name, item_quantity, location):
    """Adds a new item to the inventory database."""
    ensure_database()
    connection = _get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO items (barcode, name, quantity, location) VALUES (?, ?, ?, ?)",
            (barcode, item_name, item_quantity, location)
        )
        connection.commit()
        print("Item added!")
    except sqlite3.IntegrityError:
        print(f"Item with barcode '{barcode}' already exists. No item was added.")
    finally:
        connection.close()


def get_item(barcode):
    """Returns the item row for the barcode or None if not found."""
    ensure_database()
    connection = _get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items WHERE barcode = ?", (barcode,))
    item = cursor.fetchone()
    connection.close()
    return item


def print_inventory():
    """Prints all items currently stored in the inventory database."""
    ensure_database()
    connection = _get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    if not items:
        print("Inventory is empty.")
    else:
        print("Current inventory:")
        for item in items:
            print(item)

    connection.close()