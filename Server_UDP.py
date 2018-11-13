import socket
import datetime

#IP and PORT information (MODIFY THESE)
UDP_IP = '192.168.134.1'   #IP address here
UDP_PORT = 5001   #PORT number here

#Internet and UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((UDP_IP, UDP_PORT))

print("UDP SERVER @ ", UDP_IP, "ON PORT ", UDP_PORT )

#server will be ready to receive a new connection after service each one
while True:
	data, addr = s.recvfrom(1024) #buffer size of 1024
	print("Request received from: ", addr)
	
	req = data.decode() #decode binary from client

	#if the request matches the keyphrase
	if req == "What is the current date and time?":
			print("Client Request: ", req)
			currentDT = datetime.datetime.now(); #get the current datetime
			#format the date into MM/DD/YYYY HH:MM:SS
			formattedDT = str(currentDT.month) + "/" + str(currentDT.day) + "/" + str(currentDT.year) + " " + str(currentDT.hour) + ":" + str(currentDT.minute) + ":" + str(currentDT.second)
			response = "Current Date and Time - " + formattedDT #finalize the output
			s.sendto(response.encode(), addr) #encode and send back to client's address 
	else:
			s.sendto("Invalid Request".encode(), addr) #invalid message to send back to client
