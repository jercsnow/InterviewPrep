class Solution: 
    def longestPalindrome(self, s):
        longest = 0
        str_length = len(s)
        num_checks_total = 0
        num_checks_opt = 0
        for index, char in enumerate(s):
            if index != str_length - 1 and char == s[index + 1]: # Need to check for even length palindrome
                num_checks_total += 1
                if self.maxPalindromeIsPossible(str_length, index, longest, True):
                    longest = max(longest, self.checkPalindrom(s, index, True))
                    num_checks_opt += 1

            num_checks_total += 1
            if self.maxPalindromeIsPossible(str_length, index, longest, False):
                longest = max(longest, self.checkPalindrom(s, index, False))
                num_checks_opt += 1

        #print(f"{num_checks_opt} checks were run instead of {num_checks_total}")
        return longest

    def checkPalindrom(self, s, index, checkEven):
        left = index -1
        right = index + 2 if checkEven else index + 1
        length = 2 if checkEven else 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                length += 2
                left -= 1
                right += 1
            else:
                break

        return length


    def maxPalindromeIsPossible(self, str_length, index, longest, isEven):
        left = index -1
        right = index + 2 if isEven else index + 1
        length = 2 if isEven else 1
        return min(left + 1, str_length - right) + length > longest

# Optimize the solution by checking if palindrome at index can be longer than longest


        
# Test 1
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
print(7)
print('')

# Test 2
s = "t"
print(str(Solution().longestPalindrome(s)))
print(1)
print('')

# Test 3
s = "racecars"
print(str(Solution().longestPalindrome(s)))
print(7)
print('')

# Test 4
s = "raccars"
print(str(Solution().longestPalindrome(s)))
print(6)
print('')

# Test 5
s = "ab"
print(str(Solution().longestPalindrome(s)))
print(1)
print('')

# Test 6
s = "aba"
print(str(Solution().longestPalindrome(s)))
print(3)
print('')

# Test 7
s = "aa"
print(str(Solution().longestPalindrome(s)))
print(2)
print('')