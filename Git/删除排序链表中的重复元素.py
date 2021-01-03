class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        last, cur = head, head.next
        while True:
            while cur and cur.val == last.val:
                cur = cur.next
            last.next = cur
            last = cur
            if not cur: break
            cur = cur.next
        return head