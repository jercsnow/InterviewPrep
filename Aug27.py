def sortNums(nums):
    counts = dict()
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    arr = list()
    for i in range(0, counts.get(1, 0)): # insert 1's
        arr.append(1)
    for i in range(0, counts.get(2, 0)): # insert 2's
        arr.append(2)
    for i in range(0, counts.get(3, 0)): # insert 3's
        arr.append(3)

    return arr

result = sortNums([3, 3, 2, 1, 3, 2, 1])
print(result)
print("")
# [1, 1, 2, 2, 3, 3, 3]

result = sortNums([1])
print(result)
print("")
# [1]

result = sortNums([1,2,3])
print(result)
print("")
# [1, 2, 3]