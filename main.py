import socket

DEBUG = False

localIP = "0.0.0.0"
localPort = 4464
bufferSize = 512

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening on port: {}".format(localPort))

hostAddresses = []

while(True):
    packetData = UDPServerSocket.recvfrom(bufferSize)
    message = packetData[0]
    address = packetData[1]

    clientMsg = "Message from Client {}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    if DEBUG:
        print(clientIP)

    if address not in hostAddresses:
        print("New client: {}".format(address))
        hostAddresses.append(address)

    for currentHostAddress in hostAddresses:
        if address != currentHostAddress:
            # Sending a reply to client
            UDPServerSocket.sendto(message, currentHostAddress)
            if DEBUG:
                print("Sending packet to {}".format(currentHostAddress))
