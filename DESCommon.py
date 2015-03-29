
from DESConstant import *
from DESUtil import get_column, get_row, to_binary, left_shift


def apply_IP(block):
    """input permutaion
    """
    r = []
    r.extend(block)
    for i in range(0, 64):
        r[i] = block[IP[i]]
    return r


def apply_FP(block):
    """final permutaion
    """
    r = []
    r.extend(block)
    for i in range(0, 64):
        r[i] = block[(FP[i])]
    return r


def e_box(block):
    """exapansion permutation to expand 32 bit block into 48 bit block
       also called E-box
    """
    dummy = []
    for i in range(48):
        dummy.append(block[E[i]])

    r = []
    for i in range(0, 48, 6):
        j = i + 6
        r.append(dummy[i:j])
    return r


def s_box(block):
    """s-box function to reduce 48 bit block to 32 bit block
    """
    for i in range(0, 8):
        row = str(block[i][0]) + str(block[i][-1])
        column = ''
        for j in range(1, 5):
            column += str(block[i][j])
        a = 16 * get_row(row)
        a += get_column(column)
        block.pop(i)
        block.insert(i, to_binary(ord(chr(s[i][a]))))
    r = []
    for i in block:
        r.extend(i[4:8])
    return r


def p_box(block):
    """p-box permutation
    """
    r = []
    r.extend(block)
    for i in range(32):
        r[i] = block[P[i]]
    return r


def iterate(left_block, right_block, keys, CIPHERS_FOR_EACH_ROUND):
    """iterating  for the 16 rounds
    """
    for j in range(0, 16):
        d9 = []
        d9.extend(right_block)
        right_block = e_box(right_block)
        for i in range(0, 8):
            di = i * 6
            for k in range(0, 6):
                right_block[i][k] ^= keys[j][di + k]
        right_block = s_box(right_block)
        right_block = p_box(right_block)
        for i in range(0, 32):
            right_block[i] ^= left_block[i]

        left_block = []
        left_block.extend(d9)

        if CIPHERS_FOR_EACH_ROUND is not None:
            t = left_block
            t.extend(right_block)
            CIPHERS_FOR_EACH_ROUND.append(t)

    return left_block, right_block


def DES(text_bits, start, end, keys, CIPHERS_FOR_EACH_ROUND=None):
    """Heart of the program : DES algorithm
    """
    block = []
    for i in range(start, end):
        block.append(text_bits[i])

    block = apply_IP(block)

    left_block = block[0:32]
    right_block = block[32:64]

    left_block, right_block = iterate(left_block, right_block, keys, CIPHERS_FOR_EACH_ROUND)

    block = []
    block.extend(right_block)
    block.extend(left_block)

    block = apply_FP(block)

    cipher_block = ''
    for i in block:
        cipher_block += str(i)
    return cipher_block


def generate_keys(key_text):
    """ key generation
    """
    key = []
    for i in key_text:
        key.extend(to_binary(ord(i)))

    C = []
    D = []
    r = []
    for i in range(28):
        C.append(key[PC1_C[i]])
    for i in range(28):
        D.append(key[PC1_D[i]])
    for i in range(0, 16):
        if i in [0, 1, 8, 15]:
            C = left_shift(C, 1)
            D = left_shift(D, 1)
        else:
            C = left_shift(C, 2)
            D = left_shift(D, 2)
        CD = []
        CD.extend(C)
        CD.extend(D)
        dummy = []
        for i in range(48):
            dummy.append(CD[PC2[i]])
        r.append(dummy)
    return r
