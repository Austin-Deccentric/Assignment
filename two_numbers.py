def two_numbers(nums_list: list, target: int):
    found = {}

    for i, num in enumerate(nums_list):
        complement = target - num
        if complement in found:
            return [found[complement], i]
        found[num] = i

print(two_numbers([2,7,11,15], 9))
print(two_numbers([3,2,4], 6))
print(two_numbers([3,3], 6))
