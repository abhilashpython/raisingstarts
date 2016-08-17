import psycopg2 as pg 
try:
	con = pg.connect(user="tcloudost",password="root",host="localhost",database="db3")
	print "Connected ",con
	cur = con.cursor()
	#ret_cur = cur.execute("select * from persons")
	per_id = raw_input("Enter id to search person details:")
	query = "select * from persons where id=%s"%per_id
	cur.execute(query)
	#cur.execute("insert into persons values(120,'name120')")
	data = cur.fetchall()
	#data1 = cur.fetchall()
	print data1,'sdfsdfsdfsfsfsdf'
	if data:
		print data
	else:
		print "No data found"
except Exception as err:
	print err
finally:
	cur.close()
	con.close()
