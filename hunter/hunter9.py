n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            if(i<j<k and a[i]+a[j]==a[k]):
                print(a[i],a[j],a[k])
