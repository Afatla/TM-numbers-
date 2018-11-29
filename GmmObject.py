"""this program is going to trainning data drom MFCC input"""

import sklearn.mixture.gaussian_mixture


class GmmObject(object):

    # constructor
    def __init__(self, n_components, mfcc_input):
        self.gmm_ = sklearn.mixture.gaussian_mixture.GaussianMixture(n_components=n_components, random_state=3)
        self.untrained = True
        self.mfcc_ = mfcc_input

    # methods:
    def train_data(self):
        self.gmm_.fit(self.mfcc_)
        self.untrained = False
        print("Training successful")
        print("number of iterations: " + str(self.gmm_.n_iter_))

    def recognize(self, mfcc_input):
        if self.untrained:
            print("GMM object wasn't trained yet!")
            return -99999
        else:
            return self.gmm_.score(mfcc_input)