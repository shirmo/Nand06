symbol_dict = {"R" + str(i): i for i in range(16)}
symbol_dict.update({"SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4})
dict_count = 16


CLEAN_LINES = []
START = "("
END = ")"
COMMENT = "//"
NEW_LINE = "\n"
TAB = "\t"