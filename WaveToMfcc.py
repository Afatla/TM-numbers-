""" This program will convert wave files to MFCC"""
import numpy as np
from python_speech_features import mfcc
import librosa.feature

class WaveToMfcc(object):

    def __init__(self, array, rate, winlen, nfilt, ncep):
        if winlen != None:
            self.winlen_ = winlen
        else:
            self.winlen_ = 0.025
        if nfilt != None:
            self.nfilt_ = nfilt
        else:
            self.nfilt_ = 26
        if ncep != None:
            self.ncep_ = ncep
        else:
            self.ncep_ = 13
        self.wave_array_ = array
        self.rate_ = rate
        self.mfcc_array_ = self.create_mfcc(self.winlen_, self.nfilt_, self.ncep_)
        self.list_of_speakers = self.mfcc_array_[:, 10]

    def create_mfcc(self, winlen_, nfilt_, numcep_):
        mfcc_array = self.wave_array_
        mfcc_delta_array = mfcc_array
        mfcc_delta_array2 = mfcc_array
        for row in range(0, len(self.wave_array_)):
            for index in range(0, len(self.wave_array_[0]) - 1):
                mfcc_i = mfcc(self.wave_array_[row][index], self.rate_, appendEnergy=False, winlen=winlen_,
                              nfilt=nfilt_, numcep=numcep_)
                mfcc_array[row][index] = mfcc(self.wave_array_[row][index], self.rate_, appendEnergy=False,
                                              winlen=winlen_, nfilt=nfilt_, numcep=numcep_)

                # Cepstral Mean Substraction

                #if index != len(self.wave_array_[0]) - 1:
                    #mfcc_array[row][index] -= np.mean(mfcc_array[row][index], axis=0)

                # Cepstral Mean Variance Normalisation

                #if index != len(self.wave_array_[0]) - 1:
                    #mfcc_array[row][index] -= np.mean(mfcc_array[row][index], axis=0)
                    #mfcc_array[row][index] = mfcc_array[row][index]/np.std(mfcc_array[row][index])

                # delta and delta-delta

                mfcc_delta_array[row][index] = librosa.feature.delta(mfcc_array[row][index])
                mfcc_delta_array2[row][index] = librosa.feature.delta(mfcc_array[row][index], order=2)

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