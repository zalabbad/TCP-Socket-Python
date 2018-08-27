#TCP Socket Programming with Python
##What is this project about?
This project demonstrates how to program TCP sockets with Python. The project has two main files: Server(TCPServer.py) and Client(TCPClient.py).
##What does it do?
The server receives string values form clients and sends back the length of the received string.
##How to use it?
* First, you need to run the server(TCPServer.py) and keep it running to listen for requests from clients. Server is running on localhost(=127.0.0.1) with port number(12000).
* Second, run the client(TCPClient.py). You will be asked to enter server hostname or IP and server port, use (localhost or 127.0.0.1) for hostname or IP and (12000) for server port. While the server is running, you can run as many clients(TCPClient.py) as you want and the server will serve them. Also, Server will count how many clients had connected to it.