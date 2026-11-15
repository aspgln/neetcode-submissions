# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 

        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
        
        print(f"mid = {slow.val}")
        # print(f"end = {fast.val}")

        # reverse second part 
        curr = slow.next 
        slow.next = None 

        prev = None 
        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        # print(f"prev = {prev.val}")

        # merge 
        first = head 
        second = prev 
        while second: 
            nxt1 = first.next 
            nxt2 = second.next
            first.next = second 
            second.next = nxt1

            first = nxt1 
            second = nxt2 




