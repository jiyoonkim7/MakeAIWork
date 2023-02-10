# Define the string “paard”
word = "paard"

# Define number of vowels
vowels = 0

# Loop over each letter in string:
for char in word:
	
	# Check if vowel: a, e, i, o of u
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		
		# If so then increment counter
        vowels = vowels + 1

# Print result
if vowels > 0:

    print("Word has vowels")

else:

    print("Word has NO vowels")