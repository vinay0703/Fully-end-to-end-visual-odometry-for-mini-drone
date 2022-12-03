class LocationData(object):
    """This data class contains location data."""
    x_location = None
    y_location = None
    z_location = None
    location = None
    number_of_locations = None

    def __init__(self):
        self.x_location, self.y_location, self.z_location = 0, 0, 0
        self.location = [[0, 0, 0]]
        self.number_of_locations = 0