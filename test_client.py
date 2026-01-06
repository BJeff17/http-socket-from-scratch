import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8081))
request = b"GET /assets/illustration-anime-city-v3.jpg HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.sendall(request)

chunk = client_socket.recv(4096)
print(chunk[:200])
client_socket.close()
