'''---------Word Frequency Counter---------
Problem Statement: 
Accept a sentence from the user and create a dictionary that stores the frequency of each word. 
-------------------------------------------------------------
Example: 
Input: 
python is easy and python is powerful 
-------------------------------------------------------------
Output: 
{ 
'python': 2, 
'is': 2, 
'easy': 1, 
'and': 1, 
'powerful': 1 
} 
-----------------------------------------------------------------
Additionally: 
• Display the most frequently occurring word.  
• Display all words in alphabetical order.  '''


# input sentence
sentence = input("Enter a Sentence: ")

# split sentence into words
words = sentence.split()

# initialize dictionary
frequency = {}

# count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print("-------------------------------------------------")

# display frequency dictionary
print("Word Frequency:", frequency)
print("-------------------------------------------------")

# display most frequent word
highest = max(frequency, key=frequency.get)

print("Most Frequently Occurring Word:")
print(highest, frequency[highest])
print("-------------------------------------------------")

# display words in alphabetical order
print("Words in Alphabetical Order:")
for word in sorted(frequency):
    print(word, frequency[word])



'''
Output:-
Enter a Sentence: python is easy and python is powerful
-------------------------------------------------
Word Frequency: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
-------------------------------------------------
Most Frequently Occurring Word:
python 2
-------------------------------------------------
Words in Alphabetical Order:
and 1
easy 1
is 2
powerful 1
python 2
'''    