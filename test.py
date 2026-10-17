# s="Python"
# print(s[0],s[-1],s[6]) #s[6] is out of range and will raise an IndexError. 

#INDEXING BASICS:
#question :1
s="Python"
print(s[0],s[-1],s[5]) #valid indices for the string "Python" are 0 to 5.

#question :2
s="Python"
print(s[4])  # positive indexing (0 to 5)
print(s[-3]) # negative indexing  (-1 to -6)

#question :3
s="code"
# print(s[10])  this line s[10] is out of range and will raise an IndexError.
print(s[1:10]) # s[1:10] print only valid indices from 1 to 3, the output is "ode".

#question :4
s="mississippi"
print(s[2])  # first 's' in the string using positive indexing
print(s[6])  # last 's' in the string using positive indexing
print(s[2],s[6]) # first and last 's' in the string using positive indexing
print(s[-5]) # last 's' in the string using negative indexing
print(s.find('s')) # s.find('s') means left side la irunthu first 's' find pannum, output is 2
print(s.rfind('s')) # s.rfind('s') means right side la irunthu first 's' find pannum, output is 6

#question :5
s="abcdef"     # using negative indexing
print(s[-1],s[-3],s[-6])  #s[-1] is reversed index of 'f', s[-3] is reversed index of 'd', s[-6] is reversed index of 'a'.

#SLICING BASICS:
#question :6
s="python"
print(s[1:5:2]) #[1:5:2]  [start:end:step] concept. start=1 'y' la irunthu start agum .
 #end=5 'n' la end agum. step=2 means evolo index skip panni next index print agum. So output is 'yh'.
print(s[0:6:3]) #start=0 'p' la irunthu start agum. end=6 'n' la end agum. step=3 means evolo index skip panni next index print agum. So output is 'ph'.

#question :7
s="helloworld"
print(s[0:5]) # 0 - 'h' la start agum. 5 - 'w' la end agum. 5 'w' exclude agirum.So output is 'hello'.
print(s[5:]) # 5 - 'w' la start agum. end varikum print agum.So output is 'world'.
print(s[:5]) # 0 - 'h' la start agum. 5 - 'w' la end agum. 5 'w' exclude agirum.So output is 'hello'.
print(s[:])  # 0 - 'h' la start agum. end varikum print agum.So output is 'helloworld'.

#question :8
s="python"
print(s[4:1]) # 4 - 'o' la start agum. 1 - 'y' la end agum. 1 'y' exclude agirum.So output is empty string ''.
print(s[4:1:-1]) # 4 - 'o' la start agum. 1 - 'y' la end agum. 1 'y' exclude agirum. step=-1 means reverse indexing.So output is 'onh'.

#question :9
s="python"
print(s[3:6]) # 3 - 'h' la start agum. 6 - 'n' la end agum. 6 'n' exclude agirum.So output is 'hon'.

#question :10
s="abcdefgh"
print(s[::1]) # [::1] means start=0, end=8, step=1. So output is 'abcdefgh'.
print(s[::2]) # [::2] means start=0, end=8, step=2. So output is 'aceg'.
print(s[1::2]) # [1::2] means start=1, end=8, step=2. So output is 'bdfh').

#STEP & REVERSE SLICING:
#question :11
s="python"
print(s[::-1]) #using reverse slicing, output is 'nohtyp'.
print(s[::-2]) #using reverse slicing with step=2, output is 'nhy'.
print(s[::-3]) #using reverse slicing with step=3, output is 'ny'.

#question :12
s="abcdefgh"
print(s[::-1]) #using reverse slicing, output is 'hgfedcba'.
print(s[::-2]) #using reverse slicing with step=2, output is 'hfdb'.
print(s[6:1:-1]) # 6 - 'g' la start agum. 1 - 'b' la end agum. 1 'b' exclude agirum. step=-1 means reverse indexing.So output is 'gfedc'.

#question :13
s="a1b2c3d4e5"
print(s[1:10:2]) # [1:10:2] means start=1, end=10, step=2. So output is '12345'.

#question :14
s="Python"
print(s[5:0:-1]) # 5 - 'n' la start agum. 0 - 'P' la end agum. 0 'P' exclude agirum. step=-1 means reverse indexing.So output is 'nohty'.
print(s[5::-1]) # 5 - 'n' la start agum. end varikum print agum. step=-1 means reverse indexing.So output is 'nohtyP'.
print(s[:0:-1]) # 0 - 'P' la end agum. 0 'P' exclude agirum. step=-1 means reverse indexing.So output is 'nohty'.

#question :15
s="hello"
print(s[100::-1]) # 100 - 'o' la start agum. end varikum print agum. step=-1 means reverse indexing.So output is 'olleh'.
print(s[::-100]) # satarting '0' la start agum. end varikum print agum. step=-100 means reverse indexing.So output is 'o'.

#INTERMEDIATE SLICING CHALLANGE:
#question :16
s="abcdefghij"
print(s[3:8]) # 3 - 'd' la start agum. 8 - 'i' la end agum. 8 'i' exclude agirum. So output is 'defgh'.
print(s[2:7]) # 2 - 'c' la start agum. 7 - 'h' la end agum. 7 'h' exclude agirum. So output is 'cdefg'.

#question :17
s="racecar"
print(s == s[::-1]) # s[::-1] means reverse the string. So output is True because "racecar" is a palindrome.

#question :18
s="hello"
print(s[1:100]) # 1 - 'e' la start agum. end varikum print agum. So output is 'ello'.
print(s[-100:3]) # -100 - 'h' la start agum. 3 - 'l' la end agum. 3 'l' exclude agirum. So output is 'hel'.
print(s[100:200]) # 100 - 'o' la start agum. end varikum print agum. So output is '' (empty string).

#question :19
s="hello world"
rep=s.replace('world','python')
print(rep) # s.replace('world','python') means replace 'world' with 'python'. So output is 'hello python'.

#question :20
s="abcdefghij"
my_slice = slice (1,8,2)
print(s[my_slice]) # slice(1,8,2) means start=1, end=8, step=2. So output is 'bdfh'.



