s1=str(input("Enter a string:"))
s2=str(input("Enter a string:"))
if(sorted(s1)== sorted(s2)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")