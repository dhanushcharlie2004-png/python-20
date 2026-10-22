#while loop

#question 1

h=1
while h<=5:  # using while loop and print the 1 to 5.
    print(h)
    h+=1


#question 2

password= ""
while password!= "dhanush@123":
    password = input ("Enter your password:")

#question 3

num=12345
reverse=0
while num >0:
    digit= num%10
    reverse = reverse*10 +digit
    num=num//10
print("Reverse:", reverse)

#ANOTHER FORMAT OF REVERSING STRING IN WHILE LOOP
num=12345
reverse=0
while num>0:
    reverse,num = reverse*10+ num%10,num//10
print("Reverse:",reverse)
#Reverse: 54321

# SUM THE TOTAL NUMBER USING WHILE LOOP
num=4567
total=0
while num>0:
    total,num=total + num%10,num//10
print("total:",total)


#Password validation (Correct password enter pannura varaikkum password ask pannanum.)
password=""
while password != "hari@123":
     print("wroung password")
     password=input("enter the password:")
print("login successful")


#FIND THE FACTORIAL OF 5 USING WHILE LOOP
num=5
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print("factorial:", fact)
#factorial: 120

# COUNT DIGITS (987654-la ethana digits irukku-nu count pannanum.)
num=987654
count=0
while num>0:
    num=num//10
    count=count+1
print("digit count:", count)
#digit count: 6

