a=eval(input("Enter the elements: "))
l=len(a)
b=eval(input("Enter the element that you want to search: "))
for i in range(l):
    if a[i]==b:
        print("Element found at the position :", i+1)
        break
else:
    print("Element not Found")
