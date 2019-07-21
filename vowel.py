s= input()
if (s=='A' or s=='a' or s=='E' or s=='e' or s=='I'
 or s=='i' or s=='O' or s=='o' or s=='U' or s=='u'):
    print("Vowel") 
elif ((s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z')):
     print("Consonant")
else:
    print("invalid")
