n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
k = 0
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            if(i<j<k and a[i]<a[j]<a[k]):
                k += 1
print(k)
