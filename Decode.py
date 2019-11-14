import Global_vars as gb


def decode(inst):
    # recieves one legal line and translates it to binary
    if inst[0] == '@':
        if inst[1:].isdigit():
            num = int(inst[1:])
        else:
            if inst[1:] not in gb.symbol_dict:
                gb.symbol_dict[inst[1:]] = gb.dict_count
                gb.dict_count = gb.dict_count + 1
            num = gb.symbol_dict[inst[1:]]

        return format(num, 'b').zfill(16)
    bin_inst = "111"
    if "=" in inst:
        dest = inst.split("=")[0]
    else:
        dest = "null"