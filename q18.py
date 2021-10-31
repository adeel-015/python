class Stack:
    def __init__(s):
        s.i=[]
    def isEmpty(s):
        return s.i==[]
    def push(s,I):
        s.i.append(I)
    def pop(s):
        return s.i.pop()
    def peek(s):
        return s.i[len(s.i)-1]
    def size(s):
        return len(s.i)
S=Stack()
print("MENU BASED STACK")
t=True
while t:
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Size of Stack")
    print("5.Value at Top")
    c=int(input("Enter your choice(1-5): "))
    if c==1:
        v=input("Enter the element: ")
        S.push(v)
    elif c==2:
        if S.i==[]:
            print("Stack is empty")
        else:
            print("Deleted element is: ",S.pop())
    elif c==3:
        print(S.i)
    elif c==4:
        print("Size of the stack is: ",S.size())
    elif c==5:
        print("Value of top element is :",S.peek())
    else:
        print("You entered wrong choice ")
    print("Do you want to continue? Y/N")
    o=input()
    if o=='y' or o=='Y':
        V=True
    else:
        V=False
