
class Node:
    def __init__(self ,next ,data):
        self.next = next
        self.data = data
    def getData(self):
        return self.data

class LinkedStack:
    def __init__(self ,size):
        self.maxSize = size
        self.head = None
    # it will insert elements in the begining of the node
    def insert_at_begining(self ,data):
        if self.head == None:
            newNode = Node(self.head ,data)
            self.head = newNode
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            newNode = Node(itr.next ,data)
            itr.next = newNode



    def print_linkedList(self):
        itr = self.head
        nodeCount = 0
        while itr.next != None:
            print("Node " ,nodeCount ,": " ,itr.data)
            itr = itr.next

my_linkedList = LinkedStack(10)

sampleList = [100 ,6464 ,7374 ,237842 ,78378]

for i in sampleList:
    my_linkedList.insert_at_begining(i)

my_linkedList.print_linkedList()
#This is my file





