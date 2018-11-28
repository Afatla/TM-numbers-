"""this is wave file connector and reader"""

import scipy.io.wavfile as wav
import numpy as np
import os


class WaveReader(object):

    def __init__(self, path_folder):
        self.path_folder_ = path_folder

    def read_all(self):
        matrix = np.zeros((22, 10), dtype=object)
        names = np.chararray((22, 1), itemsize=5, unicode=True)
        rate = 0
        for i in range(0, 10):
            i2 = 0
            for file in os.listdir(self.path_folder_):
                if file.endswith("" + str(i) + '_.wav'):
                    path = os.path.join(self.path_folder_, file)
                    (rate, number_1) = wav.read(path)
                    matrix[i2][i] = number_1
                    i2 = i2 + 1
                    if i == 9:
                        filename, file_extension = os.path.splitext(os.path.basename(path))
                        name = filename[0:-3]
                        names[i2 - 1, 0] = name
        matrix = np.concatenate((matrix, names), axis=1)
        return (matrix, rate)