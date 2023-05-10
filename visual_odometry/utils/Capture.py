"""This class is related to video and image capture from drone."""
class Capture:
    def __init__(self, tello, threading, cv2, time, constants):
        self.tello = tello
        self.threading = threading
        self.cv2 = cv2
        self.time = time
        self.constants = constants
        
        # recorder threads
        self.recorder = None
        self.frame_read = None
        self.keepRecording = None  

    # Records the drone feed and shows the drone feed.
    def videoRecorder(self):
        height, width, _ = self.frame_read.frame.shape
        fps = self.constants.VIDEO_FPS
        file_name = self.constants.FOLDER_FOR_SAVING_FILE + self.constants.VIDEO_FILE_NAME
        video = self.cv2.VideoWriter(file_name, self.cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
        while self.keepRecording:
            video.write(self.frame_read.frame)
            self.cv2.imshow('feed', self.frame_read.frame)
            self.cv2.waitKey(1)
            self.time.sleep(1/fps)
        video.release()
        self.cv2.destroyAllWindows()

    # Starts the recorder thread
    def start_recording_video(self, frame_read):
        self.keepRecording = True 
        self.frame_read = frame_read 
        self.recorder = self.threading.Thread(target=self.videoRecorder)
        self.recorder.start()

    # Joins the recorder thread.
    def stop_recording_video(self):
        self.keepRecording = False
        self.recorder.join()