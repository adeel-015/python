import pickle
def writedata():
    lst=[]
    while True:
        r=input("Enter student's Roll No: ")
        n=input("Enter student's Name : ")
        s={"Roll no.:":r,"Name:":n}
        lst.append(s)
        c=input("Add more records?(y/n): ")
        if (c=='y' or c=='Y'):
            continue
        elif (c=='n' or c=='N'):
            break
    f=open("student.dat","wb")
    pickle.dump(lst,f)
    f.close()
def readdata():
    f=open("student.dat","rb")
    lst=pickle.load(f)
    print(lst)
    f.close()
print("Press 1 to write data\nPress 2 to read data")
c=int(input())
if c==1:
    writedata()
elif c==2:
    readdata()
else:
    print("Invalid choice")
