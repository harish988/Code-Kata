n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    if(i%2==0 and a[i]%2!=0):
        print(a[i],sep='')
    elif(i%2!=0 and a[i]%2==0):
        print(a[i],sep='')
