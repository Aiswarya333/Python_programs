'''AVERAGE - In this exercise you will create a program that computes the average of a collection of values entered by the user. The user will enter 0 as a sentinel
value to indicate that no further values will be provided. Your program should display an appropriate error message if the first value entered by the user is 0.
Hint: Because the 0 marks the end of the input it should not be included in the average.'''

sum=0
c=0
num=1

while num!=0:
    num=int(input('enter numbers'))
    sum=sum+num
    c+=1
avg=sum/(c-1)
print('Average is %.2f' %avg)


    

