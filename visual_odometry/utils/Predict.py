import time
class Model(object):
    """This model contains cnn models."""
    np, tf, keras = None, None, None

    model, model_weights = None, None

    imgsize1, imgsize2 = None, None

    X, y_pred = None, None

    vidcap = None

    def __init__(self, np, tf, cv2, keras, pd, constants):
        self.np = np
        self.tf = tf
        self.cv2 = cv2
        self.keras = keras
        self.pd = pd
        self.folder = constants.FOLDER_FOR_SAVING_FILE
        self.model_folder = constants.FOLDER_FOR_WEIGHTS
        self.model_weights = self.model_folder + constants.WEIGHTS_FILE_NAME
        self.video_path = self.folder + constants.VIDEO_FILE_NAME
        self.path_position = self.folder + constants.LOCATION_DATA_FILE_NAME
        self.break_line_message = constants.SEPERATE_LINE_MESSAGE
        print(self.break_line_message)
        print("\tInitiating model")
        print(self.break_line_message)

    def show_model_summary(self):
        print(self.model.summary())

    def convnext(self):
        Sequential = self.keras.models.Sequential
        Dense, Flatten, Dropout = self.keras.layers.Dense, self.keras.layers.Flatten, self.keras.layers.Dropout
        
        self.imgsize1 = 128
        self.imgsize2 = 128
        
        def load_weights():
            self.model.load_weights(self.model_weights).expect_partial()
            # self.model.load_weights(self.model_weights)
            print(self.break_line_message)        
            print("\tLoaded model weights")
            print(self.break_line_message)


        def compile_model():
            self.model.compile(optimizer='adam', loss='mse')            
            print(self.break_line_message)        
            print("\tmodel compiled")
            print(self.break_line_message)        


        def intialize_model():
            vgg = self.tf.keras.applications.ConvNeXtBase(model_name="convnext_base",include_top=False,weights="imagenet",input_shape=(self.imgsize1,self.imgsize2,3))
            for layer in vgg.layers[:-4]:
                layer.trainable = False
            model = Sequential()
            model.add(self.tf.keras.layers.TimeDistributed(vgg, input_shape=(None, self.imgsize1, self.imgsize2, 3)))
            model.add(self.tf.keras.layers.TimeDistributed(Flatten()))
            model.add(self.tf.keras.layers.LSTM(1024, return_sequences = True))
            model.add(Dropout(0.2))
            model.add(self.tf.keras.layers.LSTM(1024, return_sequences = True))
            model.add(Dropout(0.2))
            model.add(self.tf.keras.layers.TimeDistributed(Dense(128, activation='linear')))
            model.add(self.tf.keras.layers.TimeDistributed(Dense(3, activation='linear')))
            self.model = model
            print(self.break_line_message)        
            print("\tConvNext model initiated")
            print(self.break_line_message)        
        
        intialize_model()
        compile_model()
        load_weights()
        

    def predict(self):
        def load_data():
            Ytemp = self.np.array(self.pd.read_excel('{}'.format(self.path_position), engine='openpyxl'))
            Y = self.np.zeros((1, Ytemp.shape[0], 3))
            Y[0,:,:] = self.np.copy(Ytemp)
            self.X = self.np.zeros((1, Y.shape[1], self.imgsize1, self.imgsize2, 3))
            self.vidcap = self.cv2.VideoCapture(self.video_path)
            vidlength = self.vidcap.get(self.cv2.CAP_PROP_FRAME_COUNT)/ self.vidcap.get(self.cv2.CAP_PROP_FPS)
            sec = 0
            frameRate = (vidlength / Y.shape[1])
            count = 1
            success = getFrame(sec)
            while success:
                sec += frameRate
                success, image = getFrame(sec)
                if image is not None :
                    img = self.cv2.resize(image, (self.imgsize1, self.imgsize2))
                    self.X[0,count,:,:,:] = self.np.copy(img)
                count += 1
        def getFrame(sec):
            self.vidcap.set(self.cv2.CAP_PROP_POS_MSEC, sec*1000)
            hasframes, image = self.vidcap.read()
            return hasframes, image
        
        load_data()
        print(self.break_line_message)        
        print("\tStarting model prediction")
        print(self.break_line_message)  
        start = time.time()
        self.y_pred = self.model(self.X)
        stop = time.time()
        print(stop-start)
        # self.y_pred = self.model.predict(self.X)
        # self.y_pred = self.model.predict_on_batch(self.X)
        print(self.break_line_message)        
        print("\tModel prediction done")
        print(self.break_line_message)        

        return self.y_pred