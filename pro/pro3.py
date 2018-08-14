n = input()
m = input()
k = 0
l = len(m) - len(n)
for i in range(0,len(n)):
    if(n[i]!=m[i]):
        k+=1
print(k+l)
