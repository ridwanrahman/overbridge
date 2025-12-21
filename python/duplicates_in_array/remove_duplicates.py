from typing import List

def main(nums: List[int]):
    if not nums:
        return 0

    write_pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[write_pos] = nums[i]
            write_pos += 1
    return write_pos

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    # nums = [1,1,2]
    print(main(nums))
