m = input()
n = input()
if(len(m)-len(n)>1):
    print("no")
k = 0
for i in range(0,len(m)):
    if(m[i] != n[i]):
        k += 1
if(k>1):
    print("no")
else:
    print("yes")
