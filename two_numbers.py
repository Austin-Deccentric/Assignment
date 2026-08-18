def two_numbers(nums_list: list, target: int):
    found = {}

    for i in range(len(nums_list)):
        complement = target - nums_list[i]
        if complement in found:
            return [found[complement], i]
        found[nums_list[i]] = i

print(two_numbers([2,7,11,15], 9))