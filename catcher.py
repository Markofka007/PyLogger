import socket

# Define the host and port of the socket
HOST = "127.0.0.1"
PORT = 1337

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen(1)
print("Listening for connection...")

while True:
    try:
        # Accept a connection from a client
        conn, addr = sock.accept()

        # Loop to continuously receive data from the socket
        while True:
            # Receive data from the socket
            data = conn.recv(1024)

            # If no data is received, break out of the loop
            if not data:
                break

            # Decode the received data and display it to the terminal
            print(data.decode())

    except KeyboardInterrupt:
        print('KeyboardInterrupt received, closing the connection...')
        # Close the socket connection
        conn.close()
        break

    except socket.error:
        # When there is no connection available, keep listening
        pass