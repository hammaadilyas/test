from socket import *
server_name = "localhost"
server_port = 1200
client_socket = socket(AF_INET, SOCK_STREAM)
print("TCP Client started.")
greeting = raw_input('Enter a greeting to send to the server: ')
client_socket.connect((server_name, server_port))
client_socket.send(greeting)
server_message_count = client_socket.recv(1024)
client_message_count = len(greeting)
print 'Greeting: {}, Character count from server = {}, Character count from client = {}'.format(greeting, server_message_count, client_message_count)
client_socket.close()

