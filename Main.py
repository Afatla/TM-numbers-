""" this is main commander of a program"""

import Commander


commander = Commander.Commander(path_folder="train")
commander.cross_test()
print("program ended")