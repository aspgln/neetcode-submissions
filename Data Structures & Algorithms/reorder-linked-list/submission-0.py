# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head 
        while curr: 
            nodes.append(curr)
            curr = curr.next 
        print(nodes)

        l = 0
        r = len(nodes)-1

        curr = head 
        while l < r: 

            nodes[l].next = nodes[r]
            l = l+1

            if l == r: 
                break
            else: 
                nodes[r].next = nodes[l]
            r = r-1
        nodes[l].next = None
        return 





        
