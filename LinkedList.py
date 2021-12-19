# Name: Nischal Khadka
# Email: nischalkhadka.nk@gmail.com
# purpose: To learn linked list, and its common use

class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,value):
        node = Node(value,self.head)
        self.head = node

    def insert_at_end(self,value):
        if self.head == None:
            node = Node(value,self.head)
            self.head = node
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next

            node = Node(value,itr.next)
            itr.next = node
    def print_node(self):
        itr = self.head
        while itr != None:
            print(itr.value)
            itr = itr.next

linkedList = LinkedList()
linkedList.insert_at_begining("Nischal")
linkedList.insert_at_begining("Sagun")
linkedList.insert_at_begining("Nishant")
linkedList.insert_at_begining("Keshav")
linkedList.insert_at_begining("Sarita")



linkedList.insert_at_end("Manamaya")
linkedList.insert_at_end("Baa")
linkedList.insert_at_end("Khadga")

linkedList.print_node()
