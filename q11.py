import pickle
r=input('Enter roll no. whose name you want to update in binary file : ')
f=open("student.dat","rb+")
lst=pickle.load(f)
found=0
lst1=[]
for i in lst:
    if r in i['Roll no.:']:
        found=1
        i['Name:']=input('Enter new name: ')
    lst1.append(i)
if found==1:
    f.seek(0)
    pickle.dump(lst1,f)
    print("Record Updated")
else:
    print("roll no. doesn't exist")
f.close()
