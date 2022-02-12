class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtLast(self,number):
        node=ListNode(int(number[0]))
        length=0
        length=len(number)
        temp=node

        i=1
        while i<length:
            while temp.next is not None:
                temp=temp.next
            temp.next=ListNode(int(number[i]))
            i=i+1

        newNode=self.reverse(node)
        return newNode
    
    def reverse(self,list):
        temp=list
        prev=None
        while temp is not None:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        return prev

    def getNumeber(self,list):
        temp=list
        self.value=""
        while temp is not None:
            self.value=self.value+str(temp.val)
            temp=temp.next
        return int(self.value)

    def addTwoNumbers(self, l1, l2):
        ll1=self.reverse(l1)
        ll2=self.reverse(l2)
        list1=self.getNumeber(l1)
        list2=self.getNumeber(l2)
        sum=list1+list2
        sum=str(sum)
        print(sum)
        return self.insertAtLast(sum)

# node3=ListNode(9)
# node2=ListNode(4,node3)
# l1 = ListNode(2,node2)

# n4=ListNode(9)
# n3=ListNode(4,n4)
# n2=ListNode(6,n3)
# l2 = ListNode(5,n2)

# addTwoNum=Solution()
# sum=addTwoNum.addTwoNumbers(l1,l2)