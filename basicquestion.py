# #Find even or odd numbers

# number=int(input("enter:"))
# #enter:10
# if number%2==0:
#     print("even")
# else:
#     print("odd")

# #Find the largest of 2–3 numbers

# number=[20,40,50,70,80]
# largest=number[0]
# for i in number:
#     if i>largest:
#         largest=i

# print("largest number:", largest)
# #largest number: 80

# #FIND POSITIVE AND NEGATIVE NUMBER
# numbers=[20,30,-19,-20,0]
# for i in numbers:
#     if (i>0):
#         print("positive ")
#     elif (i<0):
#         print("negative")
#     else:
#         print("zero")
    
# # positive 
# # positive 
# # negative
# # negative
# # zero

# #ANOTHER METHOD OF FIND POSITIVE AND NEGATIVE NUMBER

# i=int(input("enter number:"))
# #enter number:10
# if (i>0):
#     print("positive")
# elif (i<0):
#     print("negative")
# else:
#     print("zero")

# #positive

# # PRINT NUMBERS SEQUENCE
# for i in range(1,11):
#     print(i) 
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 10


# for i in range(10,21,2):  # START , STOP , STEP METHOD
#     print(i)
  
# # 10
# # 12
# # 14
# # 16
# # 18
# # 20

# for i in range(10,0,-1): #START , STOP, STEP METHOD FOR REVERSE NUMBERS
#     print(i)

# # 10
# # 9
# # 8
# # 7
# # 6
# # 5
# # 4
# # 3
# # 2
# # 1

# # CALCULATE SUMS AND FACTORIALS

# num=5
# factorial=1
# for i in range (1,num+1):
#     factorial=factorial*i

# print("factorial:",factorial)
# # factorial: 120

# num=7
# factorial=2
# for i in range(2,num+1):
#     factorial=factorial*i

# print("factorial:",factorial)
# # factorial: 10080

# num=int(input("enter number:"))  #find the factorial . give the input any number. print the factorial value of number.
# # enter number:9
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i

# print("factorial:", factorial)
# # factorial: 362880

# total=0
# for i in range(1,6):  # calculate sums and using for loop 
#     total=total+i
    
# print("Total number:", total)
# # Total number: 15

# #COUNT DIGITS BUT USING "INPUT" CONCEPT
# num=int(input("enter number:"))
# # enter number:1289
# count=0
# while num>0:
#     num=num//10
#     count=count+1
 
# print("count digits:",count)
# # count digits: 4

# #COUNT DIGITS
# num=98365463
# # count=0
# while num>0:
#     num=num//10
#     count=count+1

# print("count digits:",count)
# # count digits: 8

num=int(input("enter number:"))
reverse=0
while num>0:     # 12345 >0
    digit=num%10    # 12345%10 = 1234.5
    reverse=reverse*10 + digit  #0*10+ 1234.5 = 5
    num=num//10    # 12345//10= 1234 remove (5) because using floor division is remove the deciaml point remove.
print("reversed number:",reverse)
