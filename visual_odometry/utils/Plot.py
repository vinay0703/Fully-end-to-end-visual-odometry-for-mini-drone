"""This class is used to plot drone path in 3d."""
class Plot:
    def __init__(self, pd, plt, ani):
        self.pd = pd
        self.plt = plt
        self.ani = ani
    
    # Takes actual data and predicted data in excel format and plots in real time
    def live_plot_path(self, actual_location_data, predicted_location_data):
        def animate(i):
            if i >= len(actual_x):
                self.ani.event_source.stop()
            i += 1
            x1, y1, z1 = actual_x[:i], actual_y[:i], actual_z[:i]
            x2, y2, z2 = predicted_x[:i], predicted_y[:i], predicted_z[:i]
            self.plt.cla()

            ax.plot3D(x1, y1, z1, label='Channel 1')
            ax.plot3D(x2, y2, z2, label='Channel 2')

            self.plt.legend(loc='upper left')
            self.plt.tight_layout()

        self.plt.style.use('fivethirtyeight')
        ax = self.plt.axes(projection='3d')
        # Importing acutal co-ordinates 
        actual_df = self.pd.read_excel(actual_location_data, sheet_name=0)
        actual_x, actual_y, actual_z = list(actual_df['x']), list(actual_df['y']), list(actual_df['z']) 

        i = 0
        # Importing predicted co-ordinates
        predicted_df = self.pd.read_excel(predicted_location_data, sheet_name=0)
        predicted_x, predicted_y, predicted_z = list(predicted_df['x']), list(predicted_df['y']), list(predicted_df['z']) 


        self.ani = self.ani(self.plt.gcf(), animate, interval=1000, repeat = False)

        self.plt.tight_layout()
        self.plt.show()

    def plot_path(self, location_data):
        fig = self.plt.figure()
        ax = self.plt.axes(projection='3d')
        df = self.pd.read_excel(location_data, sheet_name=0)
        x, y, z = list(df['x']), list(df['y']), list(df['z'])
        ax.plot3D(x, y, z, label='Drone path') 
        self.plt.show()
