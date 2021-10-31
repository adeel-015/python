def fact(f):
    a=1
    b=1
    while a<=f:
        b=b*a
        a+=1
        return b
n=int(input("Enter the no.: "))
i=1
sum=1
while i<=n:
    f=fact(i)
    sum+=1/f
    i+=1
print(sum)
