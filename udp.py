import socket
import sys
import time

UDP_IP_ADDRESS = '192.168.4.1'
UDP_PORT = 40001

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((UDP_IP_ADDRESS, UDP_PORT))

while True:
	try:
		data, addr = serverSocket.recvfrom(1024)
		split_data = data.decode("utf-8").split("@")
		f = open("data_" + split_data[0] + ".csv", "a")
		str_time = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
		str_utc = str(int(time.time()))
		time_entry = str_utc + ", " + str_time + ", "
		f.write(time_entry)
		f.write(split_data[1])
		f.write('\n')
		f.close()
		print ("Message from " + split_data[0] + " : ", split_data[1])
	except:
		print ("Exception occured")
		continue
