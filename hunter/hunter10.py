n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    for j in range(0,n):
        if(a[i]+a[j] == 0 and i!=j):
            print(a[i],a[j])
