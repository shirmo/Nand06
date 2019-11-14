import Global_vars as gb


def decode(inst):
    """
    receives a legal line and translates it to binary
    :param inst: line in english
    :return: line in binary
    """
    if inst[0] == '@':
        # A instruction
        if inst[1:].isdigit():
            num = int(inst[1:])
        else:
            if inst[1:] not in gb.symbol_dict:  # this a symbol, add to or read from dict.
                gb.symbol_dict[inst[1:]] = gb.dict_count
                gb.dict_count += 1
            num = gb.symbol_dict[inst[1:]]
        return format(num, 'b').zfill(16)

    bin_inst = "1"
    # C instruction
    dest = ""
    if "=" in inst:
        dest = inst.split("=")[0]

    jmp = "null"
    if ";" in inst:
        jmp = inst.split(";")[1]

    comp = inst.split("=")[-1].split(";")[0]
    bin_inst += gb.COMP_DICT[comp]
    for ch in ["A", "D", "M"]:
        bin_inst += "1" if ch in dest else "0"
    bin_inst += gb.JMP_DICT[jmp]

    return bin_inst
