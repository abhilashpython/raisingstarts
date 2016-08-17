import sqlite3
def get_con():
	con = sqlite3.connect('db1.db')
	return con
def create_tables():
	con = get_con()
	con.execute("create table persons(id int,name varchar(20))")
	con.close()
def inser_dummpy_data():
	con = get_con()
	ids=range(10)
	names=['n1','n2','n3','n4','n5','n6','n7','n8','n9','n10']
	for id_per,name_per in zip(ids,names):
		query = "insert into persons values(%d,'%s')"%(id_per,name_per)
		con.execute(query)
	con.commit()
	con.close()
def browse(table_name):
	con = get_con()
	cur = con.cursor()
	cur.execute("select * from %s"%table_name)
	return cur.fetchall()