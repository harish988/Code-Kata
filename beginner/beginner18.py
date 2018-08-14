def amstrong(n):
	k = n
	sum = 0
	while(k>0):
		temp = k%10
		sum += temp * temp * temp
		k = k//n
	if(sum == n):
		print(n)
 
m = int(input())
n = int(input())
for i in range(m+1,n):
	amstrong(i)
