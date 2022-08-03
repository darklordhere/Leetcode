class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        for ls , le in self.booking:
            if ls < end and start < le:
                return False
        self.booking.append((start,end))
        return True