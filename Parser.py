import Global_vars as gb
CO = {
    "C": [1],
    "A": [0]
}

CLEAN_LINES = []
START = "("
END = ")"
COMMENT = "//"


def lineHandler(line):
    line.strip()

    for i in range(len(line) - 1):
        if line[i] + line[i + 1] == COMMENT:
            line = line[:i]
            break

    if len(line) == 0:
        return

    if line[0] == START and line[len(line) - 1] == END:
        line = line[1:len(line) - 1]
        symbol_dict[line] = len(CLEAN_LINES)
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
