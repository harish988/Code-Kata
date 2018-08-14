n = int(input())
a = list(map(int,input().split()))
candies = len(a)
for i in range(1,len(a)-1):
    if(a[i]>a[i-1]):
        candies += 1
    if(a[i]>a[i+1]):
        candies += 1
if(a[0]>a[1]):
    candies += 1
if(a[-1]>a[-2]):
    candies += 1
print(candies)
