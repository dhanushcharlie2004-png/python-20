#Find even or odd numbers

number=int(input("enter:"))
enter:10
if number%2==0:
    print("even")
else:
    print("odd")

#Find the largest of 2–3 numbers

number=[20,40,50,70,80]
largest=number[0]
for i in number:
    if i>largest:
        largest=i

print("largest number:", largest)
#largest number: 80
