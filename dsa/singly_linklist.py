class Node:
    def __init__(self,item =None, next = None):
        self.item = item
        self.next = next
class sll:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        if self.start ==None
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
    def insert_after(self,data,index_data):
        k =self.search(index_data)
        if k is not None:
print("dfjg")