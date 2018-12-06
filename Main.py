"""" this is main commander of a program"""

import Commander

commander = Commander.Commander(path_folder="train", winlen=0.015)
commander.cross_test()
commander.write_to_csv('results.csv')
print("program ended")