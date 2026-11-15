# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: find midpoint 
        # step 2: reverse the second part (after the midpoint)
        # step 3: merge 

        # step 1: mid point 
        slow = head 
        fast = head.next 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        
        # print(f"slow = {slow.val}")
        # print(f"fast = {fast.val}")

        # step 2: reverse 
        prev = None 
        second = slow.next 
        slow.next = None 
        while second: 
            tmp = second.next 
            second.next = prev
            prev = second 
            second = tmp 

        # print(f"prev = {prev.val}")
        # print(f"curr = {curr.val}")

        # step 3: 
        first = head 
        second = prev

        while second: 
            tmp1 = first.next 
            tmp2 = second.next 

            first.next = second 
            second.next = tmp1

            first = tmp1
            second = tmp2





