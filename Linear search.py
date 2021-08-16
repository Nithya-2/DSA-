Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pos=-1
>>> def search(list,n):
	i=0
	while i<len(list):
		if list[i]== n;
		
SyntaxError: invalid syntax
>>> def search(list,n):
	i=0
	while i<len(list):
		if list[i]== n:
			globals() ['pos'] = i
			return True
		return False
	list = [5,8,4,6,9,2]
	n=9
	if search(list,n):
		print("Found at",pos+1)
		else:
			
SyntaxError: invalid syntax
>>> def search(list,n):
	i=0
	while i<len(list):
		if list[i]== n:
			globals() ['pos'] = i
			return True
		return False
	list = [5,8,4,6,9,2]
	n=9
	if search(list,n):
		print("Found at",pos+1)
	else:
		print("Not found")