"""This class is related to drone controls."""
class Control:
    def __init__(self, tello, constants, location, time, pygame, capture):
        # Drone classes
        self.tello = tello
        self.tello.connect()
        self.tello.streamon()
        self.frame_read = self.tello.get_frame_read()

        # Utilities
        self.constants = constants
        self.location = location
        self.capture = capture

        # Packages
        self.time = time
        self.pygame = pygame
    
    def get_battery_percentage(self):
        return self.tello.get_battery()

    def start_control(self, control_choice):
        if control_choice == 1 or control_choice == 2:
            self.tello.takeoff()
            self.tello.move_up(self.constants.FLYING_HEIGHT)
            self.capture.start_recording_video(self.frame_read)
            self.location.add_flight_start_time_data()
            self.location.start_adding_acceleration_velocity()
            if control_choice == 1: self.polygon_path()
            elif control_choice == 2: self.zig_zag_path()
            self.capture.stop_recording_video()
            self.location.add_flight_stop_time_data()
            self.location.stop_adding_acceleration_velocity()
            self.tello.land()
        elif control_choice == 3: self.manual_control()

    def polygon_path(self):
        n = self.constants.POLYGON_PATH_SIDES
        l = self.constants.POLYGON_PATH_EDGE_LENGTH
        for _ in range(n):
            self.tello.move_forward(l)
            self.tello.rotate_clockwise(360//n)
    
    def manual_control(self):
        def start():
            self.pygame.init()
            X, Y = self.constants.PYGAME_WIN_X, self.constants.PYGAME_WIN_Y
            white = self.constants.WHITE
            green = self.constants.GREEN
            blue = self.constants.BLUE
            display_surface = self.pygame.display.set_mode((X, Y))
            self.pygame.display.set_caption('Show Text')
            font = self.pygame.font.Font('freesansbold.ttf', self.constants.PYGAME_WIN_FONT_SIZE)
            display_text = self.constants.PYGAME_WIN_TEXT
            text = font.render(display_text, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            
            while True:
                display_surface.fill(white)
                display_surface.blit(text, textRect)
                vals = keymap()
                self.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
                if vals[5] == 1: break
                self.time.sleep(self.constants.PYGAME_KEY_PRESS_INTERVAL_SEC)

        def getKey(keyName):
            ans = False
            for event in self.pygame.event.get(): 
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
                    # quit()
                self.pygame.display.update() 
            keyInput = self.pygame.key.get_pressed()
            myKey = getattr(self.pygame, 'K_{}'.format(keyName))
            if keyInput[myKey]:
                ans = True
            self.pygame.display.update()
            return ans

        def keymap():
            lr, fb, ud, vy, takeoff_flag, land_flag = 0, 0, 0, 0, 0, 0
            speed = self.constants.MANUAL_CONTROL_SENSITIVITY
            if getKey("LEFT"):
                lr = -speed
            elif getKey("RIGHT"):
                lr = speed
            elif getKey("UP"):
                fb = speed
            elif getKey("DOWN"):
                fb = -speed
            elif getKey("w"):
                ud = speed
            elif getKey("s"):
                ud = -speed
            elif getKey("a"):
                vy = -speed
            elif getKey("d"):
                vy = speed
            
            if getKey("t"):
                self.tello.takeoff()
                # Start adding locations after takeoff
                if(takeoff_flag == 0):
                    self.capture.start_recording_video(self.frame_read)
                    self.location.add_flight_start_time_data()
                    self.location.start_adding_acceleration_velocity()
                    takeoff_flag = 1
            elif getKey("l") or getKey("q"):
                self.tello.land()
                # Stop adding locations after landing
                if(land_flag == 0):
                    self.capture.stop_recording_video()
                    self.location.add_flight_stop_time_data()
                    self.location.stop_adding_acceleration_velocity()
                    land_flag = 1
            return [lr, fb, ud, vy, takeoff_flag, land_flag]

        start() 

    def zig_zag_path(self):
        steps = self.constants.ZIG_ZAG_PATH_STEPS
        l = self.constants.POLYGON_PATH_EDGE_LENGTH
        for i in range(steps):
            if(i % 2 == 0): self.tello.move_right(l)
            else: self.tello.move_left(l)
            self.tello.move_forward(l)