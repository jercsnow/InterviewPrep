def lengthOfLongestSubstring(s):
	if not s:
		return 0
		
	indexes = dict()
	currIndex = 0
	runningCount = 0
	maxCount = 0
	for char in s:
		if char in indexes:
			if runningCount >= currIndex - indexes[char]: # runningCount includes last instance of char
				runningCount = currIndex - indexes[char] - 1
			indexes[char] = currIndex
		else:
			indexes[char] = currIndex
			
		runningCount += 1
		maxCount = runningCount if runningCount > maxCount else maxCount
		currIndex += 1

	return maxCount

# Test 1
print lengthOfLongestSubstring('abcaa')
print 3
print ""

# Test 2
print lengthOfLongestSubstring('abcabdcz')
print 5
print ""

# Test 3
print lengthOfLongestSubstring('abrkaabcdefghijjxxx')
print 10
print ""

# Test 4
print lengthOfLongestSubstring(None)
print 0
print ""