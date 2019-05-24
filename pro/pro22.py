n = int(input())
l = list(map(int,input().split()))
temp = 0
for i in range(2,n):	
	if(divide(l,n,i) == 1):	
		print("yes")
		temp = 1
		break
if(temp == 0):
	print("no")
	
	
	
	
	
n = int(input())
l = list(map(int,input().split()))
sum = 0 
index = []
for i in range(n):
	index.append(i)
desc = l
for i in range(n-1):
	for j in range(i+1,n):
		if(l[i] < l[j]):
			temp1 = l[i]
			temp2 = index[i]
			index[i] = index[j]
			index[j] = temp2
			l[i] = l[j]
			l[j] = temp1
sum += desc[0]
k=index[0]
select = [k]
for i in range(1,n):
	if(index[i]-1 not in select and index[i]+1 not in select):
		sum += desc[i]
		select.append(index[i])
print(sum)
