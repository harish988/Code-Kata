n = int(input())
a = []
k = set()
for i in range(0,n):
    a.append(int(input()))
for i in a:
    k.add(i)
l = list(k)
l.sort(reverse = True)
print(l)
n = 0
for i in l:
    n = n*10 + i
print(n)
