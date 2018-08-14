n = int(input())
k = n
sum = 0
while(k>0):
	temp = k%10
	sum += temp * temp * temp
	k = k//n
if(sum == n):
	print("yes")
else:
	print("no")
