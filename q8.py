fi=open("txt.txt","r")
fo=open("text.txt","a")
r=fi.readlines()
for i in r:
    if 'p' in i:
        fo.write(i)
fi.close()
fo.close()
