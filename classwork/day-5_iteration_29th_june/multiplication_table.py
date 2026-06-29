'''---------- Multiplication Table Generator ------

Display multiplication table up to 20.

---------------------------------------------------'''

#--------------------------------------------------
#---------------- Coding --------------------------

num = int(input("Enter Number : "))

for i in range(1,21):
    print(num,"x",i,"=",num*i)

#--------------------------------------------------

''' Output :

Enter Number : 8

8 x 1 = 8
8 x 2 = 16
...
8 x 20 = 160

'''
