from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def listprint(self, list1: Optional[ListNode]):
      printval = list1
      while printval is not None:
         print (printval.val)
         printval = printval.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result

if __name__ == "__main__":
    a1 = ListNode(2)
    a2 = ListNode(4)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3

    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3

    solution = Solution()
    result = solution.addTwoNumbers(a1, b1)
    print(solution.listprint(result))
