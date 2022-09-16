# a = input("Please enter a number: ")
# b = input("Please, enter a number :")

# if a>b:
#     print(" A is greater than B")
# elif a<b:
#     print("B is greater than A")
# elif a == b:
#     print("A & B both are equal")
# else:
#     print("Not a valid number")   


"""1.Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.
Solution:
number = int(input("Enter a number : "))
id  = number%10
if id%3==0:
    print("The number you have entered is disvisible")
else:
    print("The number you have entered is not disvisible")
    
    
problem_02: Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
between 1500 and 2700 (both included). 

solution : 

number = int(input("")) 


problem_03:Write a program to check whether a person is eligible for voting or not. (accept age from user)

Solution : 
age = int(input("Enter your age :"))
if age>=18:
    print("The person is eligible for voting")
else:
    print("The person is not eligible for voting")  
 
 
problem_04:Write a program to check whether a number entered by user is even or odd. 

solution :
number = int(input("Enter your number :"))

if number%2==0:
    print("The number is even")
else:
    print("The number is odd")  
    
problem_05:Write a program to check whether a number is divisible by 7 or not.

Solution:
number = int(input("Enter your number : "))
if number%7==0:
    print("7 is disvisible")
else:
    print("7 is not disvisible")

problem_06:Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.

Solution :
num = int(input("Enter a number :"))
id = num%10
if id%3==0:
    print("The Last digit of number is divisible by 3")
else:
    print("The Last digit of number is Not divisible by 3")

 problem_07: Write a program to display the last digit of a number.
(hint : any number % 10 will return the last digit)

Solution :
num = int(input("Enter your number : ")) 

id = num%10
print("The Last digit of the number is : " +str(id))
    
        
    
problem_07:Write a program to display "Hello" if a number entered by user is a multiple of five , 
otherwise print "Bye".(Here, multiple of five means disvisible by 5)

Solution:
num = int(input("Enter your number : "))
if num%5==0:
    print("Hello")
else:
    print("Bye")

 
            


problem_10: Write a program to accept percentage from the user and display the grade according
to the following criteria: 
         Marks                                      Grade
         > 90                                         A
         > 80 and <= 90                               B
         >= 60 and <= 80                              C
         below 60                                     D

Solution :

marks = int(input("Enter your marks : "))

if 90<marks<=100:
    print("You have got A grade")
elif 80<marks<=90:
    print("You have got B grade")
elif 60<=marks<=80:
    print("You have got B grade")
elif marks<60:
    print("You have got D grade")
elif 0>marks>100:
    print("Invalid number")
else:
    print("You have failed") 
    
problem_08:Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
    Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000) 



Solution :
units = int(input("Total number of using units : "))
bill = 0

if units<=100:
    bill =units*0
elif 100<units<=200:
    bill = 100*0+(units-100)*5
elif units>200:
    bill = 100*0+100*5+(units-200)*10        

print("Your total electricity bills : ", bill) 

problem_10: Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        Cost price (in Rs)                                       Tax
        > 100000                                                  15 %
        > 50000 and <= 100000                                     10%
        <= 50000                                                  5%

Solution :

cost_price = int(input("Enter your cost price : "))
tax = 0
if cost_price>100000:
    tax = cost_price*(15/100)
elif 50000<cost_price<=100000:
    tax = cost_price*(10/100)
else :
    tax = cost_price*(5/100)
print("Total amount of Tax is " +str(tax)) 

           
   
problem_11: Write a program to check whether an years is leap year or not.
 
 solution :
 year = int(input("Enter your year :"))
if year%4==0:
    print("Leap year")
elif year%400==0 and year%100!=0:
    print("Leap year")
else:
    print("Not a leap year")
              

problem_12:Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday 
, 2 for Monday and so on. 

solution:
day = int(input("Enter your day : "))
if day ==1:
    print("Today is Saturday")
elif day ==2:
    print("Today is Sunday") 
elif day ==3:
    print("Today is Monday")
elif day ==4:
    print("Today is Tuesday")
elif day ==5:
    print("Today is Wednesday")
elif day ==6:
    print("Today is Thusday")
elif day ==7:
    print("Today is Friday")
else:
    print("It's not a valid day")  
    
problem_13:Write a program to accept a number from 1 to 12 and display name of the month and 
days in that month like 1 for January and number of days 31 and so on. 

Solution :

month = int(input("Enter your month : "))
if month ==1:
    print("January month and 31 days has January")
elif month ==2:
    print("February month and 28 days has February and in Leap Year it has 29 days")
elif month ==3:
    print("March month and 31 days has March")
elif month ==4:
    print("April Month and 30 days has April")
elif month ==5:
    print("May month and 31 days has May")
elif month ==6:
    print("June month and 30 days has June")
elif month ==7:
    print("July month and 31 days has July")
elif month ==8:
    print("August month and 31 days has August")
elif month ==9:
    print("September month and 30 days has September")
elif month ==10:
    print("October month and 31 days has October")
elif month ==11:
    print("November month and 30 days has November month")
elif month ==12:
    print("December month and 31 day has December")
else:
    print("It's not valid number") 
    
problem_14:Accept any city from the user and display monument of that city.
                  City                                 Monument
                  Delhi                               Red Fort
                  Agra                                Taj Mahal
                  Jaipur                              Jal Mahal  
                  
Solution :
city = input("Enter your city name : ")


if city.lower() == "delhi":
    print("Your extract Monument is Red Fort")
elif city.lower() ==  "agra":
    print("Your extract Monument is Taj Mahal")
elif city.lower() == "jaipur":
    print("Your extract Monument is Jal Mahal")
else:
    print("Your entered Monument is not valid")
                      
problem_15:10. Write the output of the following if a = 9
        
    if (a > 5 and a <=10):    
         print("Hello")    
    else:    
        print("Bye")

Solution :
a = int(input("Enter your number : "))

if 5<a<=10:
    print("Hello")
else:
    print("Bye") 
    
problem_16: Write a program to check whether a number entered is three digit number or not

Solution:
num = len(input("Enter your number : "))

if num ==3:
    print("Your expected number of digit is : " +str(num))
else:
    print("The number you have entered is not 3 digit")
    

alternative way:

num1 = (input("Enter any number")
l=len(num1)
if l != 3:
     print("Enter three digit number")
else:
     print("Middle digit is ",(int(num1)%100//10)) 
     

problem_17: Write a program to check whether a person is senior citizen or not.

Solution:
age = int(input("Enter your age : "))

if age == 60:
    print("Senior citizen")
else:
    print("Not senior citizen")  
    
problem_18:Write a program to find the largest number out of two numbers excepted from user.

Solution :
num1 = int(input("Enter your number1 : "))
num2 = int(input("Enter your number2 : "))

if num1>num2:
    print(str(num1)+" is greater than "+str(num2))
elif num1<num2:
    print(str(num2)+" is greater than "+str(num1))
else:
    print("Both numbers are equal")


problem_19:Write a program to check whether a number (accepted from user) is positive or negative.

Solution:
num = int(input("Enter your number : "))

if num>0:
    print(str(num)+" is Positive number ")
else:
    print(str(num)+" is Negative number") 


problem_20:Write a program to check whether a number is even or odd.

Solution:
num = int(input("Enter your number : "))

if num%2==0:
    print("Even number")
else:
    print("Odd number") 
    
problem_21:Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

Solution :
num = int(input("Enter your number : "))

if num%2==0 and num%3==0:
    print("The number is divisible by 2 and 3 ")  
else:
    print("Not divisible")  
    
problem_22: Accept the temperature in degree Celsius of water and 
check whether it is boiling or not (boiling point of water in 100 oC.

Solution:
temperature = int(input("Enter your temperature : "))

if temperature>=100:
    print("The water is Boiling")
else:
    print("water is not boiling")  
    
problem_23: Accept the age of 4 people and display the youngest one?    
                             
Solution :
person1 = int(input("Enter age of Person1 : "))
person2 = int(input("Enter age of Person2 : "))
person3 = int(input("Enter age of Person3 : "))
person4 = int(input("Enter age of Person4 : "))

if person2>person1<person3 and person1<person4:
    print("The youngest one of Person1 age is " +str(person1))
elif person1>person2<person3 and person2<person4:
    print("The youngest one of Person2 age is " +str(person2))
elif person1>person3<person2 and person3<person4:
    print("The youngest one of Person3 age is " +str(person3)) 
elif person1>person4<person2  and person4<person3:
    print("The youngest one of Person4 age is " +str(person4))  
else:
    print("Not valid number")
    
problem_25:Write a program to check whether a number  is prime or not.

Solution :
num = int(input("Enter your number : "))
flag = False

if num>1:
    for i in range(2,num):
        if num%i == 0:
            flag = True
            break

if flag:
    print(str(num)+" , Not a prime number")
                
else:
    print(str(num)+ " , is prime number") 
    
alternative way:
k=0
num1 = int(input("Enter any number"))
if num1 == 0 or num1 == 1:
     k=1
for i in range(2,num1):
     if num1%i == 0:
          k = 1
if k==1:
     print("number is not prime")
else:
     print("number is prime") 
     

problem_26:Write a program to check a character is vowel or not.

Solution : 
ch = input("Enter any character : ")
vowel ="aAeEiIoOuU"
if ch in vowel:
    print("Vowel")
else:
    print("Consonant")    

problem_27:Accept the following from the user and calculate the percentage of class attended:

a.     Total number of working days

b.     Total number of days for absent

    After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam.       

solution:
total_working_days = int(input("Enter your total working days : "))
total_absent_days =  int(input("Enter your total absent days : "))
total_class_attendence = (total_working_days - total_absent_days)/total_working_days*100
print("Percentage of class attendence is" , total_class_attendence)
if total_class_attendence<75:
    print("Student will not be able to sit in the exam")
else:
    print("Student will  be able to sit in the exam")
    
problem_28:Accept the percentage from the user and display the  grade according to the following criteria:
        Below 25 —- D
        25 to 45 —- C
        45 to 50 —- B
        50 to 60 –– B+
        60 to 80 — A
        Above 80 –- A+

Solution :
marks = int(input("Enter your marks : "))

if 0<marks<25:
    print("Your grade is D")
elif 25<=marks<45:
    print("Your grade is C")
elif 45<=marks<=50:
    print("Your grade is B")
elif 50<marks<=60:
    print("Your grade is B+")
elif 60<marks<80:
    print("Your grade is A")
elif 80<=marks<=100:
    print("Your grade is A+")
else:
    print("Not valid marks") 
    
problem_29: A company decided to give bonus to employee according to following criteria:

    Time period of Service                Bonus

    More than 10 years             10%

    >=6 and <=10                   8%

    Less than 6 years              5%

    Ask user for their salary and years of service and print the net bonus amount.
    
Solution :
salary = int(input("Enter your Salary : "))
years_of_service = int(input("Enter your service year : "))

net_bonus_amount = (salary*years_of_service)/100

if years_of_service>10:
    print("Your Net Bonus Amount is ", net_bonus_amount)
elif 6<=years_of_service<=10:
    print("Your Net Bonus Amount is ", net_bonus_amount)  
elif 0<years_of_service<=5:
    print("Your Net Bonus Amount is ", net_bonus_amount)
else:
    print("Please, enter valid service year!")  
    
problem_30:Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:
Marked Price	Discount
>10000	            20%
>7000 and <=10000	15%
<=7000	            10% 

Solution:
marked_price = int(input("Enter your marked price : "))
   


if marked_price>10000:
    discount = marked_price*(20/100)
if 7000<marked_price<=10000:
    discount = marked_price*(15/100)
if 0<marked_price<=7000:
    discount = marked_price*10/100
net_amount = marked_price-discount 

print("Your net amount is ", net_amount) 

alternative way:
na=0
d=0
mp=int(input("Enter marked price"))
if mp > 10000:
     d = 20/100*mp
if mp > 7000 and mp <= 10000:
     d = 15/100*mp
if mp <= 7000:
     d = 10/100*mp
na = mp-d
print("Net amount to pay ", na) 


problem_31: Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

Note :

An equilateral triangle is a triangle in which all three sides are equal.

A scalene triangle is a triangle that has three unequal sides.

An isosceles triangle is a triangle with (at least) two equal sides.

Solution:


a_angle = int(input("Enter your a_angle size : "))
b_angle = int(input("Enter your b_angle size : "))
c_angle = int(input("Enter your c_angle size : "))

if a_angle == b_angle == c_angle:
    print("Your triangle is An equilateral")
elif (a_angle == b_angle and b_angle!=c) or (a_angle==c_angle and a_angle!=b_angle) or (b_angle==c_angle and b_angle!=a_angle):
    print("Your triangle is An isosceles")
elif a_angle!=b_angle!=c_angle:
    print("Your triangle is A scalene ")  
else:
    print("Not valid value") 
    

problem_32: Write a program to accept two numbers and mathematical operators and perform operation accordingly.

Like:

Enter First Number: 7

Enter Second Number : 9

Enter operator : +

Your Answer is : 16

solution:
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your Second number : "))
operator = input("Enter your operator : ")

if operator == '+':
    print("Your expected result is =",num1+num2)
if operator == '-':
    print("Your expected result is =",num1-num2)
if operator == '*':
    print("Your expected result is =",num1*num2)
if operator == '/':
    print("Your expected result is =",num1/num2)
if operator == '%':
    print("Your expected result is =",num1%num2)
if operator == '**':
    print("Your expected result is =",num1**num2)
if operator == '//':
    print("Your expected result is =",num1//num2)
       

problem_33:Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly

     Age	   Sex	Wage/day
>=18 and <30	M	700
	            F	 750
>=30 and <=40	M	800
	            F	850
Python if else

If age does not fall in any range then display the following message: “Enter appropriate age”       
    
Solution:
age = int(input("Enter your age : "))
sex = input("Enter your sex(M/F)  : ")
days = int(input("Enter your number of days : "))

if 18<=age<30 and sex.lower() =='m':
    print("Your expected wage is ", 700*days)
elif 18<=age<30 and sex.lower() =='f':
    print("Your expected wage is ",750*days) 
elif 30<=age<=40 and sex.lower() =='m':
    print("Your expected wage is ",800*days) 
elif 30<=age<=40 and sex.lower() =='f': 
    print("Your expected wage is ",850*days)
else:
    print("Please, enter appropiate age") 
    
problem_34:Accept three numbers from the user and display the second largest number.

Solution :

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))

if (num1>num2 and num1<num3) or (num1<num2 and num1>num3):
    print("The second largest number is ",num1)
if (num2>num1 and num2<num3) or (num2<num1 and num2>num3):
    print("The second largest number is : ", num2)
if (num3>num1 and num3<num2) or (num3<num1 and num3>num2):
    print("The second largest number is ", num3)
    
problem_35:Accept three sides of triangle and check whether the triangle is possible or not.

(triangle is possible only when sum of any two sides is greater than 3rd side)

Solution :              
angle_num1 = int(input("Enter first angle of triangle : "))
angle_num2 = int(input("Enter second angle of triangle : "))
angle_num3 = int(input("Enter third angle of triangle : "))

if (angle_num1+angle_num2 > angle_num3) and (angle_num1+angle_num3>angle_num2) and (angle_num2+angle_num3 > angle_num1):
    print("The Triangle is possible with these angles")

else:
    print("Angle is not possible")
    
    
Problem_36:Accept the marks of English, Math and Science, Social Studies Subject and display the stream allotted according to following

All Subjects more than 80 marks —       Science Stream

English >80 and Math, Science above 50 –Commerce Stream

English > 80 and Social studies > 80    —   Humanities


Solution : 
english_marks = int(input("Enter your english subject marks : "))
math_marks = int(input("Enter your math subject marks : "))
science_marks = int(input("Enter your science subject marks : "))
social_studies_marks = int(input("Enter your social studies marks : "))

if english_marks>80 and math_marks>80 and science_marks>80 and social_studies_marks>80:
    print("You have selected for Science stream")
elif english_marks>80 and math_marks>50 and science_marks>50:
    print("You have selected for Commerce stream")
elif english_marks>80 and social_studies_marks>80:
    print("You have selected for Humanities stream")
    
problem_37:Accept the kilometers covered and calculate the bill according to the following criteria:

First 10 Km              Rs11/km

Next 90Km               Rs 10/km

After that               Rs9/km

Solution : 

covered_km = int(input("Enter your covered kilometers : "))
bill = 0
if 0<covered_km<=10:
    bill = covered_km*11
if 10<covered_km<=100:
    bill = 10*11+(covered_km-10)*10
if covered_km>100:
    bill = 10*11+90*10+(covered_km-100)*9
print("Your net bill is : " , bill) 


alternative way :
kmc = int(input("Enter the kilometer covered"))

if kmc <=10 :

    amt = kmc * 11

elif kmc > 10 and kmc <= 100:

    amt = 110 + (kmc - 10)*10

elif kmc > 100:

    amt = 1010 + (kmc - 100)*9

print("Total amount to pay is ", amt)

problem_38:Accept the number of days from the user and calculate the charge for library according to following :

Till five days : Rs 2/day.

Six to ten days  : Rs 3/day.

11 to 15 days  : Rs 4/day

After 15 days    : Rs 5/day

solution :
days = int(input("Enter your number of days: "))
charge = 0

if days<=5:
    charge = days*2
elif 6<=days<=10:
    charge = days*3
elif 11<=days<=15:
    charge = days*4
elif days>15:
    charge = days*5
    
print("Your library charge : ", charge)                


problem_39:Accept the electric units from user and calculate the bill according to the following rates.

First 100 Units     :  Free

Next 200 Units      :  Rs 2 per day.

Above 300 Units    :  Rs 5 per day.

if number of unit is 500 then total bill = 0 +400 + 1000 = 1400

Solution : 
units = int(input("Enter your total electric units : "))
bill = 0

if units<=100:
    bill = units*0
elif 100<units<=300:
    bill = 100*0+(units-100)*2
elif units>300:
    bill = 100*0+200*2+(units-300)*5
print("Your Total electric bill according to units : ", bill)

alternative way :
ut = int(input("Enter number of units"))

if ut <=100:

     amt = 0

elif ut >100 and ut <= 300:

     amt = (ut-100) *2

else:

     amt = 400 + (ut - 300)*5

print("Total amount to pay is ", amt)


 
 Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)   
                    
"""
           
           


   
            






            
    


  
             




                    
        


        
    
  

       
  
          

                       



    




   


        
  

  


   



  
        


  



    
    

   





               
     



    
                             
    
    

        
      
                     

 
           

    


            


       


          
  
    
     
  
        

             