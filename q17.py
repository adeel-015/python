a=eval(input("Enter the elements: "))
l=len(a)
for j in range(0,l-1):
    for i in range(0,l-1):
        if a[i]>a[i+1]:
            b=a[i]
            a[i]=a[i+1]
            a[i+1]=b
print("The sorted list is: ",a)
