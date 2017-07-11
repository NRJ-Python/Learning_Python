#
# Example file for working with functions
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
#Define a function
def func1():
    print("I am a function")
func1()
print (func1())#Invokes function and then gives output none too as there is no return value
print (func1) #Prints the value of the function
#Functions that take arguments
def func2(arg1,arg2):
    print(arg1," ",arg2)
func2(10,20)
print (func2(10,20)) #Still prints none too as there is no return value
#function that returns a value
def cube(x):
    return x*x*x
print (cube(3))#Returns 27   
#Functions with default value of argument
def power(num,x=1):
    result=1;
    for i in range(x):
        result=result*num
    return result
print(power(2))
print(power(2,3))
print(power(x=3,num=2))