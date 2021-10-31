class Queue:
    def __init__(Q):
        Q.i=[]
    def isEmpty(Q):
        return Q.i==[]
    def Enqueue(Q,I):
        Q.i.append(I)
        if len(Q.i)==1:
            front=rear=0
        else:
            rear=len(Q.i)
    def Dequeue(Q):
        return Q.i.pop(0)
    def peek(Q):
        return Q.i[len(Q.i)-1]
    def size(Q):
        return len(Q.i)
q=Queue()
print("MENU BASED QUEUE")
t=True
while t:
    print("1.ENQUEUE")
    print("2.DEQUEUE")
    print("3.Display")
    print("4.Size of Queue")
    print("5.Value at rear")
    c=int(input("Enter your choice(1-5): "))
    if c==1:
        v=input("Enter the element: ")
        q.Enqueue(v)
    elif c==2:
        if q.i==[]:
            print("Queue is empty")
        else:
            print("Deleted element is: ",q.Dequeue())
    elif c==3:
        print(q.i)
    elif c==4:
        print("Size of the queue is: ",q.size())
    elif c==5:
        print("Value of rear element is: ", q.peek())
    else:
        print("You entered wrong choice")
    print("Do you want to continue? Y/N")
    o=input()
    if o=='y' or o=='Y':
        t=True
    else:
        t=False
