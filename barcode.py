import serial
import commands_database

# Open the ATR110 serial port
ser = serial.Serial(
    port="COM6",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

commands_database.ensure_database()
commands_database.print_inventory()
print("Waiting for barcode scans...")

while True:
    if ser.in_waiting > 0:
        barcode = ser.readline().decode("utf-8", errors="ignore").strip()

        if not barcode:
            continue

        print(f"Scanned barcode: {barcode}")
        item = commands_database.get_item(barcode)

        if item:
            print("Item found:")
            print(item)
            continue

        print("Barcode not found in inventory.")
        add_new = input("Do you want to add this item? [y/N]: ").strip().lower()

        if add_new != "y":
            continue

        name = input("Item name: ").strip()
        quantity_text = input("Quantity: ").strip()
        location = input("Location: ").strip() or None

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Invalid quantity entered. Item not added.")
            continue

        commands_database.add_item(barcode, name, quantity, location)

