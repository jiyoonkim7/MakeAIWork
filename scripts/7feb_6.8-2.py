import re

str = "happy2023"

print(len(str))
print(str *10)

print("the first value of the list is:" )
print(str[0])
print ("first 3 value of the list is:" )
print(str[0:3])

print ("The last three characters of the string:" )
N=4
Str2 = str[-N:]
print(Str2)

print("The string backwards")
print(str[::-1])

if len(str) > 7:
    print("The seventh character of the string:" )
    print(str[6]) 
else: 
    print("The word is too short.")   

print ("The string with its first and last characters removed:")
print(str[1:-1])

print ("The string in all caps")
print(str.upper())

print("The string with every a replaced with an e:" )
Str3 = str.replace("a", "e")
print(Str3)

print("The string with every letter replaced by a space:")

string = "happy 2023"
new_str = re.sub(r"[^0-9]", " ", string)
print(new_str)

string = "happy 2023"

newStr = ""

for char in list(string):
    
    if char.isalnum():
        newStr += " "
    else:
        newStr += char

print( f"[{newStr}]" )


