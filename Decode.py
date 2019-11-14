import Global_vars as gb

COMP_DICT = {"0": "110101010", "1": "110111111", "-1": "110111010", "D": "110001100", "A": "110110000",
             "!D": "110001101", "!A": "110110001", "-D": "110110011", "-A": "110001111", "D+1": "110011111",
             "A+1": "110110111", "D-1": "110001110", "A-1": "110110010", "D+A": "110000010", "D-A": "110010011",
             "A-D": "110000111", "D&A": "110000000", "D|A": "110010101", "M": "111110000", "!M": "111110001",
             "-M": "111110011", "M+1": "111110111", "M-1": "111110010", "D+M": "111000010", "D-M": "111010011",
             "M-D": "111000111", "D&M": "111000000", "D|M": "111010101", "D<<": "010110000", "A<<": "010100000",
             "M<<": "011100000", "D>>": "010010000", "A>>": "010000000", "M>>": "011000000"
             }

JMP_DICT = {"null": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110",
            "JMP": "111"}


def decode(inst):
    # receives one legal line and translates it to binary
    if inst[0] == '@':
        if inst[1:].isdigit():
            num = int(inst[1:])
        else:
            if inst[1:] not in gb.symbol_dict:
                gb.symbol_dict[inst[1:]] = gb.dict_count
                gb.dict_count += 1
            num = gb.symbol_dict[inst[1:]]

        return format(num, 'b').zfill(16)
    bin_inst = "1"
    dest = ""
    if "=" in inst:
        dest = inst.split("=")[0]

    jmp = "null"
    if ";" in inst:
        jmp = inst.split(";")[1]

    comp = inst.split("=")[-1].split(";")[0]
    bin_inst += COMP_DICT[comp]
    for ch in ["A", "D", "M"]:
        bin_inst += "1" if ch in dest else "0"
    bin_inst += JMP_DICT[jmp]

    return bin_inst
