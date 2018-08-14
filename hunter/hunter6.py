n = input()
k = 0
m = 0
for i in n:
    if(int(i)>0 and int(i)<=26):
        k+=1
m += 1
for i in range(0,len(n)):
    if(i < len(n)-1):
        if((int(a[i])*10+int(a[i+1]))<27 and (int(a[i])*10+int(a[i+1]))>0):
            m+=1
print(m-1)
