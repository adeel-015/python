a=True
while a:
    b=int(input("Press 1 to find the ordinal value of a character \nPress 2 to find a character of a value\n"))
    if b==1:
        c=input("Enter a character : ")
        print(ord(c))
    elif b==2:
        d=int(input("Enter an integer value: "))
        print(chr(d))
    else:
        print("You entered wrong choice")
    print("Do you want to continue? Y/N")
    e=input()
if e=='y' or e=='Y':
    a=True
else:
    a=False
