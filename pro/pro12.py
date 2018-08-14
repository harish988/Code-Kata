n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
for i in range(q):
    u,v = list(map(int,input().split()))
    sum = 0
    for j in range(u,v+1):
        sum += a[j]
    print(sum)
