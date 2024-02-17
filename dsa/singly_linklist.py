class Node:
    def __init__(self,item =None, next = None):
        self.item = item
        self.next = next
class sll:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        if self.start ==None:
            return True
        return False
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start= n
    def insert_at_last(self,data):
        n =Node(data)
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item ==data:
                return temp
            temp = temp.next
        return None
    def insert_after(self,data,temp):
        k =self.search(temp)
        if k is not None:
            n = Node(data,k.next)
            k.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
    def delete_first(self):
        if self.start:
            self.start = self.start.next


my_list = sll()

my_list.insert_at_start(20)
my_list.insert_at_last(30)
my_list.insert_at_start(400)
my_list.insert_at_start(500)
my_list.insert_after(50,30)
my_list.delete_first()
my_list.print_list()