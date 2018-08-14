s = input()
sum = 0
for i in range(0,len(s)):
	if(s[i] == 'I'):
		sum += 1
	if(s[i] == 'X'):
		sum += 10
		if(s[i-1] == 'I' and i>0):
			sum -= 2
	if(s[i] == 'V' and i>0):
		sum += 5
		if(s[i-1] == 'I'):
			sum -= 2
print(sum)
