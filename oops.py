# OOPS : object oriented programming language.
#  1. maintain the large application.
#  2. code reusability.
#  3. enhanced data security via encapusaltion.
#  4. code flexibility with polymorphism.
#  5. easy to find errors and debugging.


# CLASS: it's a blueprint and used to create object.(ex:car)
# OBJECT: it's actual instanse from class.(real object). (ex:BMW)
# ATTRIBUTES: it's a way to describe an object.(ex: color,brand,design)
# METHODS: actions (ex:break, acclerate, gear)
# CONSTRUCTOR ANOTHER NAME IS "INITIALIZE" (special method).(__INIT__) USING DOBULE UNDERSCOR IN START AND END.

class car:   # class and class name
    def __init__(self,model,year):
        self.model=model   # attributes
        self.year=year     # attributes

    def start_engine (self):     # method 1
        return f"this {self.model} {self.year} engine has started"
    def stop_engine (self):      # method 2
        return f"this {self.model} {self.year} engine has stopped"

c1=car("mustang",1969)  # object creation and declare the values.
print(c1.start_engine()) # method call
print(c1.stop_engine())


# INHERITANCE (CREATE A REALATIONSHIP IN PARENT TO CHILD CLASS).

#TYPES:
# 1.SINGLE LEVEL INHERITANCE
# 2.MULTI-LEVEL INHERITANCE
# 3.MULTIPLE INHERITANCE
# 4.HIRARICAL INHERITANCE
# 5.HYBRID INHERITANCE

# 1.SINGLE LEVEL INHERITANCE. (USING ONE PARENT CLASS AND ONE CHILD CLASS)

class father:
    def house (self):
        print("pink")
class son (father):     # (PARENT TO CHILD REALATIONSHIP)
    def park (self):
        print("blue")

f=father()   # OUTPUT : PINK
f.house()

s=son()     # OUTPUT : PINK AND BLUE
s.house()
s.park()

# MULTI-LEVEL INHERITANCE. (USE ONE MORE CLASSES)

class grandfather:
    def house(self):
        print("pink")

class father(grandfather):
    def park(self):
        print("blue")

class son(father):
    def school(self):
        print("red")

g=grandfather()   # o/p : pink
g.house()

f=father()      # o/p : pink and blue
f.house()
f.park()

s=son()        # o/p : blue , pink , red
s.park()
s.house()
s.school()

# 3.MULTIPLE INHERITANCE (USING MULTIPLE PARENT CLASS AND ONE CHILE CLASS).

class father:
    def house(self):
        print("orange")

class mother:
    def school(self):
        print("yellow")

class son (father, mother):
    def park (self):
        print("gray")

f=father()  # o/p : orange
f.house()

m=mother()   # o/p : yellow
m.school()

s=son()       # o/p : yellow , orange , gray
s.school()
s.house()
s.park()


# 4. HIERARICAL INHERITANCE (ONE PARENT CLASS AND MULTIPLE CHILD CLASS).

class father:
    def house (self):
        print("pink")

class son (father):
    def park (self):
        print("blue")

class daughter (father):
    def school (self):
        print("yellow")

f=father()   # o/p : pink
f.house()

s=son()      #o/p : pink , blue
s.house()
s.park()

d=daughter()   #o/p : pink , yellow
d.house()
d.school()        

# 5.HYBRID (USING ALL INHERITANCE).

class dad:
    def house(self):
        print("pink")
class son (dad):
    def shop(self):
        print("blue")

class father:
    def hospital(self):
        print("yellow")

class daughter (father):
    def park(self):
        print("orange")

class elderson (father):
    def beach(self):
        print("gray")

d=dad()       # o/p : pink
d.house()

s=son()       #o/p : pink , blue
s.house()
s.shop()

f=father()      # o/p : yellow
f.hospital()

d=daughter()     # o/p : yellow , orange
d.hospital()
d.park()

e=elderson()      #o/p : yellow, gray
e.hospital()
e.beach()


# POLYMORPHISMM  :
# TYPES : METHODOVERRRIDING (USING SAME "METHOD NAME" BUT DIFFERENT BEHAVIOUR).
# OVERRIDE (OR) OVERWRITE (SAME).

class dad:
    def house(self):
        print("pink")

class son (dad):
    def house(self):     # house is a same method name. overwrite (or) reassiging the value.
        print("blue")

s=son()
s.house()

# ABSTRACTION :
# INTERNAL IMPLEMENT DETAILS ARE HIDE AND ONLY SHOW EXTERNAL IMPLEMENT DETAILS.
# EX: CAR -> ENGINE (INTERNAL DETAILS) , GEAR,BREAK (EXTERNAL DETAILS).
# FROM abc import ABC,Abstractmethod .(import the abstract method)
# @abstractmethod (inside the class menthion this word) meaning "MANDATORY"


from abc import ABC,abstractmethod

class dad:
    @abstractmethod      # MANDATORY
    def house (self):
        pass
    @abstractmethod
    def park (self):
        pass

class son(dad):
    # def house (self):
    #     print("son at the house")
    def park (self):
        print("son at the park")
    def home(self):
        print("son at the home")

s=son()
s.home()
# s.house()
s.park()

# ENCAPSULATION : (DATA PROTECTION)
# TYPES : 1.PUBLIC METHOD
#         2.PROTECTED METHOD (ADD PREFIX "_" SINGLE UNDERSCORE USE) EX: _NAME
#         3.PRIVATE METHOD (ADD PREFIX "__" DOUBLE UNDERSCORE USE)  EX: __NAME
# ALL THE THREE TYPES CAN BE OVERRIDE (OR) OVERWRITE.

# Public :- Anyone can read or change these attributes from outside the class.

class Profile:
    def __init__(self, username):
        self.username = username  # Public attribute

# Creating the object
user = Profile("Alice")

#method call
print(user.username)   # Output: Alice
user.username = "Bob"   # overwrite
print(user.username)  # Output: Bob

# # Protected :- The single underscore _ is a signal to other programmers that these variables are intended for internal use and within child classes (inheritance).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected attribute

class Manager(Employee):
    def show_salary(self):
        # Subclasses can freely access protected parent attributes
        return f"{self.name} earns ${self._salary}"

# Creating the object
mgr = Manager("Carlos", 80000)
print(mgr.show_salary())  # Output: Carlos earns $80000

 # Private :- The double underscore __ completely locks the variable inside the class. Trying to access it directly from an object will cause a crash.

class Safe:
    def __init__(self, code):
        self.__code = code  # Private attribute

    def unlock(self, entered_code):
        # Can only be accessed by methods inside the class
        if entered_code == self.__code:
            return "Safe opened!"
        return "Wrong code!"

# Creating the object
my_safe = Safe("9999")

# print(my_safe.__code)  # CRASHES: AttributeError

# The only safe way to interact with the data:
print(my_safe.unlock("1234"))  # Output: Wrong code!
print(my_safe.unlock("9999"))  # Output: Safe opened!
