import time
print("1. Get started")
print("2. Help")
choice=input ("Enter a number: ")
if choice=="2":
 print("in the beginning welcomes you select the file, here you need to write the name of the file to finish the operation, press the key combination 'Ctrl + C', if you want to create the file, the program must be run from the desired directory")
 print("Now you are ready to go, good luck")
else:
 print("If you didn't read the help, please read")
path=input("Enter name: ")
f = open(path, 'w' )
x=1
while x==1:
s=input()
 s= s+"\n"
 f.write(s)
