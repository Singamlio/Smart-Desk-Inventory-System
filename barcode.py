import serial

# Open the ATR110 serial port
ser = serial.Serial(
    port="COM6",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

print("Waiting for barcode scans...")

while True:
    if ser.in_waiting > 0:
        barcode = ser.readline().decode("utf-8", errors="ignore").strip()

        if barcode:
            print(f"Barcode: {barcode}")
        if barcode = "x" #Put special barcode in here for special action
            print("Special Barcode Detected!") #Put Special action here
