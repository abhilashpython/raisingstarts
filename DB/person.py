#import pandas as pd 
#data  = pd.read_csv('persons.csv')
#print data.columns
#print data.values
#....................................
f=open("persons.csv")
data=f.read()
data_lines = data.split('\n')
columns = data_lines[0]
data_records = data_lines[1:]
for i in columns.split(','):
	print i
#print "columns: ",columns
#print "data: ",data_records