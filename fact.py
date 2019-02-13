n=int(input())
f=1
if n<2:
	print(f)
else:
	for i in range(1,n+1):
		f*=i
	print(f)
