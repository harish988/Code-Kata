n = int(input())
m = int(input())
a = []
b = []
for i in range(0,n):
    a.append(int(input()))
for j in range(0,m):
    b.append(int(input()))
k = 0
for i in b:
    if(i not in a):
        k = 1
if(k==0):
    print("yes")
else:
    print("no")
