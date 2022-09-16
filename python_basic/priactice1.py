""" problem_01: Swapping two variables .
Two numbers will be taken as input as input and then they will be swapped and then the 
changed output will be displayed.

input:
a = 10
b = 20

after swapping :
a = 20 
b = 10


## problem_01(solution):

# a =10
# b =20
# print("Before swapping the value of a & b is " +str(a),str(b))

# temp = a
# a = b
# b =temp
# print("After swapping the value of a & b is " +str(a),str(b))

## Alternative way to solve problem_01:

# a = 10
# b = 20

# print("Before swapping the value of a & b is " +str(a),str(b))
# a,b =b,a
# print("After swapping the value of a & b is " +str(a),str(b))



problem_02: Solving a Quadratic equation with real solutions.

x^2-5x+6 = 0
x = 2,3
ax^2+bx+c = 0
x = solution ?

4-math.sqrt(2)


## problem_02(Solution):

# ax^2+bx+c = -b+-sqrt(b*b-4*a*c)/2*a
## We have to solve this equation : x^2-5x+6 = 0 #here a =1 ,b = -5 ,c =6

# from math import sqrt
# a = int(input("The value of a is : "))
# b = int(input("The value of b is : "))
# c = int(input("The value of c is : "))
# d = sqrt(b*b-4*a*c)
# x1 = (-b+d)/2*a
# x2 = (-b-d)/2*a

# print("The solution of x1 & x2  are " +str(x1),  str(x2))


problem_03: convertion celcius to farhenheit: 

Input will take a celcius temperature and will convert to farhenheit and will give the output
"""


## problem_03(solution): convertion celcius to farhenheit: c/5 = f-32/9 

#so farhenheit f = 9*c+160/5

celcius = int(input("Enter the value of celcius is : "))

farhenheit = (9*celcius+160)/5
print("The value of Farhenheit is : " +str(farhenheit))









