from typing import List, final


def plus_one(digits: List[int]):
    to_add = 1
    i = len(digits)-1
    to_return = []
    carryover = 0
    while i>=0:
        # print(digits[i])
        increment = digits[i] + to_add + carryover
        if len(str(increment)) == 2:
            to_add = 0
            increment = 0
            carryover = 1
        else:
            carryover = 0
            to_add = 0
        to_return.append(increment)
        i-=1
    if carryover:
        to_return.append(carryover)
    return to_return[::-1]

if __name__ == "__main__":
    # digits = [1,2,3]
    # digits = [4,3,2,1]
    # digits = [9]
    # digits = [9, 9]
    digits = [8,9,9]
    print(plus_one(digits))