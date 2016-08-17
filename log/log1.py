import logging
logging.basicConfig(level=logging.WARN,filename="log1.txt",
	format="%(asctime)s,%(levelname)s:%(message)s")
logging.info('Program started')

def fun1(a,b):
	logging.info('function execution started')
	a1=a+100
	b1=b+100
	return a1+b1
fret=fun1(10,20)
logging.info('function executed well: return value:%d'%fret)
value=raw_input("Enter a vlaue:")
if not value.isdigit():
	logging.warn('USer entered alphnumeric value')
l=range(10,100,10)
logging.info("list initiated:%r"%l)
try:
	logging.info("Try block initiated")
	value=int(value)
	for i in l:
		print i/value
	logging.info("Try block executed well")
except Exception as err:
	logging.exception("Error:%r"%err)
	print err

logging.info('Program ended')