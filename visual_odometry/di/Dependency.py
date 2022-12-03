import djitellopy, cv2, threading, time, pygame, numpy, pandas
from visual_odometry.utils import Constants, Control, Location, File, Capture
from visual_odometry.data import LocationData, AccelerationData, VelocityData, TimeData

class Dependency(object):
    """This class is used to inject dependecies."""
    # Utilities
    constants, control, location, file_util, capture = None, None, None, None, None
    
    # Packages
    tello, cv2, threading, time, pygame, numpy, pandas = None, None, None, None, None, None, None
    
    # Data classes
    location_data, acceleration_data, velocity_data, time_data = None, None, None, None

    def __init__(self):
        # packages
        Dependency.tello = djitellopy.Tello()
        Dependency.cv2 = cv2
        Dependency.threading = threading
        Dependency.time = time
        Dependency.pygame = pygame
        Dependency.numpy = numpy
        Dependency.pandas = pandas

        # Data classes
        Dependency.location_data = LocationData.LocationData()
        Dependency.acceleration_data = AccelerationData.AccelerationData()
        Dependency.velocity_data = VelocityData.VelocityData()
        Dependency.time_data = TimeData.TimeData()

        # Utility classes
        Dependency.constants = Constants.Constants()
        Dependency.file_util = File.File(self.numpy, self.pandas, self.constants)
        Dependency.location = Location.Location(self.tello, self.location_data, self.acceleration_data, self.velocity_data, self.file_util, self.constants, self.threading, self.time, self.time_data, self.numpy)
        Dependency.capture = Capture.Capture(self.tello, self.threading, self.cv2, self.time, self.constants)
        Dependency.control = Control.Control(self.tello, self.constants, self.location, self.time, self.pygame, self.capture)