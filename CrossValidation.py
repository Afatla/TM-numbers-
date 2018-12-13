from sklearn.model_selection import KFold


class CrossValidation(object):
    def __init__(self, x, n_test):
        self.n_test_ = n_test
        self.x_ = x.T

    def get_split(self):
        kf = KFold(n_splits=int(len(self.x_)/self.n_test_))
        return kf.split(self.x_)