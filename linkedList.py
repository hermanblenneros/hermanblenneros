from multiprocessing.sharedctypes import Value


class linkedList:
    def __init__(self, start = None):
        self.start = start
    
    def append(self, newNode):

        if self.start == None:
            return

        q = self.start

        while q.next != None:
            q = q.next
        
        q.next = newNode
        newNode.prev = q
    
    def insert(self, index, newNode):

        q = self.start

        if index == 0:
            newNode.next = q
            q.prev = newNode
            self.start = newNode
            return

        for i in range(0, index):
            q = q.next

        newNode.next = q
        q.prev.next = newNode
        newNode.prev = q.prev
        q.prev = newNode

    def remove(self, value):

        if self.start == None:
            return

        q = self.start

        while q != None:

            if q.data == value:
                q.prev.next = q.next
                q.next.prev = q.prev
                return q
            
            q = q.next
        
        raise ValueError


    def __len__(self):

        if self.start == None:
            return

        q = self.start
        k = 1;

        while q.next != None:
            k += 1
            q = q.next
        
        return k
