from visual_odometry.di import Dependency
class Drone(object):
    def __init__(self):
        self.dependecy = Dependency.Dependency()
        self.constants = self.dependecy.constants
        self.control = self.dependecy.control
        self.location = self.dependecy.location

    def fly_drone(self):
        battery_percentage = self.control.get_battery_percentage()
        print(self.constants.DISPLAY_BATTERY_PERCENTAGE, battery_percentage)
       
        # If battery less than threshold then abort takeoff
        if battery_percentage < self.constants.MINIMUM_BATTERY_PERCENTAGE:
            print(self.constants.ABORT_TAKEOFF_MESSAGE)
        else:
            print(self.constants.SEPERATE_LINE_MESSAGE)
            print(self.constants.CONTROL_MESSAGE, self.constants.CONTROL_CHOICE_MESSAGE)
            
            # Control methods
            user_control_choice = int(input())
            self.control.start_control(user_control_choice)
            print(self.constants.SEPERATE_LINE_MESSAGE)

            # Saving acceleration and velocity data
            self.location.save_acceleration_velocity_to_file()

            # Showing total flight time
            self.location.get_flight_time()

            # Saving location data
            self.location.calculate_location_matrix()
            self.location.save_location_to_file()

        print(self.constants.LAND_MESSAGE)

if __name__ == '__main__':
    drone = Drone()
    drone.fly_drone()