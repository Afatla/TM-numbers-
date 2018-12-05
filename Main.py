"""" this is main commander of a program"""

import Commander

commander = Commander.Commander(path_folder="train", winlen=0.005)
commander.cross_test()
commander.write_to_csv('results_win05.csv')

commander = Commander.Commander(path_folder="train", winlen=0.010)
commander.cross_test()
commander.write_to_csv('results_win10.csv')

commander = Commander.Commander(path_folder="train", winlen=0.015)
commander.cross_test()
commander.write_to_csv('results_win15.csv')

commander = Commander.Commander(path_folder="train", winlen=0.020)
commander.cross_test()
commander.write_to_csv('results_win20.csv')

commander = Commander.Commander(path_folder="train", winlen=0.025)
commander.cross_test()
commander.write_to_csv('results_win25.csv')

commander = Commander.Commander(path_folder="train", winlen=0.030)
commander.cross_test()
commander.write_to_csv('results_win30.csv')

commander = Commander.Commander(path_folder="train", winlen=0.035)
commander.cross_test()
commander.write_to_csv('results_win35.csv')

commander = Commander.Commander(path_folder="train", winlen=0.040)
commander.cross_test()
commander.write_to_csv('results_win40.csv')

print("program ended")
