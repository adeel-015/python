f=open("txt.txt",'r')
str=f.read()
s=str.split()
c=0
for i in s:
    if i=='is':
        c+=1
print(c)
f.close()
