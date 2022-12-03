class VelocityData(object):
    """This data class contains velocity data."""
    x_velocity = None
    y_velocity = None
    z_velocity = None
    velocity = None
    number_of_velocity_data = None

    def __init__(self):
        self.x_velocity, self.y_velocity, self.z_velocity = 0, 0, 0
        self.velocity = [[0, 0, 0]]
        self.number_of_velocity_data = 0

    def add_velocity_data(self, velocity_data):
        self.velocity.append([velocity_data.x_velocity, velocity_data.y_velocity, velocity_data.z_velocity])