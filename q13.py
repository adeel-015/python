import csv
def readcsv():
    with open('data.csv','rt')as f:
        data=csv.reader(f)
        for row in data:
            print(row)
def writecsv():
    with open('data.csv',mode='a',newline='') as f:
        writer=csv.writer(f,delimiter=',',quotechar='"')
        writer.writerow(['4','Devansh','Arts','404'])
print("Press 1 to Read Data and Press 2 to Write data: ")
n=int(input())
if n==1:
    readcsv()
elif n==2:
    writecsv()
else:
    print("Invalid value")
