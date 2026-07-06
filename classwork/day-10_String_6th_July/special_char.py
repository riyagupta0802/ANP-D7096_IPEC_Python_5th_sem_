'''Wap to count number of special characters in a given sentence'''

# input of sentence
sentence = input("Enter any sentence: ")

# initialize count variable
count = 0

# traverse each character of the sentence
for x in sentence:
    # check if the character is a special character
    if(x.isalpha() == False and x.isdigit() == False and x.isalnum() == False and x.isspace() == False):
        # increment count variable
        count = count + 1

# display the result
print("Number of special char =", count)
