n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
k = a[-1]
r = 2*k
b = [0,1]
for i in range(0,r):
    b.append(b[i]+b[i+1])
sum = 0
for i in b:
    if(i<k):
        sum += i
print(sum)
