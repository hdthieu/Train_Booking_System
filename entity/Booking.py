class Booking:
    def __init__(self, tcode, ccode, seat):
        self._tcode = tcode
        self._ccode = ccode
        self._seat = seat

    @property
    def tcode(self):
        return self._tcode

    @tcode.setter
    def tcode(self, value):
        self._tcode = value

    @property
    def ccode(self):
        return self._ccode

    @ccode.setter
    def ccode(self, value):
        self._ccode = value

    @property
    def seat(self):
        return self._seat

    @seat.setter
    def seat(self, value):
        self._seat = value

    def __str__(self):
        return f"Booking: Train code - {self._tcode}, Customer code - {self._ccode}, Seats booked - {self._seat}"

# Example usage:
# booking1 = Booking("T001", "CC001", 2)
# booking2 = Booking("T002", "CC002", 1)

# print(booking1.tcode)
# print(booking2.ccode)

# booking1.seat = 3
# print(booking1.seat)

# print(booking1)
# print(booking2)
