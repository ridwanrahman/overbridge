def main(nums, target):
    result = None
    for i in range(1, len(nums)):
        if nums[i] == target:
            result = i
        if nums[i-1] < target < nums[i]:
            result = i
        

    return result


if __name__ == "__main__":
    nums = [1,3,5,6]
    target=7
    print(main(nums, target))
