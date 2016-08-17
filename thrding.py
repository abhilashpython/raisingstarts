import threading
def fun1():
	print "hello world"
def fun2():
	print "hello world"
t1=threading("t1",target=fun1)
t2=threading("t2",target-fun2)