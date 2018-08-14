n = int(input())
k = 0
temp = 0
while(n>0):
	temp = n%10
	k = k*10 + temp
	n = n//10
print(k)
