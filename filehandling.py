#FILE HANDLING 

#MODES

# 1.'r' -> read
# 2.'w' -> write
# 3. w -> overwrite
# 4. 'a' -> append
# 5. 'x' -> create file . if doesn't exist 
# 6. 'r+' -> read + overwrite

# two ways

# 1.using "with"
# 2. without using "with"

# 1. without using "with"

# file=open("dhanush.txt",'w')
# file.write("my name is dhanush")
# file.close()

file=open("dhanush.txt",'w')
file.write("my name is dhanush raj")
file.close()

file=open("dhanush.txt",'a')
file.write(".i am 20 years old")
file.close()

file=open("dhanush.txt",'r')
print(file.read())

# file=open("dhanush.txt",'x')   # FILE EXISTS ERROR
# print(file)

file=open("dhanush.txt",'r+')
file.write("my name is sanjay raj")
print(file.read())

#2.using "with"
with open("raj.txt",'w') as file:
      file.write("my name is raj kumar")
      file.close()

with open ("raj.txt",'w') as file:
      file.write("i am 21 years old")
      file.close()

with open ("raj.txt",'r') as file:
      print(file.read())

with open ("raj.txt",'a') as file:
      file.write(".i am from karur")
      file.close()

with open ("raj.txt",'r+') as file:
      file.write(" i completed my BE degree\n")
      file.write("i am raj kumar\n")
      file.write("i am from karur\n")
      print(file.read())

# with open ("raj.txt",'x') as file:   #FILE EXISTS ERROR
#       file.close()


with open ("raj.txt",'r') as file:    # READLINE means read only first line.
      print(file.readline())

with open("raj.txt",'r') as file:
      print(file.readlines())

#output:(readlines)
#[' i completed my BE degree\n', 'i am raj kumar\n', 'i am from karur\n']


      with open("raj.txt",'w') as file:
            for i in range(1,101):
                  file.write(f"this line {i}\n")

      with open("raj.txt",'r') as file:
            lines=file.readlines()

      lines.insert(52,"this dmeo purpose\n")

      with open("raj.txt",'w') as file:
            file.writelines(lines)   # writelines ( updated list-ah file-ah save pannum)

      with open("raj.txt",'r') as file:  
            lines=file.readlines()
            print("total lines:", len(lines))   # len(lines) means count the lines

      