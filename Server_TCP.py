import socket
import datetime

#IP and PORT information (MODIFY THESE)
TCP_IP = '192.168.134.1'  #IP address here
TCP_PORT = 5001  #PORT number here

#Inter and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1) #listen for connections
print('Server Address: ', TCP_IP)
print('Listening on port: ', TCP_PORT)

#ready to accept connection after respondng to each one
while True:
	conn, addr = s.accept()  #accept connection
	print('\nClient Address: ', addr)
	print('Connection to Client Established')
	data = conn.recv(1024)	#recieve the message from client
	req = data.decode() #decode into string

	#if client request matches keyphrase
	if req == "What is the current date and time?":
		print("Client Request: ", req)
		currentDT = datetime.datetime.now(); #get current datetime
		#format datetime into MM/DD/YYYY HH:MM:SS
		formattedDT = str(currentDT.month) + "/" + str(currentDT.day) + "/" + str(currentDT.year) + " " + str(currentDT.hour) + ":" + str(currentDT.minute) + ":" + str(currentDT.second)
		response = "Current Date and Time - " + formattedDT #final message to send back
		conn.send(response.encode()) #encode and send
	else:
		conn.send("Invalid Request".encode()) #invalid request message
	
	conn.close()