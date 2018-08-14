def prime(n):
    k = 0
    for i in range(2,n):
        if(n%i == 0):
            k = 1
    if(k==1):
        return 0
    else:
        return 1

l = int(input())
r = int(input())
n = 0
for i in range(l,r+1):
    if(prime(i) == 1 and i!=1):
        n += 1
print(n)
