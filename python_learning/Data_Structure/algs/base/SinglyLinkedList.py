from typing import Optional


class Node:

    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node


class SinglyLinkedList:

    def __init__(self):
        self._head = None

    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    def find_by_index(self, index: int) -> Optional[Node]:
        p = self._head
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node: Node, new_node: Node):
        if not node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not self._head or not node or not new_node:
            # 是否为空链表或空结点
            return
        if self._head == node:
            self.inser_node_to_head(new_node)
        current = self._head
        # 需要找到单链表的前驱指针
        while current._next and current._next != node:
            current = current._next
        if not current._next:
            return
        new_node._next = node
        current._next = new_node

    def delete_by_node(self, node: Node):
        if not self._head or not node:
            return
        if node._next:
            node.data = node._next.data
            node._next = node._next._next
            return
        # 尾结点或者不在链表里
        current = self._head
        while current and current._next != node:
            # 找到前一个结点(可能找到的是尾结点)
            current = current._next
        if not current:
            # 如果不在链表中
            return
        # 删掉尾结点
        current._next = node._next

    def delete_by_value(self, value: int):
        if not self._head or not value:
            return
        '''找到前面的结点，使其指向当前结点的下一个结点
          1 设置prev current结点
          2 改变current结点后prev的后继指针也相应该发生变化
          3 遍历current寻value的过程中，改变prev的后继指针，跳过value'''
        fake_head = Node(value + 1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:
            if current.data != value:
                prev._next = current
                prev = prev._next  # 值不等时后移指针到current，跳过value
            current = current._next  # 遍历链表

        if prev._next:
            # 如果是尾结点，直接删除
            prev._next = None
        # 如果删除的是头结点，那么需要设置头结点为第一个结点
        self._head = fake_head._next

    def __repr__(self) -> str:
        nums = []
        current = self._head
        while current:
            nums.append(current.data)
            current = current._next
        return "->".join(str(num) for num in nums)

    def __iter__(self):
        node = self._head
        while node:
            yield node.data
            node = node._next

    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end='')
            current = current._next
        while current:
            print(f"->{current.data}", end='')
            current = current._next
        print("\n", flush=True)


if __name__ == "__main__":
    linklist = SinglyLinkedList()
    for i in range(15):
        linklist.insert_value_to_head(i)
        print(linklist._head.data)  # 头插法
    print("\n")
    linklist.print_all()
    node9 = linklist.find_by_value(9)
    linklist.insert_value_before(node9, 20)
    linklist.insert_value_before(node9, 16)
    linklist.insert_value_before(node9, 16)
    print("\n")
    linklist.print_all()
    linklist.delete_by_value(16)
    node11 = linklist.find_by_index(3)
    linklist.delete_by_node(node11)
    linklist.delete_by_node(linklist._head)
    linklist.delete_by_value(13)
    print("\n")
    print(linklist)
    for value in linklist:
        print(value)
