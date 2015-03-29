
hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
          '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
dec_dict = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8, '1001': 9,
          '1010': 10, '1011': 11, '1100': 12, '1101': 13, '1110': 14, '1111': 15}


hex_revesred_dict = {v: k for k, v in hex_dict.items()}
dec_reversed_dict = {v: k for k, v in dec_dict.items()}

row_dict = {'00': 0, '01': 1, '10': 2, '11': 3}
column_dict = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8,
              '1001': 9, '1010': 10, '1011': 11, '1100': 12, '1101': 13, '1110': 14, '1111': 15}

binary_list = []
bin_to_text_dict = {}

# for calculation of 8-bit list for every character
for n in range(256):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        if n % 2:
            b[7 - i] = 1
        n = n // 2
    binary_list.append(b)

# for calculation of char from string of 8-bits
k = 0
for i in binary_list:
    string = ''
    for j in i:
        string += str(j)
    bin_to_text_dict[string] = chr(k)
    k += 1


def get_row(s):
    return row_dict[s]


def get_column(s):
    return column_dict[s]


def to_binary(s):
    return binary_list[s]


def bin_to_hex(s):
    return hex_dict[s]


def bin_to_dec(s):
    return dec_dict[s]


def hex_to_bin(s):
    return hex_revesred_dict[s]


def dec_to_bin(s):
    return dec_reversed_dict[s]


def bin_to_text(s):
    return bin_to_text_dict[s]


def left_shift(s, times):
    """left shifting a list
    """
    for i in range(times):
        s.append(s.pop(0))
    return s


def add_pads_if_necessary(s):
    """adding bits to make an integer number of 64-bit blocks
    """
    number_of_vacancy = len(s) % 64
    need_pads = number_of_vacancy > 0
    if need_pads:
        for i in range(64 - number_of_vacancy):
            s.append(0)
    return s