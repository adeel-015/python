import pickle
r=input('Enter roll no. whose record you want to delete: ')
f=open("student.dat","rb+")
lst=pickle.load(f)
d=0
lst1=[]
for i in lst:
    if r not in i['Roll no.:']:
        lst1.append(i)
    else:
        d=1
if d==1:
    f.seek(0)
    pickle.dump(lst1,f)
    print("Record Deleted")
else:
    print("Roll no. doesn't exist")
f.close()
