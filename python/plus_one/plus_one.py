def plus_one(number: list[int]):
    new_arr = []
    i = len(number)-1
    carryover = 0
    while (i>=0):
        print(number[i])
        if i==len(number)-1:
            get_last_number = number[-1]
            increment_last_number = get_last_number + 1
            if increment_last_number > 9:
                print("number has been incremented")
                carryover = 1
                increment_last_number = 0
            new_arr.append(increment_last_number)
        else:
            if carryover:
                new_add = number[i] + 1
                new_arr.append(new_add)
                carryover=0
            else:
                new_arr.append(number[i])
        i-=1

    print(new_arr[::-1])

if __name__ == "__main__":
    # number: list = [1,2,3]
    # number: list[int] = [4,3,2,1]
    # number: list[int] = [8,8,8]
    # number: list[int] = [8,8,9]
    number: list[int] = [9,9,9]
    plus_one(number)
