#if and else condition
age=20
if age>= 18:
    print("eligible")    #condition correct so , output is eligible
else:
    print("not eligible") 

age = 20
if age<=18:
    print("eleigible")   #condition is incorrect.so, not eligible
else:
    print("not eligible")


#elif condition
marks = 65
if marks>=85:
    print("excellent")
elif marks>=70:
    print(" very good") 
elif marks>=65:
    print ("good")
else:
    print("fail")


# nested if condition
age=10
driving_lic ="yes"
if (age>=18):
    if (driving_lic =='yes'):
        print ("you are allowed")
    else:
        print("apply licence")
else:
    print("you are not allowed")

    