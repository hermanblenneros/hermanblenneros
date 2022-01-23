class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        if self.next != None:
            if self.prev != None:
                return f'Fully-connected node with value {self.data}'
            else:
                return f'Forward-connected node with value {self.data}'
        elif self.prev != None:
            return f'Backward-connected node with value {self.data}'

        else:
            return f'Isolated node with value {self.data}'

