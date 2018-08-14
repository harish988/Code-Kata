def gcd(m,n):
    if(n == 0):
        return m
    else:
        return gcd(n,m%n)

n = int(input())
q = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,q):
    a = int(input())
    b = int(input())
    print(gcd(a,b))
