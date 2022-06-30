class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1, l2):
        
        values1 = []
        values2 = []
        values = []
        rest = None
        while l1 != None:
            value = l1.val
            l1 = l1.next
            values1.append(value)    
        
        while l2 != None:
            value = l2.val
            l2 = l2.next
            values2.append(value)
            
        node = None
        
        if len(values1 > values2):
            val = values1
        else:
            val = values2

        for num in val:
            
            if rest != None:
                node = ListNode(val=rest)
            val_len = len(values)

            for i in range(0, val_len):
                i = i+1
                node = ListNode(val=values[val_len-i], next=node)
            
        
        return values1, values2, node

values = [2,4,3]
values1 = [5,6,4]

node = None
for i in values:
    node = ListNode(i, node)

node1 = None
for i in values1:
    node1 = ListNode(i, node1)

s = Solution.addTwoNumbers(node, node1)
print(s)