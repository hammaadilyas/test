from socket import *
server_name = 'localhost'
server_port = 1200
client_socket = socket(AF_INET, SOCK_DGRAM)
print("UDP Client started.")
greeting = raw_input('Enter a greeting to send to the UDP server: ')
client_socket.sendto(greeting,(server_name, server_port))
server_message_count, server_address = client_socket.recvfrom(2048)
client_message_count = len(greeting)
print 'Greeting: {}, Character count from server = {}, Character count from client = {}'.format(greeting, server_message_count, client_message_count)
client_socket.close()