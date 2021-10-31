import pickle
r=input('Enter roll no. that you want to search in binary file: ')
f=open("student.dat","rb")
lst=pickle.load(f)
f.close()
for i in lst:
    if r in i['Roll no.:']:
        print("Name of the student is", i['Name:'])
        break
    else:
        print("Record not found")
