import  numpy as np
from numpy import random, rot90


def ShiftMyValue(array, shift_value):

    vector = []

    for i in range(4):
        vector.extend(array[0][0:-1])
        array = rot90(array).tolist()

    l = len(vector)
    vector *= 3
    vector = vector[l - shift_value: l*2 + shift_value]

    for _ in range(4):
        array[0] = vector[0:len(array[0])]
        vector = vector[len(array[0])-1:-1]
        array = rot90(array).tolist()

    return array


def main(array, shift_value):

    move_array = ShiftMyValue(array, shift_value)

    return move_array
