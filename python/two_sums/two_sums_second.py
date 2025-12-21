def main(nums, target):
    for index, i in enumerate(nums):
        difference = target - i
        for j in range(index+1, len(nums)):
            if nums[j] == difference:
                print([index, j])
                return

if __name__ == '__main__':
    target = 6
    # nums = [2,7,11,15]
    nums = [3,2,4]
    # nums = [3,3]
    main(nums, target)