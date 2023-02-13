"""This class provides drone acceleration and velocity at particular location."""
class Location:
    def __init__(self, tello, location_data, acceleration_data, velocity_data, file_util, constants, threading, time, time_data, numpy):
        self.tello = tello
        self.location_data = location_data
        self.acceleration_data = acceleration_data
        self.velocity_data = velocity_data
        self.file_util = file_util
        self.constants = constants
        self.threading = threading
        self.time = time
        self.time_data = time_data
        self.numpy = numpy

        # constants for location capture threading
        self.stop_threads = None
        self.t1 = None
    
    def add_flight_start_time_data(self):
        self.time_data.add_flight_start_time(self.time.time())
    
    def add_flight_stop_time_data(self):
        self.time_data.add_flight_stop_time(self.time.time())

    def get_flight_time(self):
        self.time_data.flight_time = self.time_data.flight_time_end - self.time_data.flight_time_start
        print(self.time_data.flight_time)

    def calculate_location_matrix(self):
        # position data
        acc = self.acceleration_data.acceleration
        vel = self.velocity_data.velocity
        T = self.time_data.flight_time
        n = self.location_data.number_of_locations

        self.location_data.location = self.numpy.array(vel) * (T/n) + self.numpy.array(acc) * (1/2 * T/n * T/n)
        # -1 since the drone axes are aligned to -ve by default at first.
        self.location_data.location = self.numpy.add.accumulate(self.location_data.location*-1)
        # Height is considered as constant here bcz we considered constant in our training model.
        self.location_data.location[:,2] = self.constants.FLYING_HEIGHT

    def add_location_acceleration_velocity_to_matrix(self):
        # Velocity data
        self.velocity_data.x_velocity = self.tello.get_speed_x()
        self.velocity_data.y_velocity = self.tello.get_speed_y()
        self.velocity_data.z_velocity = self.tello.get_speed_z()
        self.velocity_data.add_velocity_data(self.velocity_data)
        
        # Acceleration data
        self.acceleration_data.x_acceleration = self.tello.get_acceleration_x()
        self.acceleration_data.y_acceleration = self.tello.get_acceleration_y()
        self.acceleration_data.z_acceleration = self.tello.get_acceleration_z()
        self.acceleration_data.add_acceleration_data(self.acceleration_data)

    def save_location_to_file(self):
        # Location data
        self.file_util.save_matrix_to_excel(self.location_data.location, self.constants.LOCATION_DATA_FILE_NAME)
        print(self.constants.CAPTURE_LOCATIONS_COMPLETE_MESSAGE, end=": ")
        print(self.location_data.number_of_locations)

    def save_acceleration_velocity_to_file(self):
        # Acceleration data
        self.file_util.save_matrix_to_excel(self.acceleration_data.acceleration, self.constants.ACCELERATION_DATA_FILE_NAME)
        print(self.constants.CAPTURE_ACCELERATION_COMPLETE_MESSAGE, end = ": ")
        print(self.acceleration_data.number_of_acceleration_data)

        # Velocity data
        self.file_util.save_matrix_to_excel(self.velocity_data.velocity, self.constants.VELOCITY_DATA_FILE_NAME)
        print(self.constants.CAPTURE_VELOCITY_COMPLETE_MESSAGE, end = ": ")
        print(self.velocity_data.number_of_velocity_data)

    def add_acceleration_velocity(self, stop):
        i = 1
        while True:
            self.add_location_acceleration_velocity_to_matrix()
            self.time.sleep(self.constants.CAPUTRE_INTERVAL_SEC)
            if stop():
                break
            i += 1
        self.acceleration_data.number_of_acceleration_data = i
        self.velocity_data.number_of_velocity_data = i
        self.location_data.number_of_locations = i
    
    def start_adding_acceleration_velocity(self):
        self.stop_threads = False
        self.t1 = self.threading.Thread(target = self.add_acceleration_velocity, args =(lambda : self.stop_threads, ))
        self.t1.start()

    def stop_adding_acceleration_velocity(self):        
        self.stop_threads = True
        self.t1.join()