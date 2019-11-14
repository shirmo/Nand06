import os
import sys

import Global_vars as gb
CO = {
    "C": [1],
    "A": [0]
}

CLEAN_LINES = []
START = "("
END = ")"
COMMENT = "//"
NEW_LINE = "\n"
TAB = "\t"


def lineHandler(line):
    line = line.strip(NEW_LINE)
    line = line.strip(TAB)
    line = line.strip(" ")
    for i in range(len(line) - 1):
        if line[i] + line[i + 1] == COMMENT:
            line = line[:i]
            break

    if len(line) == 0:
        return

    if line[0] == START and line[len(line) - 1] == END:
        line = line[1:len(line) - 1]
        gb.symbol_dict[line] = len(CLEAN_LINES)
        return
    CLEAN_LINES.append(line)
    return


def fileReader(file):
    with open(file) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            lineHandler(line)
            line = fp.readline()
            cnt += 1
        fp.close()


def main():
   filepath = sys.argv[1]
   if not os.path.isfile(filepath):
       sys.exit()
   fileReader(filepath)
   for i in CLEAN_LINES:
       print(i)


if __name__ == "__main__":
    main()