import socket

send_data = input("Enter: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 3000))

client.sendall(bytes(send_data, 'utf-8'))
data = client.recv(1024).decode('utf-8')

print("Received: ", data)

client.close()