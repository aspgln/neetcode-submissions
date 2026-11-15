# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head) 
        first = dummy 
        second = head 

        for i in range(n):
            second = second.next
        
        print(f"first={first.val}")
        print(f"second={second.val if second is not None else None }")

        while second: 
            first = first.next 
            second = second.next 
        
        print(f"first={first.val}")
        print(f"second={second.val if second is not None else None }")

        first.next = first.next.next 
        # dummy.next = None 

        # out = head if head else None 
        return dummy.next  



