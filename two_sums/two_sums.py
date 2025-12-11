import random
import time
from typing import List, Any


def generate_random_numbers(generate_this_many):
    to_submit = []
    for i in range(generate_this_many):
        random_integer = random.randint(1, 10)
        to_submit.append(random_integer)
    return to_submit

def brute_force_2(nums, target):
    for index, i in enumerate(nums):
        difference = target - i
        for j in range(index+1, len(nums)):
            if nums[j] == difference:
                print([index, j])
                return

def brute_force_1(nums, target):
    found = False
    l,m=None, None
    for index, i in enumerate(nums):
        for j in range(index + 1, len(nums)):
            if nums[index] + nums[j] == target:
                l = index
                m = j
                found = True
                break
    print([l, m])

def correct_solution(nums: List[int], target: int) -> list[int] | None:
    thing = {}
    for index, i in enumerate(nums):
        difference = target - i
        if difference in thing:
            return [thing[difference], index]
        thing[i] = index

    return None


if __name__ == "__main__":
    nums = generate_random_numbers(10000)

    start_time = time.perf_counter()
    nums.append(2)
    nums.append(5)
    target = 7
    # brute_force_1(nums, target)
    correct_solution(nums, target)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time:.6f} seconds")
