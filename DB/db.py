import psycopg2 as pg 
try:
	con = pg.connect(user="tcloudost",password="root",host="localhost",database="db3")
	print "Connected ",con
	cur = con.cursor()
	#cur.execute("create table persons(id int,name varchar(30))")
	'''
	1. from the user
	2. fro th list pf details
	3. list of dictionaries
	'''
	#person_id = raw_input("Enter id of the persion: ")
	#person_name = raw_input("Enter name of the persion: ")
	#query = "insert into persons values({0},'{1}')".format(person_id,person_name)
	#for per_id,per_name in zip(range(10),['n0','n1','n2','n3','n4','n4','n6','n7','n8','n9']): 
		#query = "insert into persons values({0},'{1}')".format(per_id,per_name)
	
	per_details = [
	{'id':10,'name':"name10"},
	{'id':11,'name':"name11"},
	{'id':13,'name':"name12"},
	{'id':14,'name':"name14"},
	{'id':16,'name':"name16"},
	]
	for i in per_details:
		query = "insert into persons values(%(id)s,'%(name)s')"%i
		#query = "insert into persons values({0},'{1}')".format(i['id'],i['name'])
		cur.execute(query)
	con.commit()

except Exception as err:
	print err
finally:
	con.close()