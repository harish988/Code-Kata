n = input()
m = input()
k = 0
sum = 0
for i in range(len(m),len(n)):
    sum += i
for i in range(0,len(n)):
    if(n[i]!=m[i]):
        k += (ord(m[i])-ord(n[i]))
print(k+sum)
