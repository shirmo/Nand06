import os
import sys

import Decode as dc
import Parse as pr
import Global_vars as gb

if __name__ == "__main__":
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        sys.exit()
    pr.fileReader(filepath)

    new_file = filepath.strip("asm") + ".hack"
    f = open(new_file, "a+")
    for inst in gb.CLEAN_LINES:
        line = dc.decode(inst)
        f.write(line)
    f.close()