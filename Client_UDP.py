import socket

#Take IP as input from user
UDP_IP = input("Please enter the server's IP Address: ")

#Take PORT as input from user, make sure it is castable to int or re-prompt
while True:
	UDP_PORT = input("Please enter the port the server is listening at: ")
	try:
		UDP_PORT = int(UDP_PORT)
		break
	except ValueError:
		pass

#Ask user for request to send to server
request = input("Please enter message to send to server: ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("sending request to ", UDP_IP, "at port ", UDP_PORT)
s.sendto(request.encode(), (UDP_IP,UDP_PORT)) #send message to connection details
data, addr = s.recvfrom(1024)	#receive response from server
response = data.decode()	#decode response
print("Server response: ", response) #echo to user

