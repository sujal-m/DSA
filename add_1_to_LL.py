class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
    
    def addOne(self,head):
        
        #Step 1: Reverse the LL
        head = self.reverse(head)
        
        curr = head
        carry = 1
        
        while curr and carry:
            total = curr.data + carry
            curr.data = total % 10
            carry = total // 10
            
            #if we are at the last node and still have a carry
            if curr.next is None and carry:
                curr.next = Node(carry)
                carry = 0
                
            curr = curr.next
            
        head = self.reverse(head)
        
        return head
        
                
                
            
        