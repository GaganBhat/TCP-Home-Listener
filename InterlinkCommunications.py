import serial
import time
import socket

TCP_IP = '192.168.1.169'
TCP_PORT = 5000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print
'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data)
    conn.send(data)  # echo
    conn.close()
#
# ser = serial.Serial(port='COM10', baudrate='9600')
# if ser.is_open:
#     time.sleep(2)
#     ser.write(b'1')
#     time.sleep(1)
#     ser.write(b'0')
# else:
#     ser.open()
#     time.sleep(2)
#     ser.write(b'0')


