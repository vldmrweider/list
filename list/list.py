class NodeItem:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class List:
    def __init__(self, *args):
        self.head = None
        for value in args:
            self.__add(value)

    def __add(self, value):
        temp = NodeItem(value)
        temp.set_next(self.head)
        self.head = temp

    def __str__(self):
        current_head = self.head
        result = None
        while current_head != None:
            result += current_head.value
            current = current.next
        return result
