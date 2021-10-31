f=open("txt.txt",'r')
r=f.readlines()
b=''
for i in range(len(r)):
    a=r[i].split()
    for j in a:
        b+=j
        b+='#'
print(b)
f.close()
