import socket
try:
	s=socket.socket()
	s.connect((socket.gethostname(),8069))
	print s.recv(1024)
	table_name = raw_input("Enter table name:")
	s.send(table_name)
	print "table_data: ",s.recv(1024)
except Exception as err:
	print err
finally:
	s.close()
