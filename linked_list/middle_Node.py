

class ListNode:

    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class middle_Node:


    def middle_node_value(self,head):
        fast = head
        fast_one = head

        while fast and fast.next:

            fast = fast.next.next
            fast_one = fast_one.next

        return fast_one



if __name__ == "__main__":

    head = [1,2,3,4,5]

    mn = middle_Node()
    ans = mn.middle_node_value(head)
    print(ans)
