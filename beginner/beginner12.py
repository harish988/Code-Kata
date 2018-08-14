n = int(input())
rev = 0
k = n
while(k>0)
	rev = (rev*10) + (k%10)
	k = k//10
if(rev == n):
	print("yes")
else:
	print("no")
