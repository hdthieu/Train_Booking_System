import re
def alphanumeric_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

class CustomerList:
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

    def display(self):
        current = self.head
        while current:
            customer = current.data
            print(f"{customer.ccode} | {customer.cus_name} |  {customer.phone}")
            current = current.next

    def search_by_ccode(self, ccode):
        current = self.head
        while current:
            if current.data.ccode == ccode:
                return current.data
            current = current.next
        return None 
    
    def delete_by_ccode(self, ccode):
        current = self.head
        while current:
            if current.data.ccode == ccode:
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
    
    def is_ccode_unique(self, ccode):
        current = self.head
        while current:
            if current.data.ccode == ccode:
                return False
            current = current.next
        return True
    
    def has_customer(self, ccode):
        current = self.head
        while current:
            if current.data.ccode == ccode:
                return True
            current = current.next
        return False