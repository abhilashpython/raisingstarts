#!/usr/bin/env python
print "Content-type: text/html"
print 
print "<html><body>"
print """
<form action="action.py" method="get">
First Name: <input type="text" name="first_name">  <br />

Last Name: <input type="text" name="last_name" />
<input type="submit" value="Submit" />
</form>

"""

print "</body></html>"
