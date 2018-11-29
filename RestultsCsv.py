""" this program is going to wirte results to csv"""

import csv


class ResultsCsv(object):
    # constructor

    def __init__(self, results_matrix, rr, name):
        self.name_ = name
        self.results_ = results_matrix
        self.rr_ = rr
    # methods

    def write_to_csv(self):

        with open(str(self.name_), mode='w') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for site in range(0, 11):
                site_file = self.results_[site]
                results_writer.writerow(['Crossvalidation type: '] + [str(site)])

                for each in site_file:
                    results_writer.writerow([str(each[0])] + [' recognised: '] + [str(each[1])])

                results_writer.writerow(['Recognition ratio: '] + [self.rr_[0, site]])

        results_file.close()