def main(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return left


if __name__ == "__main__":
    nums = [1,3,5,6]
    target=7
    print(main(nums, target))
