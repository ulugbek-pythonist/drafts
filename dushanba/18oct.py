nums = [3, 1, 4, 3]
target = 6
my_dict = dict()


def Two(nums: list, target: int):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No solution found


result = Two(nums, target)
print(result)
