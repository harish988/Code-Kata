n = input()
vowel = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
if(n in  vowel):
	print("Vowel")
elif(n in consonant):
	print("Consonant")
else:
	print("Invalid")
