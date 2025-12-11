def main(nums, target):
    thing = {}
    for index, i in enumerate(nums):
        difference = target - i
        if difference in thing:
            return [thing[difference], index]
        thing[i] = index

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(main(nums, target))
