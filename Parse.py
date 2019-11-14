import Global_vars as gb

def lineHandler(line):
    line = line.strip(gb.NEW_LINE)
    line = line.strip(gb.TAB)
    line = line.strip(" ")
    for i in range(len(line) - 1):
        if line[i] + line[i + 1] == gb.COMMENT:
            line = line[:i]
            break

    if len(line) == 0:
        return

    if line[0] == gb.START and line[len(line) - 1] == gb.END:
        line = line[1:len(line) - 1]
        gb.symbol_dict[line] = len(gb.CLEAN_LINES)
        return

    gb.CLEAN_LINES.append(line)
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


