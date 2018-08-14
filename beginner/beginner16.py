def prime(n):
	k = 0
	for i in range(2,n):
		if(n%i == 0):
			k = 1
	if(k==0):
		print(n)

n = int(input())
m = int(input())
for i in range(n+1,m):
	prime(i)
