""" this is main commander of a program"""

import Commander

commander = Commander.Commander(path_folder="train")
commander.cross_test()
commander.write_to_csv()
print("program ended")