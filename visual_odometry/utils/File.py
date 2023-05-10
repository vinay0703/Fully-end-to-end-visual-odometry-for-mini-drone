class File:
    """This class is used to save information to file."""
    def __init__(self, numpy, pandas, constants):
        self.numpy = numpy
        self.pandas = pandas
        self.constants = constants

    # Saves matrix into excel file into respected location.
    def save_matrix_to_excel(self, matrix, file_name):
        matrix = self.numpy.array(matrix)
        
        x = self.numpy.array(matrix[:, 0])
        y = self.numpy.array(matrix[:, 1])
        z = self.numpy.array(matrix[:, 2])
        
        df = self.pandas.DataFrame({'x': x, 'y': y, 'z':z})

        file_name = self.constants.FOLDER_FOR_SAVING_FILE + file_name
        writer = self.pandas.ExcelWriter(file_name)
        df.to_excel(writer, 'Sheet1', index=False)
        writer.save()