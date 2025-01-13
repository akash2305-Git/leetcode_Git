


class Node:

    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Swap_Node:

    def reverse_node(self,head):

        if not head or head.next:
            return head

        NewHead = None

        prev = None
        curr = head

        while curr and curr.next:
            nextPair = curr.next.next
            temp = curr.next

            curr.next = nextPair
            temp.next = curr

            if prev:
                prev.next = temp
            else:
                NewHead = temp

            prev = curr
            curr = nextPair

        return NewHead






    def add_val(self,head,val):

        new_node = Node(val)
        new_node.next = head
        return new_node

    def print_linkedList(self,head):

        while head != None:
            print(head.val, "->",end=" ")
            head = head.next





if __name__ == "__main__":

    head = None
    sn = Swap_Node()
    head = sn.add_val(head,1)
    head = sn.add_val(head,2)
    head = sn.add_val(head,3)
    head = sn.add_val(head,4)

    sn.print_linkedList(head)

    head1 = sn.reverse_node(head)

    print(head1.val)





