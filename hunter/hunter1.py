n = int(input())
a = []
k = set()
for i in range(0,n):
    a.append(int(input()))
for i in a:
    if(a.count(i)>1):
        k.add(i)
l = list(k)
if(l == []):
    print("unique")
else:
    print(l)
