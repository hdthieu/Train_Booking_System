from linkedList.Booking_list import BookingList
from entity.Booking import Booking
import os
import csv
from Node.Node import Node

class BookingManagement:
    def __init__(self):
        self.bookings = BookingList()
    
    def input_booking(self, tcode, ccode, seat, trains, customers):
        # Kiểm tra nếu mã tàu và mã khách hàng tồn tại trong danh sách Tàu và Khách hàng
        if not trains.has_train(tcode):
            print("Mã tàu không tồn tại.")
            return
        
        if not customers.has_customer(ccode):
            print("Mã khách hàng không tồn tại.")
            return

        # Kiểm tra nếu mã tàu và mã khách hàng đã tồn tại trong danh sách Đặt vé
        if self.bookings.find_booking(tcode, ccode):
            print("Vé đã tồn tại.")
            return

        # Kiểm tra nếu tàu đã hết chỗ
        train = trains.searchByTcode(tcode)
        if train.booked == train.seat:
            print("Tàu đã hết chỗ.")
            return

        # Kiểm tra nếu có đủ ghế để đặt
        if seat <= train.seat - train.booked:
            booking = Booking(tcode, ccode, seat)
            node = Node(booking)
            self.bookings.add_to_end(node)
            train.booked += seat
            print("Đặt vé thành công.")
        else:
            print("Không đủ ghế trống.")

    def display_bookings(self, trains):
        header = "{:<8} | {:<20} | {:<15} | {:<12}".format("tcode", "ccode", "seat", "Available Seats")
        print(header)
        print('-' * len(header))

        current = self.bookings.head
        while current:
            booking = current.data
            train = trains.searchByTcode(booking.tcode)
            available_seats = train.available_seat
            print("{:<8} | {:<20} | {:<15} | {:<12}".format(booking.tcode, booking.ccode, booking.seat, available_seats))
            current = current.next

    def sort_bookings_by_tcode(self):
        self.bookings.sort_by_tcode()



    
    
  
   