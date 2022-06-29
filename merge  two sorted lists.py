class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeTwoLists(self, list1, list2):
    newListhHead = ListNode()
    i = list1
    j = list2
    if i.val >= j.val:
        newListHead = ListNode(j.val)
        j = j.next
    else:
        newListHead = ListNode(i.val)
        i = i.next
    newListTail = newListHead
    while i != None and j != None:
        if i.val >= j.val:
            newListTail.next = ListNode(j.val)
            newListTail = newListTail.next
            j = j.next
        else:
            newListTail.next = ListNode(i.val)
            newListTail = newListTail.next
            i = i.next
    if (i != None):
        newListTail.next = ListNode(i.val)
    else:
        newListTail.next = ListNode(j.val)
    return newListHead

XXXX