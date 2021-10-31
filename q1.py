a=int(input("Enter a no.: "))
b=a
c=0
while a>0:
    d=a%10
    c=d+c*10
    a=a//10
if c==b:
    print("No. is Palindrome")
else:
    print("No. isn't Palindrome")
