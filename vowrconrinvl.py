vow=['a','e','i','o','u']
ch = input()
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
	if ch in vow:
		print("Vowel")
	else:
		print("Consonant")
else:
     print("invalid")
