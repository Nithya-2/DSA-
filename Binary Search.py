pos =-1
 def search(list,n):
	l=0
	u=len(list)-1
	while l<u:
		mid=(l+u)//2
		if list[mid]==n:
			globus()['pos']=mid
			return True
		else:
			if list[mid]<n:
				l=mid;
			else:
				u=mid;

				
list=[4,5,9,1,99,3]
 if search(list,n):
	print("Found at",pos+1)
 else:
	print("Not found")
