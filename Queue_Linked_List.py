class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue_Linked_List:
    def __init__(self):
        self.head=None
    def Enqueue(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
    def Dequeue(self):
        if (self.head==None):
            print("Queue empty")
        else:
            self.head=self.head.next
    def Display(self):
        if (self.head==None):
            print("Queue empty")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,"--->",end=" ")
                temp=temp.next
    def Search(self,data):
        if (self.head==None):
            print("Queue empty")
        else:
            temp=self.head
            count=0
            while(temp!=None):
                if (temp.data==data):
                    print(data,"found at index-->",count)
                    return
                count +=1
                temp=temp.next
            print("Element is not found")
    def Peek(self):
        if (self.head==None):
            print("Queue empty")
        else:
            print("Peak element is --->",self.head.data)
    def Isempty(self):
        if self.head==None:
            print("Queue empty")
        else:
            print("Queue is not empty")
   
print("Implementation of Queue using Linkedlist")
obj=Queue_Linked_List()
while True:
    print("1) Enqueue \n2) Dequeue  \n3) Display  \n4) Search \n5) Peek \n6) Isempty")
    choice=int(input())
    if choice==1:
        size=int(input("Enter Size of Queue : "))
        for item in range (size):
            n=int(input("Enter element to add : "))
            obj.Enqueue(n)
        obj.Display()
        print()
    elif choice==2:
        obj.Dequeue()
        obj.Display()
        print()
    elif choice==3:
        obj.Display()
        print()
    elif choice==4:
        n1=int(input("Enter element to Search for : "))
        obj.Search(n1)
        print()
    elif choice==5:
        obj.Peek()
    elif choice==6:
        obj.Isempty()
    else:
        print("Enter correct choice..!!")
        print()


            
        

            
