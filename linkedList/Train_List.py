from entity.Train import Train

import re
def alphanumeric_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

class Train_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, node):
        if not self.head:  
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def add_to_head(self, node):
        if not self.head:  
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete_by_tcode(self, tcode):
        current = self.head
        while current:
            if current.data.tcode == tcode:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head: 
                    self.head = current.next
                if current == self.tail: 
                    self.tail = current.prev
                return True  
            current = current.next
        return False  

    def display(self):
        current = self.head
        while current:
            train = current.data
            print(f"{train.tcode} | {train.tname} | {train.seat} | {train.booked} | {train.depart_time} | {train.depart_place} | {train.available_seat}")
            current = current.next

    def searchByTcode(self, tcode):
        current = self.head
        while current:
            if current.data.tcode == tcode:
                return current.data
            current = current.next
        return None 

    def is_tcode_unique(self, tcode):
        current = self.head
        while current:
            if current.data.tcode == tcode:
                return False
            current = current.next
        return True
    
    def sort_by_tcode(self):
        swap = True
        while swap:
            current = self.head
            swap = False
            while current is not None and current.next is not None:
                next_node = current.next
                if alphanumeric_key(current.data.tcode) > alphanumeric_key(next_node.data.tcode):
                    current.data, next_node.data = next_node.data, current.data
                    swap = True
                current = current.next
    
    def add_after_position(self, node, k):
        if not self.head or k < 0:
            return False
        current = self.head
        pos = 0
        while current and pos < k:
            current = current.next
            pos += 1
        if not current:
            return False
        node.next = current.next
        node.prev = current
        if current.next:
            current.next.prev = node
        current.next = node
        if not node.next:
            self.tail = node
        return True
    
    def delete_before_tcode(self, tcode):
        if self.head is None or self.head.next is None:  
            return False  

        current = self.head.next  
        while current is not None:
            if current.data.tcode == tcode and current.prev is not None:
                to_delete = current.prev
                if to_delete.prev is not None:
                    to_delete.prev.next = current
                    current.prev = to_delete.prev
                else:
                    self.head = current
                    current.prev = None
                return True 
            current = current.next
        return False
    
    def has_train(self, tcode):
        current = self.head
        while current:
            if current.data.tcode == tcode:
                return True
            current = current.next
        return False