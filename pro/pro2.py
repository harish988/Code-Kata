n = input()
k = int(input())
min = n
for i in range(0,k):
    for j in range(0,len(n)-1):
        temp = n[0:j]+n[j+1:]
        if(int(min) > int(temp)):
            min = temp
print(min)
