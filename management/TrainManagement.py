
from linkedList.Train_List import Train_List
from entity.Train import Train
import os
import csv
from Node.Node import Node
class TrainManagement:
    def __init__(self):
        self.trains = Train_List()
    
    def load_data(self, filename):
        # full_path = os.path.join(os.getcwd(), filename)
        # if self.trains.head is not None:
        #     response = input("Danh sách đã chứa dữ liệu. Bạn có muốn giữ lại dữ liệu hiện có? (yes/no): ")
        #     if response.lower() == 'n':
        #         self.trains = Train_List()  
        # if not os.path.exists(full_path):
        #     print(f"File {full_path} không tìm thấy.")
        #     return
        # with open(filename, 'r', newline='') as csvfile:
        #     csv_reader = csv.reader(csvfile, delimiter=',')
        #     for row in csv_reader:
        #         tcode, tname, seat, booked, depart_time, depart_place = row
        #         train = Train(tcode.strip(), tname.strip(), int(seat), int(booked), depart_time.strip(), depart_place.strip())          
        #         self.trains.add_to_end(Node(train))
        #     print("Load thành công file.")
        full_path = os.path.join(os.getcwd(), filename)
        if self.trains.head is not None:
            response = input("Danh sách đã chứa dữ liệu. Bạn có muốn giữ lại dữ liệu hiện có? (yes/no): ")
            if response.lower() == 'n':
                self.trains = Train_List()  
        if not os.path.exists(full_path):
            print(f"File {full_path} không tìm thấy.")
            return
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            header_skipped = False
            for row in csv_reader:
                if not header_skipped:
                    header_skipped = True
                    continue  
                tcode, tname, seat, booked, depart_time, depart_place, _ = row  
                train = Train(tcode.strip(), tname.strip(), int(seat), int(booked), depart_time.strip(), depart_place.strip())          
                self.trains.add_to_end(Node(train))
            print("Load thành công file.")

    def add_train(self):
        tcode = input("Nhập vào train code (tcode): ").strip()
        if not self.trains.is_tcode_unique(tcode):
            print(f"Mã '{tcode}' đã tồn tại.")
            return

        tname = input("Nhập vào train name (tname): ").strip()
        
        try:
            seat = int(input("Nhập số chỗ ngồi (seat > 0): "))
            booked = int(input("Nhập số chỗ đã đặt (booked >=0 && booked <= seat): "))
            depart_time = float(input("Nhập thời gian khởi hành (depart_time >= 0): "))
            depart_place = input("Nhập nơi khởi hành (depart_place): ").strip()

            new_train = Train(tcode, tname, seat, booked, depart_time, depart_place)
            new_node = Node(new_train) 
            self.trains.add_to_head(new_node) 
            print(f"Tàu có tên: '{tname}' cùng với mã tcode: '{tcode}' đã được thêm thành công.")
            
        except ValueError as e:
            print(f"Error: {e}")
            return


    def display_trains(self):
        header = "{:<5} | {:<9} | {:^4} | {:^6} | {:>11} | {:<12} | {:>13}".format(
            "tcode", "Train_name", "Seat", "booked", "depart_time", "depart_place", "available_seat"
        )
        print(header)
        print('-' * len(header))

        current = self.trains.head
        while current:
            train = current.data
            print("{:<5} | {:<9} | {:^4} | {:^6} | {:>11} | {:<12} | {:>13}".format(
                train.tcode, train.tname, train.seat, train.booked, train.depart_time, train.depart_place, train.available_seat
            ))
            current = current.next
    
    def save_data(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Viết tiêu đề vào file CSV
            csv_writer.writerow(["tcode", "Train_name", "Seat", "booked", "depart_time", "depart_place", "available_seat"])
            
            current = self.trains.head
            while current:
                train = current.data
                csv_writer.writerow([
                    train.tcode, train.tname, train.seat, train.booked, train.depart_time, train.depart_place, train.available_seat
                ])
                current = current.next
        print("Dữ liệu được lưu thành công vào CSV.")
    
    def searchByTcode(self, tcode):
        train_data = self.trains.searchByTcode(tcode)
        return train_data


    def delete_by_tcode(self, tcode):
        trainDeletedTcode = self.trains.delete_by_tcode(tcode)
        if trainDeletedTcode:
            print(f"Xóa thành công '{tcode}' ")
        else:
            print(f"Không tìm thấy '{tcode}' .")
    
    def sort_trains_by_tcode(self):
        self.trains.sort_by_tcode()
    
    def add_train_after_position(self,  k):
        tcode = input("Nhập vào train code (tcode): ")
        if not self.trains.is_tcode_unique(tcode):
            print(f"Tàu với mã tcode: '{tcode}' đã tồn tại.")
            return
        tname = input("Nhập vào tên tàu (tname): ")
        seat = int(input("Nhập số chỗ ngồi (seat): "))
        booked = int(input("Nhập số chỗ đã đặt (booked): "))
        depart_time = input("Nhập thời gian khởi hành (depart_time): ")
        depart_place = input("Nhập nơi khởi hành(depart_place): ")
        
        new_train = Train(tcode, tname, seat, booked, depart_time, depart_place)
        new_node = Node(new_train)
        
        if self.trains.add_after_position(new_node, k):
            print(f"Train có tên: '{tname}' cùng với mã tcode '{tcode}' được thêm thành công sau vị trí {k}.")
        else:
            print(f"Không thêm được chuyến tàu sau vị trí {k}. Vui lòng kiểm tra xem vị trí có hợp lệ không.")

    def delete_before_tcode(self, xCode):
        if self.trains.delete_before_tcode(xCode):
            print(f"Xóa thành công trước '{xCode}' ")
        else:
            print(f"Không tìm thấy '{xCode}' .")

    def has_train(self, tcode):
        return self.trains.has_train(tcode)