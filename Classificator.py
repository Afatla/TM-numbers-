import numpy as np


class Classificator(object):
    def __init__(self, mfcc_input, gmm_list_input):
        self.mfcc_ = mfcc_input
        self.gmm_list = gmm_list_input
        self.n_correct = 0

    # methods:
    def classify(self, mfcc_digit):
        scores_list = []
        for gmm in self.gmm_list:
            gmm = gmm.gmm_.score(self.mfcc_)
            scores_list.append(gmm)
        max_likelihood = np.max(scores_list)
        if scores_list.index(max_likelihood) == mfcc_digit:
            self.n_correct += 1
        return scores_list.index(max_likelihood)

    def get_RR(self, n_correct, n_all):
        return n_correct/n_all



