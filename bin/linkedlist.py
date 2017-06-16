import random

class UnorderedList:
    def __init__(self):
        self.head=None
        self.count=0
    def isEmpty(self):
        return self.head == None
    def add(self, nodeData):
        curr = Node(nodeData)
        curr.setnext(self.head)
        self.head = curr
        self.count += 1
        return curr
    def insert(self,pos, insertData):
        new = Node(insertData)
        pointer =self.head
        i=0
        while pointer != None and i<pos:
            pointer = pointer.next
            i += 1
        curr=pointer.next
        pointer.setnext(new)
        new.setnext(curr)
    def p(self):
        pointer = self.head
        linkedlist=[]
        while pointer != None:
            linkedlist.append(pointer.data)
            # linkedlist.insert(0,pointer.data)
            pointer = pointer.next
        print(linkedlist)

    def __str__(self):
        pointer = self.head
        linkedlist = []
        while pointer != None:
            linkedlist.append({pointer.data:pointer.next})
            # linkedlist.insert(0,pointer.data)
            pointer = pointer.next
        return str(linkedlist)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def setnext(self, next):
        self.next = next

if __name__ == '__main__':

    # print(random.randrange(3,10))

    list = UnorderedList()
    list.add(67)
    list.add(11)
    list.add(40)
    list.add(30)
    list.add(0)
    last = list.add('a')
    list.insert(1,'inserted')
    # list.p()
    print(list)