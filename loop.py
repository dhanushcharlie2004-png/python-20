#for loop 
# CORM - checks once and run manytime

#format 1
name="dhanush"
for i in name:
    print(i,end=',') # horizontal ahh print agum
    print(i)# vertical ahh print agum

# #format 2
my_list =['ashiq', 'dhanush', 'hari', 'harish']
for i in my_list:
    print(i, end=',')

# #format3
for i in range (1,11):
    print(i,'*4=', i*4)

for i in range (2,11,2):
    print(i,'*4=', i*4)  # only even numbers print agum


# #break
for i in range (10):
    if i==5:
        break
    print(i) 

# #pass
name='gokul'
for i in name:
    pass

# #continue
my_list=[2,5,-6,9,-10,-7]
for i in my_list:
    if i<0:
        continue
    print(i)

    
