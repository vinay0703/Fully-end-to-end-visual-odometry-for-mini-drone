"""This class contains all constants used in this project"""
class Constants(object):
    # File save constants
    FOLDER_FOR_SAVING_FILE = None
    LOCATION_DATA_FILE_NAME = None
    ACCELERATION_DATA_FILE_NAME = None
    VELOCITY_DATA_FILE_NAME = None
    VIDEO_FILE_NAME = None
    VIDEO_FPS = None

    # Battery constants
    MINIMUM_BATTERY_PERCENTAGE = None

    # Pygame window constants
    PYGAME_WIN_X, PYGAME_WIN_Y = None, None
    PYGAME_WIN_FONT_SIZE = None
    PYGAME_WIN_TEXT = None
    PYGAME_KEY_PRESS_INTERVAL_SEC = None

    # Colors
    WHITE, GREEN, BLUE = None, None, None

    # Constants used in drone path
    POLYGON_PATH_EDGE_LENGTH = None
    MANUAL_CONTROL_SENSITIVITY = None
    POLYGON_PATH_SIDES = None
    ZIG_ZAG_PATH_STEPS = None
    PATH_ANGLE = None
    FLYING_HEIGHT = None

    # Constants for capturing images and locations
    CAPUTRE_INTERVAL_SEC = None

    # Messages for displaying on screen
    CONTROL_MESSAGE = None
    CONTROL_CHOICE_MESSAGE = None
    SEPERATE_LINE_MESSAGE = None
    CAPTURE_LOCATIONS_COMPLETE_MESSAGE = None
    CAPTURE_ACCELERATION_COMPLETE_MESSAGE = None
    CAPTURE_VELOCITY_COMPLETE_MESSAGE = None
    ABORT_TAKEOFF_MESSAGE = None
    LAND_MESSAGE = None

    def __init__(self):
        # File save constants
        Constants.FOLDER_FOR_SAVING_FILE = "visual_odometry/files/"
        Constants.LOCATION_DATA_FILE_NAME = "location.xlsx"
        Constants.ACCELERATION_DATA_FILE_NAME = "acceleration.xlsx"
        Constants.VELOCITY_DATA_FILE_NAME = "velocity.xlsx"
        Constants.VIDEO_FILE_NAME = "video.avi"
        Constants.VIDEO_FPS = 30

        # Battery constants
        Constants.MINIMUM_BATTERY_PERCENTAGE = 10

        # Pygame window constants
        Constants.PYGAME_WIN_X = 400
        Constants.PYGAME_WIN_Y = 400
        Constants.PYGAME_WIN_FONT_SIZE = 32
        Constants.PYGAME_WIN_TEXT = "Manual control on"
        Constants.PYGAME_KEY_PRESS_INTERVAL_SEC = 0.05

        Constants.WHITE = (255, 255, 255)
        Constants.GREEN = (0, 255, 0)
        Constants.BLUE = (0, 0, 128)

        # Constants used in drone path
        Constants.MANUAL_CONTROL_SENSITIVITY = 60
        Constants.POLYGON_PATH_EDGE_LENGTH = 60
        Constants.POLYGON_PATH_SIDES = 3
        Constants.ZIG_ZAG_PATH_STEPS = 2
        Constants.PATH_ANGLE = 60
        Constants.FLYING_HEIGHT = 50

        # Constants for capturing location and images
        Constants.CAPUTRE_INTERVAL_SEC = 0.005

        # Messages for displaying on screen
        Constants.CONTROL_MESSAGE = "How do you like to control drone?"
        Constants.CONTROL_CHOICE_MESSAGE = "\n1)Predefined polygon path\n2)Predefined zig zag path\n3)Manual control drone\nEnter your choice: "
        Constants.SEPERATE_LINE_MESSAGE = "**************************************"
        Constants.CAPTURE_LOCATIONS_COMPLETE_MESSAGE = "Captured locations"
        Constants.CAPTURE_ACCELERATION_COMPLETE_MESSAGE = "Captured acceleration"
        Constants.CAPTURE_VELOCITY_COMPLETE_MESSAGE = "Captured velocity"
        Constants.DISPLAY_BATTERY_PERCENTAGE = "Battery percentage is: "
        Constants.ABORT_TAKEOFF_MESSAGE = "Takeoff aborted!"
        Constants.LAND_MESSAGE = "Successfully landed!"