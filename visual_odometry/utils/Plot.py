"""This class is used to plot drone path in 3d."""
class Plot:
    def __init__(self, pd, plt, ani):
        self.pd = pd
        self.plt = plt
        self.ani = ani
    
    # Takes actual data and predicted data in excel format and plots in real time
    def live_plot_path(self, actual_location_data, predicted_location_data):
        self.plt.style.use('fivethirtyeight')
        ax = self.plt.axes(projection='3d')
        
        # Importing acutal co-ordinates 
        actual_df = self.pd.read_excel(actual_location_data, sheet_name=0)
        actual_x, actual_y, actual_z = list(actual_df['x']), list(actual_df['y']), list(actual_df['z']) 

        # Importing predicted co-ordinates
        predicted_df = self.pd.read_excel(predicted_location_data, sheet_name=0)
        predicted_x, predicted_y, predicted_z = list(predicted_df['x']), list(predicted_df['y']), list(predicted_df['z']) 

        i = 0
        
        def animate(i):
            if i >= len(actual_x):
                self.ani.event_source.stop()
            i += 1
            x1, y1, z1 = actual_x[1:i], actual_y[1:i], actual_z[1:i]
            x2, y2, z2 = predicted_x[1:i], predicted_y[1:i], predicted_z[1:i]
            self.plt.cla()
            ax.plot3D(x1, y1, z1, label='Actual path')
            ax.plot3D(x2, y2, z1, label='Predicted path')
            ax.set_xlim([min(min(x1), min(x2)), max(max(x1), max(x2))])
            self.plt.legend(loc='upper left')
            self.plt.tight_layout()

        self.ani = self.ani(self.plt.gcf(), animate, interval=1, repeat = False)
        self.plt.tight_layout()
        self.plt.show()

    # Static plots that plots the actual and predicted paths.
    def plot_path(self, actual_location_data, predicted_location_data):
        fig = self.plt.figure()
        ax = self.plt.axes(projection='3d')
        df1 = self.pd.read_excel(actual_location_data, sheet_name=0)
        df2 = self.pd.read_excel(predicted_location_data, sheet_name=0)
        x1, y1, z1 = list(df1['x']), list(df1['y']), list(df1['z'])
        x2, y2, z2 = list(df2['x']), list(df2['y']), list(df2['z'])
        ax.plot3D(x1, y1, z1, label='Actual path') 
        ax.plot3D(x2, y2, z1, label='Predicted path') 
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        self.plt.show()
