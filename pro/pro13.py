n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
for i in range(q):
    u,v = list(map(int,input().split()))
    min = 0
    for j in range(u,v+1):
        if(min < a[j]):
            min = a[j]
    print(sum)
