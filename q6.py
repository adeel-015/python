f=open("txt.txt",'r')
str=f.read()
L=str.split()
c=0
for i in L:
    c+=1
print(c)
f.close()
