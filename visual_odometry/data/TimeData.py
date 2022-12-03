class TimeData(object):
    """This class contains flight time taken."""
    flight_time_start = None
    flight_time_end = None
    flight_time = None
    
    def __init__(self):
        self.flight_time_start = 0
        self.flight_time_end = 0
        self.flight_time = 0

    def add_flight_start_time(self, time):
        self.flight_time_start = time
    
    def add_flight_stop_time(self, time):
        self.flight_time_end = time