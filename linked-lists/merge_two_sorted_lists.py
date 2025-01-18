# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Given two sorted linked lists, merge them into a single sorted linked list.
        
        The merged linked list should also be sorted, and the input lists should not be modified.
        
        A valid solution must satisfy the following conditions:
        1. Nodes from both lists are compared, and the smaller node is appended to the result.
        2. The process continues until all nodes from one or both lists are processed.
        3. Any remaining nodes in one list are directly appended to the result.
        
        Args:
        list1: Optional[ListNode] - The head node of the first sorted linked list.
        list2: Optional[ListNode] - The head node of the second sorted linked list.
        
        Returns:
        Optional[ListNode] - The head node of the merged sorted linked list.
        """
        #create pointer to a node we will create so we can build the sorted list 
        temp = ListNode(-1)
        curr = temp

        #iterate until we reach the end of one of the lists
        while list1 and list2:
            #check current node of list1 and list2, depending on smaller value set curr.next to that node and update list1 or list2 to its next
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next  #after adding node from list1 or list2 update curr to its next 
        
        #after exiting while loop we will have a list with nodes still, depending on which list that is update curr.next to that node
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return temp.next  #return temp.next since we do not want to include head node we created
