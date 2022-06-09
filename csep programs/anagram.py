String1 =input("Enter the first string:")
String2 =input("Enter the second string:")

String1 = sorted(String1.lower())
String2 = sorted(String2.lower())

print("String1 after sorting: ", String1)
print("String2 after sorting: ", String2)

if String1 == String2:
    print('Strings are anagram')
else:
    print('Strings are not anagram')