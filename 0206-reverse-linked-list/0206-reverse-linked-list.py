# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, actual = None, head

        while actual:
            temp = actual.next # resto, 2345, depois 345, depois 45....
            actual.next = prev # começa com none
            prev = actual #começa comm 1
            actual = temp # 2345
        return prev