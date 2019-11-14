dict_count = 16


def decode(str):
    # recieves one legal line and translates it to binary
    if str[0] == '@':
        if str[1:].isdigit():
            num = int(str[1:])
        else:
            if str[1:] not in var_dict:
                var_dict[str[1:]] = dict_count
                dict_count = dict_count + 1
            num = var_dict[str[1:]]

        return format(num, 'b').zfill(16)
