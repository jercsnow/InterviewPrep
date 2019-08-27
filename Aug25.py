class Solution: 
    def getRange(self, arr, target):
        if arr == None or target < arr[0] or target > arr[-1]: # target not within arr
            return -1, -1

        index = self.getIndexofTarget(arr, target)
        if index == -1:
            return -1, -1
        else:
            first = index
            last = index
            while first > 0 and arr[first - 1] == target:
                first -= 1

            while last + 1 < len(arr) and arr[last + 1] == target:
                last += 1

            return first, last

    def getIndexofTarget(self, arr, target): # Binary search for target through arr
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 0
print(Solution().getRange(arr, x))
# [-1, -1]

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 5
print(Solution().getRange(arr, x))
# [-1, -1]

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 1
print(Solution().getRange(arr, x))
# [0, 0]



