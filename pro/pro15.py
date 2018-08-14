n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    temp = bin(i)
    count = 0
    for j in temp[2:]:
        if(j == '1'):
            count += 1
    b.append(count)
for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if(b[i] > b[j]):
            temp = b[i]
            b[i] = b[j]
            b[j] = temp
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
a.reverse()
for i in a:
    print(i)
