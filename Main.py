""" this is main commander of a program"""

import Commander

commander15 = Commander.Commander(path_folder="train", winlen=0.015)
commander15.cross_test()
commander15.write_to_csv(file_name="results_win_15")

commander20 = Commander.Commander(path_folder="train", winlen=0.020)
commander20.cross_test()
commander20.write_to_csv(file_name="results_win_20")

commander25 = Commander.Commander(path_folder="train", winlen=0.025)
commander25.cross_test()
commander25.write_to_csv(file_name="results_win_25")

commander30 = Commander.Commander(path_folder="train", winlen=0.030)
commander30.cross_test()
commander30.write_to_csv(file_name="results_win_30")

commander35 = Commander.Commander(path_folder="train", winlen=0.035)
commander35.cross_test()
commander35.write_to_csv(file_name="results_win_35")

commander40 = Commander.Commander(path_folder="train", winlen=0.040)
commander40.cross_test()
commander40.write_to_csv(file_name="results_win_40")

print("program ended")