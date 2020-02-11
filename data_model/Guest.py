class Guest(object):

    def __init__(self, id, first_name, last_name, reservation):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.reservation = reservation


class Reservation(object):

    def __init__(self, room_number, start_timestamp, end_timestamp):
        self.room_number = room_number
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp