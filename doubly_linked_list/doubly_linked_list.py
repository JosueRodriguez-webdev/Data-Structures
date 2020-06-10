"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if self.head is None:
            self.head = new_node
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # if there is no head then return none
        if self.head is None:
            return None
            # if head and tail are the same then remove both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return None
            # else capture previous head value, set new head, and make the new head.prev == None.
        else:
            set_capture_prev_head = self.head.value
            set_new_head = self.head.next
            self.head = set_new_head
            self.head.prev = None
            self.length -= 1
            return set_capture_prev_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        # if there is no tail return null
        if self.head is None:
            return None
        else:
            old_node_prev = self.tail
            self.tail = new_node
            self.tail.next = None
            self.tail.prev = old_node_prev
            self.length += 1

        # else access the next until we get to the very end

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):

        # if no tail then return none
        if self.tail is None:
            return None
            # if head and tail are the same return reset values for head tail and length
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return None
            # else while loop through until the node.prev.next is none and capture it, set tail to captured object, set tail.next to none, return captured object.value
        else:
            value = self.tail.value
            self.delete(self.tail)
            self.length -= 1
            return value
        before_tail_node = self.head

        while before_tail_node.next is not self.tail:
            before_tail_node = before_tail_node.next

        self.tail = before_tail_node
        old_value = self.tail.next
        self.tail.next = None
        return old_value.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass
