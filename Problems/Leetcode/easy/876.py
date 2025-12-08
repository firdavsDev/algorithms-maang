"""
https://leetcode.com/problems/middle-of-the-linked-list/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    # length = 0
    # current = head

    # while current is not None:
    #     length += 1
    #     current = current.next

    # middle = length // 2  # 2
    # current = head
    # for _ in range(middle):  # 0, 1
    #     current = current.next

    # return current
    mid = head
    end = head

    while end is not None and end.next is not None:
        mid = mid.next
        end = end.next.next

    return mid


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    # node_6 = ListNode(6)

    # add nexts
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    # node_5.next = node_6

    mid_node = middleNode(node_1)
    lst = []
    while mid_node is not None:
        lst.append(mid_node.val)
        mid_node = mid_node.next

    print(lst)
