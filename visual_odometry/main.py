from visual_odometry.di import Dependency

class Drone(object):
    def __init__(self):
        self.dependency = Dependency.Dependency()
        self.constants = self.dependency.constants
        self.file_util = self.dependency.file_util
        self.plot = self.dependency.plot
        self.np = self.dependency.numpy
        self.tf = self.dependency.tf
        self.cv2 = self.dependency.cv2
        self.keras = self.dependency.keras
        
        # Model
        self.m = None

    def menu(self):
        # Intializing the GPU so that we can save the time later in prediction.
        print(self.constants.SEPERATE_LINE_MESSAGE)
        with self.tf.device('/GPU:0'):
            self.m = self.dependency.predict
            self.m.convnext()
        
        # Drone flight choices
        print(self.constants.DRONE_FLIGHT_CHOICE)
        choice = input()
        if(choice.lower() == "yes" or choice.lower() == "y"):
            self.dependency.init_drone_dependencies()
            self.control = self.dependency.control
            self.fly_drone()
        
        # Drone path prediction choices
        print(self.constants.PREDICT_PATH_CHOICE)
        choice = input()
        if(choice.lower() == "yes" or choice.lower() == "y"):
            self.predict()
        
        # Plotting the drone actual and predicted paths
        print(self.constants.PLOT_PATH_CHOICE )
        choice = input()
        if(choice.lower() == "yes" or choice.lower() == "y"):
            self.plot_data()
    
    # Function responsible for drone flight.
    def fly_drone(self):
        self.location = self.dependency.location
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
            self.control.stop_control()
        print(self.constants.LAND_MESSAGE)
      
    # Predicts the drone path
    def predict(self):
        print(self.constants.SEPERATE_LINE_MESSAGE)
        with self.tf.device('/GPU:0'):
            Y_pred = self.m.predict()
            self.file_util.save_matrix_to_excel(Y_pred[0, :, :], self.constants.PREDICTED_LOCATION_DATA_FILE_NAME)
            print("Predicted drone path")
        print(self.constants.SEPERATE_LINE_MESSAGE)

    # Plotting the paths.
    def plot_data(self):
        # Plotting drone path in 3d.
        def static_plot():
            self.plot.plot_path(self.constants.FOLDER_FOR_SAVING_FILE + self.constants.LOCATION_DATA_FILE_NAME,self.constants.FOLDER_FOR_SAVING_FILE + self.constants.PREDICTED_LOCATION_DATA_FILE_NAME)

        # Plotting live drone path in 3d.
        def plot_live_data():
            self.plot.live_plot_path(self.constants.FOLDER_FOR_SAVING_FILE + self.constants.LOCATION_DATA_FILE_NAME, self.constants.FOLDER_FOR_SAVING_FILE + self.constants.PREDICTED_LOCATION_DATA_FILE_NAME)
        
        print(self.constants.SEPERATE_LINE_MESSAGE)
        print(self.constants.PLOT_MESSAGE, self.constants.PLOT_CHOICE_MESSAGE)
        
        choice = int(input())
        if choice == 1:
            static_plot()
        else:
            plot_live_data()            


if __name__ == '__main__':
    # Initializing the drone object and calling the menu() function to display the menu.
    drone = Drone()
    drone.menu()