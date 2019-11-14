import Global_vars as gb

COMP_DICT = {"0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100", "A": "0110000", "!D": "0001101",
             "!A": "0110001", "-D": "0110011", "-A": "0001111", "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
             "A-1": "0110010", "D+A": "0000010", "D-A": "0010011", "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
             "M": "1110000", "!M": "1110001", "-M": "1110011", "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
             "D-M": "1010011", "M-D": "1000111", "D&M": "1000000", "D|M": "1010101"}

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
    bin_inst = "111"
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
