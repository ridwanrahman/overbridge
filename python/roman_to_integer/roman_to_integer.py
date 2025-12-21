def main(user_input: str):

    all_romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    final = 0
    # for inp in user_input:
    #     roman_to_num = all_romans[inp]
    #     final = final + roman_to_num
    # print(final)
    final = 0
    for i in range(len(user_input)):
        curr_val = all_romans[user_input[i]]
        next_val = all_romans[user_input[i+1]] if i+1<len(user_input) else 0

        if curr_val < next_val:
            final = final - curr_val
        else:
            final = final + curr_val


    print(final)

if __name__ == "__main__":
    # user_input:str = "III"
    # user_input:str = "LVIII"
    user_input: str = "XCMX"
    # user_input: str = "IX"
    # user_input: str = "III"
    main(user_input)