import re
def alphanumeric_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

class BookingList:
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
            booking = current.data
            print(f"{booking.tcode} | {booking.ccode} |  {booking.seat}")
            current = current.next

    def sort_by_tcode(self):
        swap = True
        while swap:
            current = self.head
            swap = False
            while current is not None and current.next is not None:
                next_node = current.next
                # So sánh tcode và ccode của các nút
                if (current.data.tcode, current.data.ccode) > (next_node.data.tcode, next_node.data.ccode):
                    # Hoán đổi dữ liệu giữa các nút
                    current.data, next_node.data = next_node.data, current.data
                    swap = True
                current = current.next

    def find_booking(self, tcode, ccode):
        current = self.head
        while current:
            if current.data.tcode == tcode and current.data.ccode == ccode:
                return True
            current = current.next
        return False
    
    def display(self):
        current = self.head
        while current:
            booking = current.data
            print(f"{booking.tcode} | {booking.ccode} |  {booking.seat}")
            current = current.next

