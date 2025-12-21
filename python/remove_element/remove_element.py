def main(nums, val):
    counter = 0
    for i in range(0, len(nums)):
        curr = nums[i]
        print(curr)
        if curr == val:
            nums[i] = "_"
        else:
            counter+=1

    write_pos = 0
    for i in range(0, len(nums)):
        if nums[i] != '_':
            nums[write_pos] = nums[i]
            write_pos += 1
    # second pass: fill the rest with underscores
    for i in range(write_pos, len(nums)):
        nums[i] = '_'

    return counter

if __name__ == "__main__":
    nums = [3,2,2,3]
    # nums = [0,1,2,2,3,0,4,2]
    val = 3
    # val=2
    print(main(nums, val))
