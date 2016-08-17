import socket
import db
import json
try:
	s=socket.socket()
	s.bind((socket.gethostname(),8069))
	s.listen(5)
	print "Waiting for the request"
	co,ip_info=s.accept()
	co.send("Connection created successfully")
	table_name = co.recv(1024)
	data= db.browse(table_name)
	data_json = json.dumps(data)
	co.send(data_json)
except Exception as err:
	print err
finally:
	s.close()
