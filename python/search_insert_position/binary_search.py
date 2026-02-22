# binary search has O(log n) which is much better than
# linear search is O(n).
def binary_search(data):
    nums = data[0]
    target = data[1]
    # left and right are my pointers. I will use these pointers
    # to move around the nums array
    left = 0
    right = len(nums) - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            # this means the target should be on the right as
            # it is sorted list and mid has the maximum number in the left
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    # data = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 11]
    # data = [[1,3,5,6], 5]
    data = [[1,3,5,6], 2]
    print(binary_search(data))