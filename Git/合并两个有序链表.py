class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l0 = listNode = ListNode()
        if not l1 and l2:
            l0=l2
        elif not l2 and l1:
            l0=l1
        elif not l1 and not l2:
            l0= None
        else:
            if l1.val < l2.val:
                listNode.val = l1.val
                l1 = l1.next
            elif l1.val > l2.val:
                listNode.val = l2.val
                l2 = l2.next
            else:
                listNode.val = l1.val
                l1 = l1.next
                listNode.next = ListNode(l2.val)
                l2 = l2.next
                listNode = listNode.next
            while l1 or l2:
                if not l1:
                    while l2:
                        listNode.next=ListNode(l2.val)
                        l2=l2.next
                        listNode=listNode.next
                elif not l2:
                    while l1:
                        listNode.next = ListNode(l1.val)
                        l1 = l1.next
                        listNode = listNode.next
                else:
                    if l1.val<l2.val:
                        listNode.next=ListNode(l1.val)
                        l1=l1.next
                        listNode=listNode.next
                    elif l1.val>l2.val:
                        listNode.next = ListNode(l2.val)
                        l2 = l2.next
                        listNode = listNode.next
                    else:
                        listNode.next=ListNode(l1.val)
                        l1 = l1.next
                        listNode = listNode.next
                        listNode.next = ListNode(l2.val)
                        l2 = l2.next
                        listNode = listNode.next
        return l0