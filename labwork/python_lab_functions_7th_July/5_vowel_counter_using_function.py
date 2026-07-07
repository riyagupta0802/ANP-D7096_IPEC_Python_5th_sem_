'''--------------Vowel Counter using Function-----------------

Problem Statement:
Write a Python program that defines a function count_vowels(text). 
The function should: 
• Accept a string.  
• Count the total number of vowels (a, e, i, o, u) irrespective of case.  
• Return the total vowel count.  
------------------------------------
The main program should: 
• Accept a sentence from the user.  
• Call the function.  
• Display the total number of vowels.  
----------------------------------------------
Sample Output 
Enter a sentence: 
Python Programming is Fun 

Total Vowels: 6
'''

#function to count vowels
def count_vowels(text):
    count = 0

    for x in text:
        if x == 'a' or x == 'A' or x == 'e' or x == 'E' or x == 'i' or x == 'I' or x == 'o' or x == 'O' or x == 'u' or x == 'U':
            count = count + 1

    return count
#--------------------------------------------------------
# Main Program
text = input("Enter a sentence: ")
print("Total number of vowels =", count_vowels(text))


'''Output:

Enter a sentence: 
Python Programming is Fun 
 
Total Vowels: 6
'''