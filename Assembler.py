import os
import sys
import glob

import Decode as dc
import Parse as pr
import Global_vars as gb



def main(argv):
    """
    Main function, operates the varies components of the program and connects between them.
    """
    if len(argv) < 2:
        raise Exception("no path given")

    path = sys.argv[1]
    if os.path.isfile(path):
        files = [path]
    elif os.path.isdir(path):
        files = glob.iglob(os.path.join(path, "*.asm"))
    else:
        raise Exception("invalid path")

    for file in files:
        pr.fileReader(file)
        new_file = file[:len(file) - 3] + "hack"
        f = open(new_file, "a+")
        for inst in gb.CLEAN_LINES:
            line = dc.decode(inst) + gb.NEW_LINE
            f.write(line)
        f.close()

if __name__ == "__main__":
    main(sys.argv)

