
from itertools import combinations
from statistics import mean
def divide(array, n, avg):	
	one = list(combinations(array ,n))
	for i in one:
		other = []
		for j in array:
			if j not in one:
				other.append(j)
			
		if mean(list(i)) == mean(other):
			return 1
	return 0
	

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
