import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

print(ports)
for port in ports:
    print(f'Порт доуступа {port.device}')

port = "COM4"  # Replace with the appropriate COM port name
baudrate = 19200  # Replace with the desired baud rate

with serial.Serial(port, 19200, timeout=1) as ser:
    mes = ['01', '03', '00', '00','00','0A','C5','CD']
    for ch in mes:
        ser.write(b'ch')
    s = ser.read(10)        # read up to ten bytes (timeout)
    print(s)
    line = ser.readline()   # read a '\n' terminated line
    print(line)

ser.close()  # Remember to close the connection when done