n = int(input())
a = []
k = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    if(a[i] == i):
        k.append(a[i])
if(k == []):
    print('-1')
else:
    k.sort()
    print(k)
