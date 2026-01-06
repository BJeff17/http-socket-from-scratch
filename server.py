import socket

from http_utils import http_request_parser, http_response
from socket_utils import recv_all 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8081



server_socket.bind(("localhost", PORT))


server_socket.listen()
print(f"server running on http://localhost:{PORT}")
while True:
    is_client_socket = False
    print("Waiting for connection...")
    try:
        print("Before accept")
        client_socket, client_addr = server_socket.accept()
        is_client_socket = True
        print(f"Connection from {client_addr}")    
        out = recv_all(client_socket)
       
        print(http_request_parser(out))

        resp = http_response(out)




        client_socket.sendall(resp)
    except Exception as e:
        if isinstance(e,KeyboardInterrupt):
            print(f"Arret du server!")
            break
        else:
            print("Erreur inconnue: ", e)
            print("Continuing...")
    finally:
        if is_client_socket:client_socket.close()
server_socket.close()




