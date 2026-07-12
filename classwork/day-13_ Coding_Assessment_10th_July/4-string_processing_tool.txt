
'''--- String Processing Tool---

Write a Python program that accepts a sentence from the user. 
Create separate user-defined functions to: 
1. Count vowels.  
2. Count consonants.  
3. Count words.  
4. Reverse the sentence.  
Display all the results. 
---------------------------------------
Sample Input 
Python Programming Language 
Sample Output 
Vowels : 7 
Consonants : 19 
Words : 3 
Reverse : 
egaugnaL gnimmargorP nohtyP
'''

# Function to count vowels
def count_vowels(sentence):
    count = 0
    for ch in sentence:
        if ch in "AEIOUaeiou":
            count = count + 1
    return count


# Function to count consonants
def count_consonants(sentence):
    count = 0
    for ch in sentence:
        if ch.isalpha() and ch not in "AEIOUaeiou":
            count = count + 1
    return count


# Function to count words
def count_words(sentence):
    words = sentence.split()
    return len(words)


# Function to reverse the sentence
def reverse_sentence(sentence):
    return sentence[::-1]


# Main Program
sentence = input("Enter a sentence: ")

print("Vowels :", count_vowels(sentence))
print("Consonants :", count_consonants(sentence))
print("Words :", count_words(sentence))
print("Reverse :", reverse_sentence(sentence))