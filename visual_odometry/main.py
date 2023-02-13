from visual_odometry.di import Dependency
class Drone(object):
    def __init__(self):
        self.dependency = Dependency.Dependency()
        self.constants = self.dependency.constants
        self.control = self.dependency.control
        self.location = self.dependency.location
        self.plot = self.dependency.plot

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

            # Plotting live drone path in 3d.
            # self.plot.live_plot_path(self.constants.FOLDER_FOR_SAVING_FILE + self.constants.LOCATION_DATA_FILE_NAME, self.constants.FOLDER_FOR_SAVING_FILE + self.constants.LOCATION_DATA_FILE_NAME)

            # Plotting drone path in 3d.
            self.plot.plot_path(self.constants.FOLDER_FOR_SAVING_FILE + self.constants.LOCATION_DATA_FILE_NAME)

        print(self.constants.LAND_MESSAGE)

if __name__ == '__main__':
    drone = Drone()
    drone.fly_drone()