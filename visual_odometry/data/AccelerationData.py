class AccelerationData(object):
    """This data class contains acceleration data."""
    x_acceleration = None
    y_acceleration = None
    z_acceleration = None
    acceleration = None
    number_of_acceleration_data = None

    def __init__(self):
        self.x_acceleration, self.y_acceleration, self.z_acceleration = 0, 0, 0
        self.acceleration = [[0, 0, 0]]
        self.number_of_acceleration_data = 0

    def add_acceleration_data(self, acceleration_data):
        self.acceleration.append([acceleration_data.x_acceleration, acceleration_data.y_acceleration, acceleration_data.z_acceleration])