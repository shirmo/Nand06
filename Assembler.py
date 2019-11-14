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

    for inst in gb.CLEAN_LINES:
        dc.decode(inst)