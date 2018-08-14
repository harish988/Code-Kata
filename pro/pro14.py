n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
for i in range(q):
    u,v = list(map(int,input().split()))
    x = 0
    for j in range(u,v+1):
           x ^= a[j-1]
    print(x)
