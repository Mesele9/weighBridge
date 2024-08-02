# serial_communication.py
import serial

def read_weight():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        weight_data = ser.readline().decode('utf-8').strip()
        ser.close()
        return weight_data
    except serial.SerialException as e:
        print(f"Error reading from serial port: {e}")
        return None

