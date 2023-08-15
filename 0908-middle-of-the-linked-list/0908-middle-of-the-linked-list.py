# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr.next:
            count = count + 1
            curr = curr.next
        curr = head
        for i in range(count // 2):
            curr = curr.next
        
        return curr