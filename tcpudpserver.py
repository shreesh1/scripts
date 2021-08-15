import socket
import sys
import logging
import time,datetime
import argparse



size = 1024
host = '127.0.0.1'

def tcp_proto(port):
	print(f"TCP server running on {host} at {port}")
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host,port))
	sock.listen(1)
	while True:
		connection, client_address = sock.accept()
		while True:
			data = connection.recv(size)
			print(data.decode('utf-8').replace('\n', ''))
			kl = "how you doing " + data.decode('utf-8').replace('\n', '')+'\r\n'
			if data :
				connection.sendall(kl.encode())
			else:
				break
	sock.close()

def udp_proto(port):
	print(f"UDP server running on {host} at {port}")
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host,port))
	while True:
		data, address = sock.recvfrom(size)
		print(data)
		if data :
			sock.sendto(data,address)
		else:
			break
	sock.close()	





def main():
	parser = argparse.ArgumentParser(description='TCP/UDP Server')
	parser.add_argument('-p','--port',type=int,required=True)
	parser.add_argument('-t','--type',choices=['tcp','udp'],required=True)
	args=parser.parse_args()
	port = args.port
	if(not(port>=0 and port <= 65535)):
		print("Port should be between 0-65535")
		exit(0)
	protocol = args.type
	if protocol == "tcp":
		tcp_proto(port)
	elif protocol == "udp":
		udp_proto(port)
	else:
		sys.exit("invalid protocol pls choose between tcp or udp")


if __name__ == "__main__":
	main()
