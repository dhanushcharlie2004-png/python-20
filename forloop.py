#question 1

numbers =[1,-2,3,-4,5]   # neagative numbers count panna usin for loop and if coundition
count=0
for i in numbers:        #output : negative numbers : 2 
    if i<0: 
        count+=1         # count+=1 vanthu add panna bodhu negative numbers vantha increase agum. count=-2+1 =-1 apa onu increase agum.
print("negative numbers:",count)

#question 2 

numbers = [1,-2,3,-4,5]  #positive numbers count panna using for loop and if condition.
count=0
for i in numbers:        # output: positive numbers: 3
    if i>0:
        count +=1
print("positive numbers:", count)

#question 3

string="education"    # vowels letters yathana irukku nu count panni irukka .using for loop and if condition
count=0                # string la yathana vowels letters irukku nu count panni solum.
for i in string:
    if i.lower() in "aeiou":
        count+=1
print("vowels letters count:", count)

string="education"     # another format of vowels . string la irukka vowels letters ahh matum print pannum.
for i in string:
    if i.lower() in "aeiou":
        print(i)


#question4

numbers=[3,5,7,2,8,1,4]   # find the largest number using for loop
for i in numbers:
    if i>7:
        print(i)

numbers=[10,25,8,45,30]   # find the largest number using for loop
for i in numbers:
    if i>44:
        print(i)


numbers=[10,25,8,45,30]  # another format of find largest number using for loop
largest=numbers[0]  
for i in numbers:
    if i>largest:
      largest =i
print("largest numbers:",largest)

numbers=[3,5,7,2,8,1,4]    # find the largest number and count the largest numbers
largest=numbers[0]         # using for loop , count and if conditions
for i in numbers:
    if i>largest:
        largest =i
        count=0
for i in numbers:
        if i==largest:
         count+=1
print("largest number count:",largest)
print("count:",count)


#question 5

num =5
fact=1                 # calculate the factorial number of 5 using for loop
for i in range(1,num+1):
    fact =fact *i
print("factorial:",fact)


#question 6

my_list=[1,-2,3,-4,5,-6,-7]   # skip  the negative numbers . so, using for loop and continue
for i in my_list:
    if i<0:
        continue
    print(i)


# question 7

mylist = [1,2,3,4,5,6,7,8,9]  # using for loop and break keyword.
for i in mylist:
    if i==5:
        break
    print(i)

mylist = [1,2,3,4,5,6,7,8,9]  
for i in mylist:
    if i==6:
        break
    print(i)