n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    if(a.count(a[i]) == 1):
        k = a[i]
print(a[i])
