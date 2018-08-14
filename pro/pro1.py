n = int(input())
a = []
for i in range(0,n):
    a.append(input())
k = []
for j in range(0,len(a[i])):
    if(a[0][j] == a[1][j]):
        k.append(a[0][j])
for i in range(2,n):
    if(k not in a[i]):
        for j in range(0,len(k)):
            if(k[j] == a[i]):
                k[j] = a[i]
                k[j+1] = 0
for i in k:
    if(i==0):
        break
    else:
        print(i)
