""" This program will convert wave files to MFCC"""
import numpy as np
from python_speech_features import mfcc


class WaveToMfcc(object):

    def __init__(self, array, rate):
        self.wave_array_ = array
        self.rate_ = rate
        self.mfcc_array_ = self.create_mfcc()
        self.list_of_speakers = self.mfcc_array_[:, 10]

    def create_mfcc(self):
        mfcc_array = self.wave_array_
        for row in range(0, len(self.wave_array_)):
            for index in range(0, len(self.wave_array_[0]) - 1):
                 mfcc_array[row][index] = mfcc(self.wave_array_[row][index], self.rate_, appendEnergy=False)
        return mfcc_array

    def glue(self, indexes):
        output = []
        for i in range(0, 10):
            if not isinstance(indexes, np.int32):
                mfcc_i = self.mfcc_array_[indexes[0], i]
                indexes2 = np.delete(indexes, 0)
                for row in range(1, len(self.mfcc_array_)):
                    if row in indexes2:
                        mfcc_i = np.concatenate((mfcc_i, self.mfcc_array_[row][i]), axis=0)
            else:
                mfcc_i = self.mfcc_array_[indexes, i]
            output.append(mfcc_i)
        return output

    def glue_all(self):
        output = []
        for i in range(0, 10):
            mfcc_i = self.mfcc_array_[0, i]
            for row in range(1, len(self.mfcc_array_)):
                mfcc_i = np.concatenate((mfcc_i, self.mfcc_array_[row][i]), axis=0)
            output.append(mfcc_i)
        return output