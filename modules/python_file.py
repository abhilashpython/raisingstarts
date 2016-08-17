import file1
import file2
import file3
import mod1
import sqlite3
print mod1.f1.fun1()
print (file1.fun1())
print (file3.fun3())
try:
	con=sqlite3.connect("db2.db")
	#con.execute("create table persons(id int,name varchar(60))")
	#con.commit()
except Exception as err:
	print err
finally:
	pass
	#con.close()
#print (file3.fun4())

#import file2