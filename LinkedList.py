class Node:
    data = None
    next_node = None
    
    def __init__(self, data) -> None:
        self.data = data
        
    def __repr__(self) -> str:
        return "<Node %s>"%self.data

class Linked_list:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    
    def size(self):
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        new_data = Node(data)
        new_data.next_node = self.head
        self.head = new_data
    
    def search(self, key):
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
        
        while current:
            if current.data == key:
                return current.data
            else:
                current = current.next_node
        return None
    
    def delete(self, key):
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
                
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            current.next_node
            
            while position > 1:
                current = new.next_node
                position -= 1
                
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
    
    def __repr__(self) -> str:
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head %s]" %current.data)
            
            elif current.next_node is None:
                nodes.append("[Tail %s]" %current.data)
            
            else:
                nodes.append("[%s]" %current.data)
            
            current = current.next_node
        
        return '-> '.join(nodes)