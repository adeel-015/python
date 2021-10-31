import random
a=random.randint(1,6)
g=int(input("Enter a no. between 1 to 6 :"))
if a==g:
    print("Congratulations! You won the lottery")
else:
    print("Better luck next time. The lucky number was: ",a)
