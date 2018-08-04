'''IS A STRING PALINDROME - A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of
palindromicwords. Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome. Display the result, including a me
aningful output message. '''

str=input('ENTER A STRING')
l=len(str)
index=0
p=l-1
while index <p:
    if str[index]==str[p]:
        index+=1
        p=p-1
        if index==p or index+1==p:
            print('string is palindrome')
    else:
        print('string is not palindrome')
        break


    
