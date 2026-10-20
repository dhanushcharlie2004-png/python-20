#list multiple values remove and using for loop

mylist=["hari","ashiq","dhanush","harish","hari","hendry"]
remove_values=["hari","harish","hendry"]

for i in remove_values:
    mylist.remove(i)
    print(i)
print(mylist)

#append
mylist=["dhanush","hari","harish","ashiq"]
print(mylist.append("hendry"))
# None
print(mylist)
# ['dhanush', 'hari', 'harish', 'ashiq', 'hendry']

#extend
print(mylist.extend(["nasir","naveen","gokul"]))
# None
print(mylist)
# ['dhanush', 'hari', 'harish', 'ashiq', 'hendry', 'nasir', 'naveen', 'gokul']

#insert
print(mylist.insert(4,"sanjay"))
# None
print(mylist)
# ['dhanush', 'hari', 'harish', 'ashiq', 'sanjay', 'hendry', 'nasir', 'naveen', 'gokul']

#pop
print(mylist.pop())
# gokul
print(mylist.pop(3))
# ashiq
print(mylist)
# ['dhanush', 'hari', 'harish', 'sanjay', 'hendry', 'nasir', 'naveen']

#remove
print(mylist.remove("hari"))
# None
print(mylist)
# ['dhanush', 'harish', 'sanjay', 'hendry', 'nasir', 'naveen']

#count
print(mylist.count("sanjay"))
# 1
print(mylist.insert(3,"sanjay"))
# None
print(mylist)
# ['dhanush', 'harish', 'sanjay', 'sanjay', 'hendry', 'nasir', 'naveen']
print(mylist.count("sanjay"))
# 2
print(mylist)
# ['dhanush', 'harish', 'sanjay', 'sanjay', 'hendry', 'nasir', 'naveen']

#index
print(mylist.index("harish"))
# 1

#another format of index method
print(mylist[2])
# hendry

#reverse
print(mylist.reverse())
# None
print(mylist)
# ['naveen', 'nasir', 'hendry', 'sanjay', 'sanjay', 'harish', 'dhanush']


#TUPLE

#count
mylist=("dhanush","hari","harish")
print(mylist.count("dhanush"))
#1

#index
print(mylist.index("hari"))
#1
print(mylist[2])
#harish

#SET WITH NUMBERS  (numbers orderwise la print agum)
#add
myset={1,2,3,4,5}
print(myset.add(6))
#None
print(myset)
#{1, 2, 3, 4, 5, 6}
print(myset.add(0))
#None
print(myset)
#{0, 1, 2, 3, 4, 5, 6}
print(myset.add(8))
#None
print(myset)
#{0, 1, 2, 3, 4, 5, 6, 8}
print(myset.add(7))
#None
print(myset)
#{0, 1, 2, 3, 4, 5, 6, 7, 8}

#SET WITH LIST (list  ordered and unordered la print agum)
#add
myset={"dhanush","hari","harish","sanjay"}
print(myset.add("jeeva"))
#None
print(myset)
#{'dhanush', 'sanjay', 'hari', 'jeeva', 'harish'}
print(myset.add("raj"))
#None
print(myset)
#{'dhanush', 'sanjay', 'hari', 'jeeva', 'harish', 'raj'}
print(myset.add("kamalesh"))
#None
print(myset)
#{'dhanush', 'kamalesh', 'sanjay', 'hari', 'jeeva', 'harish', 'raj'}

#clear (clear means clear all list . only empty list print agum)
print(myset.clear())
#None
print(myset)
#set()
print(myset.add("jeeva")) 
#None
print(myset)
#{'jeeva'}
print(myset.add("sanjay"))
#None
print(myset)
#{'jeeva', 'sanjay'}
print(myset.clear())
#None
print(myset)
#set()

#DICTIONARY (ONLY VALUES ARE STORE IN "KEY" AND "VALUES")
student1={"name":"kumar","age":20,"course":"fullstack"}
print(student1)
#{'name': 'kumar', 'age': 20, 'course': 'fullstack'}

#UPDATE AGE
student1["age"]=23
print(student1)
#{'name': 'kumar', 'age': 23, 'course': 'fullstack'}

#ADD NEW "KEY" AND "VALUES"
student1["place"]="karur"
print(student1)
#{'name': 'kumar', 'age': 23, 'course': 'fullstack', 'place': 'karur'}


#LIST EXAMPLE PROGRAM
mylist=["apple","orange","banana"]
print(mylist)
#['apple', 'orange', 'banana']
print(mylist.append("grapes"))
#None
print(mylist)
#['apple', 'orange', 'banana', 'grapes']

print(mylist[1])
#orange
print(mylist[2])
#banana
mylist[1]="gova"
print(mylist)
#['apple', 'gova', 'banana', 'grapes']


#TUPLE EXAMPLE PROGRAM

colors=("red","blue","green","red")
print(colors)
#('red', 'blue', 'green', 'red')
print(colors[0])
#red
print(colors[1])
#blue
print(colors.count("red"))
#2
print(colors.index("blue"))
#1

#SET EXAMPLE PROGRAM
a={1,2,3,4}
b={5,6,3,2}

print(a.union(b))  # ONLY UNIQUE VALUE SHOW
#{1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # ONLY DUPLICATE VALUE SHOW
#{2, 3}


#DICTIONARY EXAMPLE PROGRAM
student = {
    "name": "Dhanush",
    "age": 21,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["age"])

student["age"] = 22
student["city"] = "Chennai"

print(student)