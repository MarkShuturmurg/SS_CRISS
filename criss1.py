import socket

serverIP= '172.17.29.11'
serverPORT =6000

serveraddress =(serverIP, serverPORT)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = 'HI Harsh here 2022A3PS0418P'

bytestosend =str.encode(message)

UDPClientSocket.sendto(bytestosend, serveraddress)
