# EXCEPTION HANDLING
# WHY USE "TRY" - IT CONTAINS THE CODE WHICH MAY CAUSE IN OCCURS.
# WHY USE "EXCEPT" - IT HANDLES THE ERROR INCASE IF IT OCCURS . IT CAN'T STOP THE CODE CONTINUOUSLY RUN .

# FOR EXAMPLE PROGRAM :
try:
    num=int (input("enter your number:"))
    print(10/num)

except:
    print("error occured")    # ENTER THE CORRECT NUMBER AND SHOW THE CORRECT OUTPUT AND IT'S RUNS "TRY"
 
# enter your number:10
# 1.0

try:
    num=int (input("enter your number:"))
    print(10/num)
 
except:                   # ENTER THE WROUNG NUMBER AND IT'S RUN ON BOTH HANDLING LIKE "TRY" AND "EXCEPT"
    print("error occured")

# enter your number:0
# error occured


try:
    a=10
    b=0
    print(a/b)
except:
    print("a not divided b")


number=[10,20,30,40,50]
for num in number:
    try:
        print(num/10)     # output correct ah iruntha "try" matum excute agum.
    except:
        print("invalid")
        
# 1.0
# 2.0
# 3.0
# 4.0
# 5.0

number=[10,20,30,40,50]
for num in number:
    try:
        print(num/0)     # output wroung iruntha "except" run agum
    except:
        print("invalid ")
     
# invalid 
# invalid 
# invalid 
# invalid 
# invalid 


number=[10,20,30,40,30]
for num in number:
    try:
        print(num!=30)     # output  correct and wroung ah iruntha "try" and "except" both run agum.
    except:
        print("invalid")
        
# True
# True
# False
# True
# False

while True:
    try:
        num=int(input("enter number:"))   # using while with "try" and "except"
        print("your number:", num)
        break
    except ValueError:
        print("invalid value")
        
# enter number:10
# your number: 10
# enter number:bef
# invalid value
# enter number:20
# your number: 20


numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index: "))     # index value 
    print(numbers[index])  

except IndexError:
    print("Index not found")


values = ["10", "20", "hello", "40", "abc"]
for value in values:
    try:
        num = int(value)
        print(num)
    except ValueError:
        print("Invalid value:", value)

# 10
# 20
# invalid value: hello
# 30
# invalid value: abc