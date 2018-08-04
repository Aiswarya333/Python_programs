'''MULTIPLE WORD PALINDROME - There are numerous phrases that are palindromes when spacing is ignored. Examples include “go dog”, “flee to me remote elf” and “some men
interpret nine memos”, among many others. Extend your solution to Exercise 72 so that it ignores spacing while determining whether or not a string is a palindrome. For
an additional challenge, extend your solution so that is also ignores punctuation marks and treats uppercase and lowercase letters as equivalent. '''

str=input("ENTER THE SENTENCE")
s=str.lower()
index=0
l=len(str)
p=l-1

while index <p:
    if(not(s[index]>='a' and s[index]<='z')):
        index+=1
    elif(not(s[p]>='a' and s[p]<='z')):
        p=p-1
    elif(s[index]==s[p]):
         index+=1
         p=p-1
         if index==p or index+1==p:
             print('palindrome')
    else:
        print('not palindrome')
        break
    

