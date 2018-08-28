#Q.1- Write a Python program to read n lines of a file
f=open("hello.txt","r")
print(f.read())
f.close()

#Q.2- Write a Python program to count the frequency of words in a file.
f=open("hello.txt","r")
a=f.read()
b=input("enter word to count the frequency")
c=a.count(b)
print("\n",b,"occour",c,"times")
f.close()


#Q.3- Write a Python program to copy the contents of a file to another file
f=open("hello1.txt","r")
a=f.read()
f.close()
print("before copying")
g=open("hello2.txt","r")
b=g.read()
print(b,"\n")
print("after copying","\n")
g.close()
g=open("hello2.txt","a")
g.write(a)
g.close()
g=open("hello2.txt","r")
c=g.read()
print(c)
g.close()


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f=open("hello3.txt","r")
a=open("hello4.txt","r")
c=open("hello5.txt","w")
b=f.readlines()
d=a.readlines()
for h,i in zip(b,d):
    c.write(h)
    c.write(i)    
c.close()
c=open("hello5.txt","r")
r=c.read()
print(r)
c.close()
a.close()
f.close()

#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
f=open("file.txt","r")
f2=open("file1.txt","w+")
a=f.readlines()
a.sort()
f2.write(str(a))
f2.close()
f2=open("file1.txt","r")
b=f2.read()
print(b)
f2.close()
f.close()
