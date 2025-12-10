PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

ROTATIONS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def validate_key(key):
    if not isinstance(key, str):
        print("ERROR: Key must be written as text (a string).")
        return False
    if len(key) != 64:
        print("ERROR: Key must be exactly 64 bits long.")
        return False
    for bit in key:
        if bit not in ("0", "1"):
            print("ERROR: Key must contain only 0s and 1s.")
            return False
    return True
def permute(bits, table):
    new_bits = ""
    try:
        for position in table:
            new_bits += bits[position - 1]
    except:
        print("ERROR: Something went wrong during permutation.")
        return None
    return new_bits