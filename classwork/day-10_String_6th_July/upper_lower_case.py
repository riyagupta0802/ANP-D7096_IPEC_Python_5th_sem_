'''Wap to count numb of upper case and lower case character in a given sentence without using lib functions'''

#input of sentence
sentence = input("Enter a sentence :")

#initialize upper case and lower case count variable
upper=0
lower=0

for x in sentence:
    if(x>="A" and x<="Z"):
        #increment upper case count variable
        upper=upper + 1 
    if(x>="a" and x<="z"):
        #increment lower case count variable
        lower=lower + 1 
#-----------------------------------------------------
print("Number of upper case characters =" , upper) 
print("Number of lower case characters =" , lower)           
