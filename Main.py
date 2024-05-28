from management.TrainManagement import TrainManagement
from management.CustomerManagement import CustomerManagement
from management.BookingManagement import BookingManagement
def main_menu():
    trainManagement = TrainManagement()
    customer_list = CustomerManagement()
    booking_list = BookingManagement()

    while True:
        print("\nMain Menu")
        print("1. Train list")
        print("2. Customer list")
        print("3. Booking list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            train_menu(trainManagement)
        elif choice == '2':
            customer_menu(customer_list)
        elif choice == '3':
            booking_menu(trainManagement, customer_list, booking_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


def train_menu(trainManagement):
    while True:
        print("\nMain Menu Train List")
        print("1 - Load data from file")
        print("2 - Add train to head")
        print("3 - Display trains")
        print("4 - Save train list to file")
        print("5 - Search by train code")
        print("6 - Delete by tcode")
        print("7 - Sort by tcode")   
        print("8 - Add after position k")
        print("9 - Delete the node before the node having tcode = xCode")
        print("10 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the file name to load data from: ")
            trainManagement.load_data(filename)
        elif choice == '2':
            trainManagement.add_train()
        elif choice == '3':
            trainManagement.display_trains()
        elif choice == '4':
            filename = input("Enter the file name to save data to: ")
            trainManagement.save_data(filename)
        elif choice == '5':
            searchTcode = input("Nhập vào TCode: ")
            train_data = trainManagement.searchByTcode(searchTcode)
            if train_data:
                print(f"Train found: Tcode: {train_data.tcode}, Train name: {train_data.tname}, Seat: {train_data.seat}, Booked: {train_data.booked}, Departure time: {train_data.depart_time}, Departure place: {train_data.depart_place}, Available seat: {train_data.available_seat}")
            else:
                print("Không tìm thấy.")
        elif choice == '6':
            tCodeDelete = input("Nhập vào TCode: ")
            trainManagement.delete_by_tcode(tCodeDelete)
        elif choice == '7':
            print("TCode đã được sort")
            trainManagement.sort_trains_by_tcode()
            trainManagement.display_trains()
        elif choice == '8':
            positionK =int(input("Nhập vào position k: "))  
            print("Add after position k")
            trainManagement.add_train_after_position(positionK)
        elif choice == '9':
            xCode = input("Nhập vào TCode của nút muốn xóa nút trước đó: ")
            trainManagement.delete_before_tcode(xCode)
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

def customer_menu(customer_list):
    while True:
        print("\nMain Menu Customer List")
        print("1 - Load data from file")
        print("2 - Input & add to the end ")
        print("3 - Display data customer")
        print("4 - Save customer list to file ")
        print("5 - Search by ccode")
        print("6 - Delete by ccode")
        print("7 - Exit")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            #filename = input("Enter the file name to load data from: ")
            customer_list.load_data('customers.csv')
        elif choice == '2':
            customer_list.add_customer()
        elif choice == '3':
            customer_list.display_customers()
        elif choice == '4':
            #filename = input("Enter the file name to save data to: ")
            customer_list.save_data('customers.csv')
        elif choice == '5':
            searchCcode = input("Nhập vào Ccode: ")
            customer_list.search_by_ccode(searchCcode)
        elif choice == '6':
            CcodeDelete = input("Nhập vào Ccode: ")
            customer_list.delete_by_ccode(CcodeDelete)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

def booking_menu(trainManagement, customer_list, booking_list):
    while True:
        print("\nMain Menu Booking Menu")
        print("1 - Input data")
        print("2 - Display data width available seats")
        print("3 - Sort by tcode + ccode")
        print("4 - Exit")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
                    tcode = input("Nhập mã tàu: ")
                    ccode = input("Nhập mã khách hàng: ")
                    while True:
                        seats_input = input("Nhập số lượng ghế muốn đặt: ")
                        if seats_input.isdigit():
                            seats = int(seats_input)
                            break
                        else:
                            print("Số lượng ghế phải là một số nguyên dương. Vui lòng nhập lại.") 
                    booking_list.input_booking(tcode, ccode, seats, trainManagement, customer_list)

        elif choice == '2':
            booking_list.display_bookings(trainManagement)
        elif choice == '3':
            print("Đã sắp xếp theo TCode + CCode.")
            booking_list.sort_bookings_by_tcode()
            booking_list.display_bookings(trainManagement)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()