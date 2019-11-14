from Global_vars import *

CO = {
    "C":[1],
    "A":[0]
}


CLEAN_LINES = []
START = "("
END = ")"
COMMENT = "//"

def lineHandler(line):
    line.stip()

    for i in range(len(line)-1):
        if line[i]+line[i+1] == COMMENT:
            line = line[:i]
            break
    if len(line) == 0:
        return 0
    if line[0] == START and line[len(line) - 1] == END:
        symbol_dict[line[1:len(line) - 1]] = len(CLEAN_LINES)
