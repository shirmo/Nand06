import Global_vars as gb


def lineHandler(line):
    """
    receives a string, removes all white spaces + allocates memory space to symbols
    :param line: a string of a line from the given asm file
    :return: void
    """
    line = line.strip(gb.NEW_LINE)
    line = line.strip(gb.TAB)
    for i in range(len(line) - 1):
        if line[i] + line[i + 1] == gb.COMMENT:
            line = line[:i]
            break
    line = line.replace(" ","")
    if len(line) == 0:
        return

    if line[0] == gb.START and line[len(line) - 1] == gb.END:
        line = line[1:len(line) - 1]
        gb.symbol_dict[line] = len(gb.CLEAN_LINES)  # Symbols memory allocation
        return
    gb.CLEAN_LINES.append(line)
    return


def fileReader(file):
    """
    Opens the given file, reads line after line and sends it to lineHandler method
    :param file: the path of the given file from argv[1]
    :return: void
    """
    with open(file) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            lineHandler(line)
            line = fp.readline()
            cnt += 1
        fp.close()


