# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        for i in range(0, len(arr), k):
            if i + k <= len(arr):
                arr[i:i+k] = arr[i:i+k][::-1]
        cur = head
        i = 0
        while cur:
            cur.val = arr[i]
            i += 1
            cur = cur.next
        return head