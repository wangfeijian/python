def test(n):
    if n == 1 or n == 2:
        return 1
    return test(n - 1) + test(n - 2)
nums = []
for i in range(20):
    nums.append(test(i + 1))
print(nums)