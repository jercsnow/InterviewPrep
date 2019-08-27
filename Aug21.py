# Class definition for a SinglyLinkedList
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, n1, n2):
		p1 = n1
		p2 = n2
		carryTheOne = False
		result = None
		curr = None
		while p1 or p2 or carryTheOne:
			val = (1 if carryTheOne else 0) + (p1.val if p1 else 0) + (p2.val if p2 else 0)
			carryTheOne = (val > 9)
			val %= 10
			digit = ListNode(val)
			if curr:
				curr.next = digit
			else:
				result = digit

			curr = digit

			if p1:
				p1 = p1.next
			if p2:
				p2 = p2.next

		return result

# Test 1
l1 = ListNode(8)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
	print result.val
	result = result.next
print "3 7 4"
print ""

# Test 2
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
	print result.val
	result = result.next
print "7 0 8"
print ""

# Test 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(8)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
	print result.val
	result = result.next
print "7 0 3 1"
print ""



