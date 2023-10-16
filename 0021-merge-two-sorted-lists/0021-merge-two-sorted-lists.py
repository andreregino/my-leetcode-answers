# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = new_list = ListNode() #dummy node always point to the beginning
        
        while list1 and list2: # both lists should be non empty
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            

            new_list = new_list.next

        new_list.next = list1 or list2 # get the rest of the list
        return dummy_node.next