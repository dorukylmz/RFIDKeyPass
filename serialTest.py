import serial.tools.list_ports
import serial

ports=serial.tools.list_ports.comports()
serialInst=serial.Serial()
for port in ports:
    print(str(port))

serialInst.baudrate=9600
serialInst.port="COM7"
serialInst.open()
packet='A'.encode(encoding='ascii')
packet=serialInst.write(packet)

x=0
while True:
    input()
    if (x%2==1) :
        packet='A'.encode(encoding='ascii')
    else:
        packet='K'.encode(encoding='ascii')
    packet=serialInst.write(packet)
    x+=1