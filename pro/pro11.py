def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

n = int(input())
print(int(fact(n)/(2*fact(n-2))))
