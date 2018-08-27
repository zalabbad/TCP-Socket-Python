from socket import *
import datetime
#to count the number of clients connected to our server
clientCount = 1
serverPort = 12000
#AF_INET is for IPv4 - SOCK_STREAM is for TCP
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is listening on localhost :', serverPort
print '-----------------------------------------------------'
while 1:
    connectionSocket, addr = serverSocket.accept()
    print 'Client #', clientCount
    print '--> message reveived from client #', clientCount, \
          connectionSocket.getpeername()[0], \
          ":", \
          connectionSocket.getpeername()[1], \
          'on', datetime.datetime.now()
    sentence = connectionSocket.recv(1024)
    numOfCharacters = len(sentence)
    connectionSocket.send(str(numOfCharacters))
    print '<-- message sent to client #', clientCount,  \
          connectionSocket.getpeername()[0], \
          ":", \
          connectionSocket.getpeername()[1], \
          'on', datetime.datetime.now()
    connectionSocket.close()
    print 'Connection closed with Client #', clientCount
    print '-----------------------------------------------------'
    clientCount += 1 