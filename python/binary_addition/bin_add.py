def binary_to_int_converter(num):
    i = len(num) - 1
    counter = 0
    adder = 0
    while i>=0:
        conv = int(num[i]) * (2**counter)
        adder = adder + conv
        i -= 1
        counter += 1
    return adder
def int_to_binary_converter(num):
    final_arr = []
    divisor = num
    if num == 0:
        return ["0"]
    while divisor != 0:
        b = divisor % 2
        divisor = divisor // 2
        final_arr.append(b)
    return final_arr[::-1]

def bin_add(data):
    num1 = binary_to_int_converter(data[0])
    num2 = binary_to_int_converter(data[1])
    addition = int_to_binary_converter(num1 + num2)
    binary_str = ''.join(str(bit) for bit in addition)
    print(binary_str)


if __name__ == "__main__":
    # data = ["11", "11"]
    # data = ["1010", "1011"]
    data = ["0", "0"]
    bin_add(data)