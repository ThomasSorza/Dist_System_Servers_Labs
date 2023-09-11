import socket
import threading
import time

from server import Server

MAX_CLIENTS = 5
PORT = 446
queue_clients = []

""" def sacar_primero():
    #sacar primero  """

def getFistclient():
    return queue_clients.pop(0)

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                break  # If no data received, the client has disconnected
            message = data.decode('utf-8')  # Convert the received bytes to a string
            response = f"Received: {message}"
            client_socket.send(response.encode('utf-8'))  # Send a response back to the client
            print(f"Message from client: {message}")

    except Exception as e:
        print(f"Error while handling client: {e}")

    finally:
        client_socket.close()  # Close the client socket when done

def start(): 
    mainServer = Server(446, 2)
    slave = Server(447, 2)
    slave.bind()
    mainServer.bind()
    mainServer.startListening()
    print(f"Server listening on port {mainServer}...")

    while True:
        if(not mainServer.isFull()):
            # Accept a new connection and handle messages from the client
            try:
                client_socket, client_address = mainServer.accept()
                mainServer.getUsersConnected().append(client_socket)
                print(f"Connection from: {client_address}")
                client_socket.send("You are connected to the server.".encode('utf-8'))
                # Start a new thread to handle the client connection
                server1thread = threading.Thread(target=handle_client, args=(client_socket,))
                server1thread.start()

            except KeyboardInterrupt:
                print("Server shutting down.")
                break

        elif(slave.getIsListening()):
            slave.startListening()
            print(f"Slave Server listening on port {slave}...")

        elif(mainServer.isFull() and not slave.isFull()):
            try:
                # Encolar al cliente en el server 2
                slave.append(getFistclient)
            except:
                print("Server full")
                break
        else:
            queue_clients.append(client_socket)
            print("Server full")
            break

if __name__ == "__main__":
    start()