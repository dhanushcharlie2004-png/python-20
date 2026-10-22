#function using return method
def add (a,b):
    return a+b
result=add(10,39)
print(result)

# function only use this program
def employee(name):
    print("enter my name:",name)
employee("dhanush")
#enter my name: dhanush

#default arugument using this function
def student(name="raj"):
    print("student name:" , name)
student()
# student name: raj

#keywords function
def student(name,age):
    print(name,age)
student(age=25,name="dhanush")
#dhanush 25

#positional function
def sum(a,b):
    print(a+b)     
sum(19,20)          # a=19 position automatically assign b=20 positon assign 


#variable length aruguments (*args)
# def add(*args):
#     print(sum(args))     # add multiple numbers  add(29,29,29,29,292,29) 
# add(33,22,30)

#(*args) (multiplication,subraction)
def mul(*args):
    result=args[0]*args[1]*args[2]
    print("multiplication:",result)
mul(20,30,40)
#multiplication: 24000

def sub(*args):
    result=args[0]-args[1]-args[2]
    print("sunstraction:",result)
sub(20,5,3)
#substraction: 12

#keywords variable length aruguments(**kwargs)
def name(**kwargs):
    print(kwargs)
name(name="raj",age=31,place="porur")
#{'name': 'raj', 'age': 31, 'place': 'porur'} 


#FUNCTION TYPE :

#BUILT-IN FUNCTIONS:
   # PRINT(), LEN(), TYPE(), MIN(), MAX() , SUM()

#USER-DEFINED FUNCTION:
def name(**kwargs):
    print(kwargs)              # user defined function start from (def) .
name(name="dhanush",age=21)

#RECURSIVE FUNCTIONS:
def countdown(s):
    if s==0:
        print("stop")
    else:
        print(s)
        countdown(s-1) # this line is recursive function.
countdown(5)

#LAMBDA FUNCTION

square=lambda a,b: a*b   # lambda is shorter way to write user defined function 
print(square(23,30))

def square (a,b): #this user defined function 
    print(a*b)
square(23,20)

