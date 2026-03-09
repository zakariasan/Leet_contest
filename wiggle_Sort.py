def wiggleSort(nums):
    nums.sort()

    n = len(nums)
    mid = (n + 1) // 2

    small = nums[:mid][::-1]
    large = nums[mid:][::-1]

    i = 0
    for num in small:
        nums[i] = num
        i += 2

    i = 1
    for num in large:
        nums[i] = num
        i += 2

num = [1, 1, 3, 5, 6]
print(num)
wiggleSort(num)
print(num)
