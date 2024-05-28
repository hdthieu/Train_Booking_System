class Train:
    def __init__(self, tcode, tname, seat, booked, depart_time, depart_place):
        self.tcode = tcode
        self.tname = tname
        self.seat = seat
        self.booked = booked
        self.depart_time = depart_time  
        self.depart_place = depart_place

    @property
    def tcode(self):
        return self._tcode

    @tcode.setter
    def tcode(self, value):
        self._tcode = value

    @property
    def tname(self):
        return self._tname

    @tname.setter
    def tname(self, value):
        self._tname = value

    @property
    def seat(self):
        return self._seat

    @seat.setter
    def seat(self, value):
        if value <= 0:
            raise ValueError("Số lượng ghế phải lớn hơn 0.")
        self._seat = value

    @property
    def booked(self):
        return self._booked

    @booked.setter
    def booked(self, value):
        if value < 0:
            raise ValueError("Số chỗ đã đặt phải lớn hơn hoặc bằng 0.") 
        if value > self.seat:  
            raise ValueError("Số chỗ đã đặt phải nằm trong khoảng từ 0 đến tổng số chỗ.")
        self._booked = value

    @property
    def depart_time(self):
        return self._depart_time

    @depart_time.setter
    def depart_time(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Thời gian khởi hành phải là một giá trị không âm.")
        self._depart_time = value
        

    @property
    def depart_place(self):
        return self._depart_place

    @depart_place.setter
    def depart_place(self, value):
        self._depart_place = value

    @property
    def available_seat(self):
        return self._seat - self._booked