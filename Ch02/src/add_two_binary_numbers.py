"""
    ２つのnビットの配列の足し算
"""


def add_two_binary_numbers(A, B, C):
    carry = 0
    for i in range(len(A) - 1, -1, -1):
        carry, bit = divmod(A[i] + B[i] + carry, 2)
        C[i + 1] = bit
    else:
        C[i] = carry