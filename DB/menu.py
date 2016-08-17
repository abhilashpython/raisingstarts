while True:
	print """
	1.insert
	2.update
	3.delete
	"""
	option = raw_input("Enter an option or q to quit the program:")
	if option == 'q':
		break
	elif option == 1:
		print "proceed with insert"