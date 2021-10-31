import collections
f=open('txt.txt','r')
a=f.read()
b={}
l=a.lower().split()
for i in l:
    i=i.replace(".","")
    i=i.replace(",","")
    i=i.replace(":","")
    i=i.replace("\"","")
    i=i.replace("!","")
    i=i.replace("&","")
    i=i.replace("*","")
for j in l:
    k=j
    if k not in b:
        c=l.count(k)
        b[k]=c
d=int(input("How many most common words to print: "))
print("\nOK.",d,"most common words are as follows\n")
w=collections.Counter(b)
for i, c in w.most_common(d):
    print(i,":",c)
f.close()
