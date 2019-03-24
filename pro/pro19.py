n = int(input())
a = []
for i in range(n):
	t = list(map(int,input().split()))
	for j in t:
		a.append(j)
print(sorted(a))
