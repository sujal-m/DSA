#LC 2
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def addTwoNumbers(self, l1, l2):
        curr1, curr2 = self.reverseList(l1), self.reverseList(l2)
        num1 = num2 = 0
        ans = ListNode(-1)
        newHead = ans
        while curr1:
            num1 = num1*10 + curr1.val
            curr1 = curr1.next
        while curr2:
            num2 = num2*10 + curr2.val
            curr2 = curr2.next
        result = num1 + num2
        result = str(result)
        l = len(result)
        for i in range(l):
            ans.next = ListNode(int(result[i]))
            ans = ans.next
        ans.next = None
        newHead.next = self.reverseList(newHead.next)
        return newHead.next



        