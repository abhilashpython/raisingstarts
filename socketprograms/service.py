import socket
import sys
try:
	s=socket.socket()
	host = socket.gethostname()
	port = 8069
	s.bind((host,port))
	s.listen(12)
	while 1:
		print "Service is waiting for the request:::"
		connecton_obj,ip_info=s.accept()
		connecton_obj.send('Acknowledgement: Coneected successfully')
		clinet_data=connecton_obj.recv(1024)
		if clinet_data == 'q':
			s.close()
			sys.exit()
		clinet_data = int(clinet_data)
		if clinet_data%2==0:
			res="EVEN"
		else:
			res="ODD"
		connecton_obj.send(res)


except Exception as err:
	print ".............>",err
finally:
	s.close()