# WAP to input a sentence and count the number of vowels present

# Input of sentence
sentence = input("Enter a sentence: ")

# Initialize vowel count variable
vowels = 0

# Check each character of the sentence
for x in sentence:
    # Check if the character is a vowel
    if (x == 'A' or x == 'a' or
        x == 'E' or x == 'e' or
        x == 'I' or x == 'i' or
        x == 'O' or x == 'o' or
        x == 'U' or x == 'u'):
        
        # Increment vowel count
        vowels = vowels + 1

# Display the total number of vowels
print("Number of vowels =", vowels)