#1.using the reduce function find out the sum of all elements in a list:
#lst = [5,10,15,20]
  #to use reduce write - 
  #from functools import reduce (import the reduce function)

#2. Write lambda to calculate the sum of two numbers.
z=lambda x,y:x+y
print(z(1,2))
#3.create a lambda that will return 'yes' if the given number is even and No if the given number is odd
#4.retrieve odd numbers from given list of numbers using suitable lambda function.
lst=[10,2,3,5,7,13,4,8]
     
result=list(filter(lambda x:x%2!=0,lst))
print(result)     
#5.given list of numbers using suitable function add 1 to each element.
  #l1=[2,4,5,6]
#6.write a program to demostrate use of function argument types.
def func(x):
    x=8
    print("x is:",x)
func(6)    
 
#7.Demonstrate with an example how functions can be passed as parameter to another function.
def display(fun):
    return 'hey ' + fun

def name():
    return 'janu'


def show():
    return  'how are you ?'


print(display(name()))
print(display(show()))

