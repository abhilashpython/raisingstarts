import pdb
print "program started"
def sum1(a1):
	print a1
	a1 = a1+[10,20,30,4]
	return sum(a1)
a=10
b=20
c=30
d=40
f=0
l=[a,b,c,d,f]
pdb.set_trace()
print sum1(l)
for i in l:
	print "iteration started"
	print 10/i
print "program ended"