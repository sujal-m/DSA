# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, k):
        count = 0
        curr = head
        l = head
        while count != k:
            count += 1
            if count == k:
                break
            curr = curr.next
        firstNode = l
        firstNode.next = curr
        while l != curr:
            nxt = l.next
            prev = l

    def reverseKGroup(self, head, k: int):
        # calculate length of LL
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        #
