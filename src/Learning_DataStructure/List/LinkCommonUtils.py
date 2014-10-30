__author__ = 'wenychan'

from MyListNode import MyListNode
import random


def print_link(head):
    if head is None:
        print 'Link: []'

    print_list = []
    current_node = head
    while current_node is not None:
        print_list.append(str(current_node.get_value()))
        current_node = current_node._next

    if len(print_list) > 0:
        print ','.join(print_list)


def generate_random_int_link(if_double_link=False, size=10, *args):
    if len(args) == 0:
        random_gen = True
    else:
        random_gen = False
        size = len(args)

    pre = None
    for i in range(size):
        if random_gen:
            node = MyListNode(random.randint(0, 100))
        else:
            node = MyListNode(args[i])
        if pre is not None:
            pre._next = node
            if if_double_link:
                node._pre = pre
        else:
            head = node
        pre = node

    return head

print_link(generate_random_int_link())
