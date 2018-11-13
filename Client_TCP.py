import socket

#Take IP as input from user
TCP_IP = input("Please enter the server's IP Address: ")

#Take PORT as input from user, make sure it is castable to int or re-prompt
while True:
	TCP_PORT = input("Please enter the port the server is listening at: ")
	try:
		TCP_PORT = int(TCP_PORT)
		break
	except ValueError:
		pass

#Ask user for request to send to server
request = input("Please enter message to send to server: ")

print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT)) #connect with connection settings
print ("Connection to Server Established")
s.sendall(request.encode())  #encode and send message to server
response = s.recv(1024) #get response from server
s.close() #close socket

print("Server Response: ", response.decode()) #decode and echo response to user
