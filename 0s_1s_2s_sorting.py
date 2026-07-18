
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

	
class Solution:
    def segregate(self, head):
        #code here
        #maintain three different lists
        zero_dummy = Node(-1)
        one_dummy = Node(-1)
        two_dummy = Node(-1)
        
        #tail pointers to add new nodes
        zero_tail = zero_dummy
        one_tail = one_dummy
        two_tail = two_dummy
        
        curr = head
        
        while curr:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
            
            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
                
            else:
                two_tail.next = curr
                two_tail = two_tail.next
                
            curr = curr.next
        
        zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
        one_tail.next = two_dummy.next
        two_tail.next = None
        
        return zero_dummy.next
        
        