import serial
from serial.tools import list_ports

#usb scanner must be in 'USB CDC Host' mode

def listPorts():
    port = list(list_ports.comports())
    for p in port:
        print(p.device)

def createConnection(port, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE):
    ser = serial.Serial(
        port=port,
        baudrate=baudrate,
        parity=parity,
        stopbits=stopbits
    )
    return ser