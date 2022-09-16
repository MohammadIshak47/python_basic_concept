# for i in "Myblog":
#          print (i, '?')
# a = ['tomato','cucumber','onion','potato','gourd']
# print(type(a))
# for item in a:
#     print(item)
    
# a = {'name':'Mohammad Ishak','nickname':'Ishak','profession':'student','gender':'male'}
# print(type(a))
# for item in a:
#     print(item)

# a ='python'
# for item in a:
#     print(item)

# a = ['Bangladesh','Pakistan','Afganistan','Saudi Arab']

# for item in a:
#     print(list(item)) 

# print(list(range(2,33)))

##Loop statement : break continue pass

## break __ statement

# for i in range(3,43):
#     if i ==9:
#         break
#     print(i)

## continue __statement:

# for number in range(2,77,6):
#     if number == 52:
#         continue
#     print(number)

#### pass_statement(null)
# for number in range(3,44):
#     if number == 3:
#         pass
#     print(number)


# n = 1

# while n<=10:
#     print(n)
#     n = n+1
# else:
#     print("Your Loop is over") 

# for i in range(2,23):
#     print(i)
#     i = i+1   

# else:
#     print("Your while loop is over")
"""
##while loop

# n = 1
# while n<=20:
#     print(n)
#     n = n+1

problem_01: 1+2+3+4......+100

Solution: 
n =1
temp = 0
while n<=100:
    temp = temp+n
    n = n+1
print(temp)

alternative way:
n=100
temp = (n*(n+1))/2
print(temp)

problem_02: 1+3+5+7+...+97=?

Solution:
n = 1
temp =0
while n<=97:
    temp = temp+n
    n = n+2
print(temp)   

alternative way:

temp = 0
for i in range(1,98,2):
    temp = temp+i
    i = i+2
print(temp)    
    
n = 97

a = 1
d = 2
temp = (n/2)*((2*a)+((n-1)*d))
print(temp)


problem_03:Write a program to print first 10 even numbers in reverse order.
 
Solution:
for i in range(10,0,-2):
    print(i)

problem_04: Write a program to print table of a number accepted from user.

Solution : 
 num = input("Enter any number : ")
for i in range(1,11):
    print("The exact number is ",num*i) 
    
problem_05: Write a program where take any integer input and Find out those numbers multiplication table.

solution:
number = int(input("Enter any number : "))
count = 1

for count in range(1,11):
    print("Multiplication table of ",number,'*',count,'=',number*count)
    count = count+1

# while count<=10:
#     print("The multiplication of ",number,'*',count, '=',number*count)
#     count = count+1  

problem_06: 1 to 100 numbers where dvisible by 3 and not dvisible by 5 and show their output in list.

solution :
my_list = []

for i in range(1,101):
    if i%3==0 and i%5!=0:
        my_list.append(i)
print(my_list) 

problem_07: Given 13,34,40,66,88,33,21,23,43,83,99,112,12,23,32,98,45.Show the output in list order below 50 
 
Solution:
a = [13,34,40,66,88,33,21,43,83,99,112,12,23,32,98,45]
my_list = []

for i in a:
    if i<50:
        my_list.append(i)
print(my_list) 

problem_08:  Given 44,22,33,33,54,34,42,99,78,43,44,22,12,98,12,89,67,76,33,21,32,34,29,99.
remove all duplicates value from this list and show their output in list.

Solution : 
a = [44,22,33,32,33,54,42,99,78,43,22,12,98,12,89,67,76,33,21,32,34,29,99]
my_list = []

for i in a:
    if i  not in  my_list:
        my_list.append(i)
print(my_list) 

problem_09: Simple pyramid pattern.
*
**
***
****
*****

Solution:
height = 5
for i in range(height+1):
    print(i*'*')
    

problem_10:Simple pyramid pattern. 

*
***
*****
*******   
solution :
height = 4

for i in range(height+1):
    print((2*i-1)*"*") 
    
problem_11: 
    *
   **
  ***
 ****
*****

solution:

height = 5

for row in range(1,height+1):
    print(" " * (height -  row) +"*" * row)
    
problem_12: Input a number or word and show us your taken number or word palindrome  or not .
Note : Palindrome means if you reverse the word or number it will be same . Such as 707 reverse number
will be 707 or madam word. it will be also madam.

Solution : 
print("Please input your desired word or number .")

word  = input()
word  = word.casefold()
reverse_word = word[::-1]

if word == reverse_word:
    print("wow!it's palindrome")
else:
    print("Lol! it's not palindrome")
    
problem_13: Given a list lower to upper . 1,3,5,7,11,13,15,17,20,26,31,44,54,56,65,77,94,100.
Take a input and search from the list is your input number in the list or  not.  

Solution:

my_list = [1,3,5,7,11,13,15,17,20,26,31,44,54,56,65,77,94,100]

number = int(input("Enter your desired number : "))

first = 0
last =  len(my_list)-1
found = False
cycle = 0

while first <= last and not found:
    midpoint = (first+last)//2
    if my_list[midpoint] == number:
        found = True
    else:
        if my_list[midpoint]>number:
            last = midpoint-1
        else:
            first = midpoint+1
    cycle = cycle+1
print("Found after", ,'cycle')

problem_14: Given A = {1,2,3,4,5} & B = {5,6,7,8} set. Findout  mentioned sets union and intersection
without using union() and intersection() function .

Solution : 
 
 

problem_15:Write a program to find the factorial of a number.

Solution:
number = int(input("Enter your desired value : "))
fact =1

for i in range(1,number+1):
    fact = fact*i
print('Your desired',number,'! =',fact) 

alternative way:

import math
num = int(input("Enter your number : "))
fact = math.factorial(num)
print("Your desired result is ",fact)          

problem_16:Write a program to find the sum of the digits of a number accepted from user

Solution: 
# num=int(input("Enter any number"))
# s=0
# while(num):
#    r=num%10
#    s=s+r
#    num=num//10
# print("Sum of digits is",s)

num = input("Enter any number : ")
sum = 0
for i in num:
    sum = sum+int(i)
    
print("The number of the sum is ",sum)

problem_17:Write a program to check whether a number is prime or not.

Solution:
    num = int(input("Enter any number : "))
p = False

for i in range(2,num):
    if num%i == 0:
        p = True
        break
if p:
    print(num," is not a prime number")
else:
    print(num," is prime number") 
    
#for i in (1,10):
       print(i) 
            
#for i in range(2,7):
       print(i)
#for i in "csiplearninghub":
       print(i)
       
#for i in "python":
       print(i, end=' ')
       
#x=5
while(x<15):
  print(x**2)
  x+=3  
##problem_18:
1

1 2

1 2 3

1 2 3 4  

Solution:num = '1234'

x = "  "

for i in num:
    x = x+i
    print(x)
   
problem_20:

* * * *

* * *

* *

*

solution: 
height = 4

for i in range(5,1,-1):
    print((i-1)*"*")
    
problem_20:Accept 10 numbers from the user and display their average.

solution : 
f = 0

for i in range(10):
    f = f+i
avg = f/10
print("Average of 10 numbers ",avg) 

alternative way:
s=0

for i in range(10):
 n=int(input("Enter number"))
s=s+n

print("Average of 10 numbers is ",s/10)   
    
    
problem_21:Write a program to print all prime numbers  that fall between two numbers 
including both(accept two numbers from the user)

Solution: 
lower_num = int(input("Enter your lower number : "))
upper_num = int(input("Enter your upper number : "))
print('Your expected prime number' ,lower_num,'to',upper_num, 'are')

for num in range(lower_num,upper_num+1):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
          print(num)


problem_22:Write a program to display sum of odd numbers and even numbers that
fall between 12 and 37(including both numbers)          

solution :

minimum_value = int(input("Enter your minimum value : "))
maximum_value = int(input("Enter your maximum value : "))

even_total = 0
odd_total =  0

for number in range(minimum_value,maximum_value+1):
    if (number%2 == 0):
        even_total = even_total+number
    else:
        odd_total = odd_total+number

print("The sum of Even numbers 12 to 37  {1}".format(number,even_total))  
print("The sum of Odd numbers 12 to 37  {1}".format(number,odd_total))          

problem_23:Write a program to display all the numbers which are 
divisible by 11 but not by 2 between 100 and 500.

solution: 
for i in range(100,500):
    if i%11==0 and i%2!=0:
        print(i)

problem_24:Write a program to print numbers from 1 to 20 except multiple of 2 & 3.

solution :
for i in range(1,21):
    if i%2!=0 and i%3!=0:
        print(i)
        

problem_25:Write a program to print table of a number(accepted from user) in the following format. 

    Like : input number is 7, so expected output  is

    7 * 1 = 7

    7 * 2 = 14 and so on
    
solution:
number = int(input("Enter your desire number : "))

for i in range(1,11):
   
  print(number,'*',i,'=',number*i)
  
problem_26: Write a program that keep on accepting number from the user until 
user enters Zero. Display the sum and average of all the numbers.

solution : 

num=1

i=-1

s=0

while(num!=0):

   num=int(input("Enter any number"))

   s=s+num

   i=i+1

print("Average of numbers entered by you is ",s/i)  


problem_27:. Write a program to print the following pattern

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1           
 
solution :
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end = '')
    print() 
    
problem_28:    
                                     
"""
 

       

    



    
    





   
        



    

    

    



   
    
   
           


  



   
  

                    



   





            

       

    

    
    

    
    
    

    


    



 



