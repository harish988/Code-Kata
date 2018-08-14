s = input()
s = s[0].upper() + s[1:]
for i in range(0,len(s)):
    if(s[i] == ' '):
        s = s[0:i+1] + s[i+1].upper() + s[i+2:]
print(s)
