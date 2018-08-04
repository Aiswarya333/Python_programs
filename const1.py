'''VOWELS OR CONSONANTS - In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your
program should display a message indicating that the entered letter is a vowel. If the user enters y then yourprogram should display a message indicating that
sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating
that the letter is a consonant.'''

i=input('Enter a letter')

if (i=='a' or i=='i' or i=='e' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
     print('ENTERED LETTER IS A VOWEL')
elif (i=='y' or i=='Y'):
    print('Y IS A CONSONANT')
else:
    print('ENTERED LETTER IS A CONSONANT')
