import Global_vars as gb
from Global_vars import *


def decode(str):
    # recieves one legal line and translates it to binary
    if str[0] == '@':
        if str[1:].isdigit():
            num = int(str[1:])
        else:
            if str[1:] not in symbol_dict:
                symbol_dict[str[1:]] = gb.dict_count
                gb.dict_count = gb.dict_count + 1
            num = symbol_dict[str[1:]]

        return format(num, 'b').zfill(16)
    bin_inst = "111"
