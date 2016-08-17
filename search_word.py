import sys
comd_req = sys.argv[1:]
file_path = comd_req[0]
search_word = comd_req[1]
file_data = open(file_path).read()
if search_word in file_data:
	print "searching word is there in file"
else:
	print "Not found"
