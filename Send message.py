# I skal bruge Pygame (pip install pygame) til keyboard.
# socket skal I ikke installere. Batteries included:)
#
import socket
from time import sleep
UDP_IP = "10.100.0.131" #IP på jeres Raspberry
UDP_PORT = 5005 #Port på Raspberry (skal også sættes til samme i raspberry pi python script)
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP

def sendUDP(MESSAGE): #sender tekstbesked via UDP
    sock.sendto(bytes(MESSAGE,"ASCII"), (UDP_IP, UDP_PORT))
    print (MESSAGE)
while 1:
    sendUDP('e23 2nd, gruppe 5, TGH, 69')
    sleep(30)
