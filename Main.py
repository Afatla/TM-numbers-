"""" this is main commander of a program"""

import Commander


commander = Commander.Commander(path_folder="train", winlen=0.015)
commander.eval_test()
commander.write_to_csv_else('results.csv')

print("program ended")