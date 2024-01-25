# insert_back()만 변경됨
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next_ = next


class LinkedList(object):
    def __init__(self):
        self.size = 0  # node의 개수
        self.head = None
        self.tail = None

    # 시간복잡도 O(1)
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_ = new_node
            self.tail = self.tail.next_
        self.size += 1

    # 시간복잡도 O(n)
    # 예외사항1 : if self.head is None
    # 예외사항2 : if idx < 0 or idx > self.size
    def insert_at(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next_ = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next_
            new_node.next_ = current.next_
            current.next_ = new_node
        self.size += 1

    # 시간복잡도 O(n)
    # 예외상황: if idx < 0 or idx >= self.size
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next_
        return current.value

    # 시간복잡도 O(n)
    # 예외상황: if idx < 0 or idx >= self.size
    def set(self, idx, value):
        current = self.head
        for _ in range(idx):
            current = current.next_
        current.value = value

    # 시간복잡도 O(n)
    # 예외상황 : size == 1 => size == 0 이되는 상황 제외
    def remove_at(self, idx):
        if idx == 0:
            self.head = self.head.next_  # garbage collector가 알아서 처리해준다.
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next_
            current.next_ = current.next_.next_
        self.size -= 1

    # 시간복잡도 O(n)
    def remove_back(self):
        current = self.head
        last_index = self.size - 1
        for _ in range(last_index - 1):
            current = current.next_
        current.next_ = current.next_.next_
        self.tail = current.next
        self.size -= 1

    def print(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next_
            if current:
                print("->", end="")
        print()


ll = LinkedList()
ll.insert_back(value=1)
ll.insert_back(value=2)
ll.insert_back(value=3)
ll.insert_back(value=4)
ll.insert_back(value=5)
ll.print()
ll.remove_at(idx=3)
ll.print()
