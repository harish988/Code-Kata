n = int(input())
k = int(input())
a = []
for i in range(0,n):
  temp = int(input())
  a.append(temp)
sum = 0
for i in range(0,k):
	sum += a[i]
print(sum)
