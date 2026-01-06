import socket

def write_chunk_by_chunk_in_file(filename, data):
    with open(filename, 'wb') as f:
        for chunk in data:
            f.write(chunk)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8081))
# client_socket.connect(("127.0.0.1", 8081))
print("Connected")
request = b"GET /assets/illustration-anime-city-v3.jpg HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.sendall(request)
print("Request sent")
response = b""
received_bytes = 0
while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    response += chunk
    received_bytes += len(chunk)
    if received_bytes % (1024*1024) == 0:
        print(f"Received {received_bytes} bytes")
print(f"Finished receiving {received_bytes} bytes")

header_end = response.find(b"\r\n\r\n")
if header_end != -1:
    body = response[header_end + 4:]
    write_chunk_by_chunk_in_file("downloaded_image.jpg", [body])
    print("Image saved without headers")
else:
    print("Error: Could not find end of headers")

client_socket.close()