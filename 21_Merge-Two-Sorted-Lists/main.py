from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.headval = None

    def listprint(self, list1: Optional[ListNode]):
      printval = list1
      while printval is not None:
         print (printval.val)
         printval = printval.next
    
    # Bubble Sorting Algorithms
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1)
    a2 = ListNode(0)
    a3 = ListNode(4)
    list1.next = a2
    a2.next = a3

    list2 = ListNode(1)
    b2 = ListNode(0)
    b3 = ListNode(4)
    list2.next = b2
    b2.next = b3

    result = Solution()
    result2 = result.mergeTwoLists(list1, list2)
    print(result.listprint(result2))


