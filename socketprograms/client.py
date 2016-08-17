import socket
#print socket.gethostname()
#print socket.gethostbyname(socket.gethostname())
#print socket.gethostbyname('google.com')
'''
try:
	s=socket.socket()
	#s.connect(('google.com',80))
	s.connect(('google.com',800))
	print "Connected well"
except Exception as err:
	print "------------------->",err
finally:
	s.close()
'''
s=socket.socket()
host = socket.gethostname()
port = 8069
try:
	s.connect((host,port))
	ack=s.recv(1024)
	print ack
	number = raw_input("Emter a number:")
	s.send(number)
	response = s.recv(1024)
	print "You have entered "+response + " Number"
except Exception as err:
	print ",,,,,,,,,,,,>",err
finally:
	s.close()

