from LinkedList import *

def merge2_country(l1, l2):

    dummy = LinkedListNode(-1)

    prev = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        
        prev = prev.next
    
    prev.next = l1 if l1 is not None else l2

    return dummy.next

def mergeK_country(lists):
    if len(lists)>0:
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge2_country(res, lists[i])
        
        return res
    return


if __name__ == "__main__":
    a = create_linked_list([11,41,51])
    b = create_linked_list([21,23,42])
    c = create_linked_list([25,56,66,72])

    display(mergeK_country([a,b,c]))