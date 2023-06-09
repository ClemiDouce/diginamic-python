# import argparse
from pyperclip import copy, paste
#
# argParser = argparse.ArgumentParser()
# argParser.add_argument("")
import os
from os.path import isfile, join

file_list = [f for f in os.listdir("./") if isfile(join("./", f)) and f.endswith(".dat")]

final_str = "plot "
for index, file in enumerate(file_list):
    title = "-".join(file.split("_")[2:]).capitalize()[:-4]
    if index == len(file_list)-1:
        final_str += f'"{file}" using 1:2 title "{title}" with lines'
    else:
        final_str += f'"{file}" using 1:2 title "{title}" with lines, \\\n'

copy(final_str)
print(f"La commande suivante a été copié dans votre presse papier :\n{final_str}")