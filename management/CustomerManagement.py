from linkedList.Customer_list import CustomerList
from entity.Customer import Customer
import os
import csv
from Node.Node import Node

class CustomerManagement:
    def __init__(self):
        self.customers = CustomerList()

    def load_data(self, filename):
        full_path = os.path.join(os.getcwd(), filename)
        if self.customers.head is not None:
            response = input("Danh sách đã chứa dữ liệu. Bạn có muốn giữ lại dữ liệu hiện tại không? (Y/N): ")
            if response.lower() == 'n':
                self.customers = CustomerList()
        if not os.path.exists(full_path):
            print(f"Tệp {full_path} không tồn tại.")
            return

        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)  # Bỏ qua dòng tiêu đề

            for row in csv_reader:
                ccode, cus_name, phone = row
                customer = Customer(ccode.strip(), cus_name.strip(), phone.strip())
                self.customers.add_to_end(Node(customer))

        print("Dữ liệu được tải thành công từ tệp CSV.")

    def add_customer(self):
        ccode = input("Nhập mã khách hàng (ccode): ")
        if not self.customers.is_ccode_unique(ccode):
            print(f"Khách hàng với mã '{ccode}' đã tồn tại. Vui lòng nhập một mã duy nhất.")
            return
        cus_name = input("Nhập tên khách hàng (cus_name): ")
        phone = input("Nhập số điện thoại (phone): ")

        new_customer = Customer(ccode, cus_name, phone)
        new_node = Node(new_customer)
        self.customers.add_to_end(new_node)
        print(f"Khách hàng '{cus_name}' có mã '{ccode}' đã được thêm thành công vào danh sách.")

    def display_customers(self):
        header = "{:<8} | {:<20} | {:<15}".format("ccode", "Customer Name", "Phone")
        print(header)
        print('-' * len(header))

        current = self.customers.head
        while current:
            customer = current.data
            print("{:<8} | {:<20} | {:<15}".format(customer.ccode, customer.cus_name, customer.phone))
            current = current.next


    def save_data(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Viết tiêu đề vào file CSV
            csv_writer.writerow(["ccode", "Customer Name", "Phone"])
            
            current = self.customers.head
            while current:
                customer = current.data
                # Viết dữ liệu vào file CSV, mỗi giá trị được ngăn cách bằng dấu phẩy
                csv_writer.writerow([
                    customer.ccode, customer.cus_name, customer.phone
                ])
                current = current.next
        print("Dữ liệu đã được lưu thành công vào tệp CSV.")

    def search_by_ccode(self, ccode):
        data = self.customers.search_by_ccode(ccode)
        if data:
            # Hiển thị hoặc xử lý thông tin về khách hàng đã tìm thấy
            print("Thông tin về khách hàng:")
            print(f"Mã khách hàng: {data.ccode}")
            print(f"Tên khách hàng: {data.cus_name}")
            print(f"Số điện thoại: {data.phone}")
        else:
            print(f"Không có khách hàng nào có mã là {ccode}.")

    def delete_by_ccode(self, ccode):
        customer_deleted = self.customers.delete_by_ccode(ccode)
        if customer_deleted:
            print(f"Đã xóa thành công khách hàng có mã '{ccode}'.")
        else:
            print(f"Không tìm thấy khách hàng có mã '{ccode}'.")

    def has_customer(self, ccode):
        return self.customers.has_customer(ccode)      


