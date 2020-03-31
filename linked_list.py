#Node Class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        pl = []
        temp = self.head
        while(temp):
            pl.append(str(temp.data))
            temp = temp.next
        print(' -> '.join(pl))

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        self.head = llist.head.next

    def remove(self,old_data):
        temp = self.head

        if temp.data == old_data:
            self.head = temp.next
            return

        while(temp is not None):
            if temp.data == old_data:
                break
            prev = temp
            temp = temp.next

        if temp ==  None:
            return

        prev.next = temp.next

    def get_nth_object(self,index):
        temp = self.head
        while(index>0):
            temp = temp.next
            index = index-1
        return temp.data

    def reverse(self):
        current = self.head
        prev = next = None
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def get_last_to_front(self):

        temp = self.head
        sec_last = None

        while(temp and temp.next):
            sec_last = temp
            temp = temp.next

        sec_last.next = None
        temp.next = self.head
        self.head = temp

    def length(self):

        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

def merge_ll(ll1, ll2):
    new_list = LinkedList()
    #ll1 = 1,2,3,4,5
    #ll2 = 9,8,7,6,5
    head1 = ll1.head
    head2 = ll2.head
    while ll1 is not None:
        if head1.data < head2.data:
            new_list.push(ll2.head.data)
            ll2.head = head2.next

        elif head1.data == head2.data:
            new_list.push(ll1.head)
            ll1.head = head1.next
            ll2.head = head2.next

        else:
            new_list.push(ll1.data)
            ll1.head = head1.next

    return(new_list)

if __name__ == '__main__':

    llist = LinkedList()
    llist1 = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist1.push(7)
    llist.head.next = second
    second.next = third
    #llist.get_last_to_front()
    #llist.get_last_to_front()
    #llist.reverse()
    llist.push(4)
    llist.push(5)
    llist.printList()
    print('length->',llist.length())
    merge_ll(llist,llist1)
    #print(llist.get_nth_object(2))

