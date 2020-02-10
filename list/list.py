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
        result = ''
        while current_head:
            result = str(current_head.get()) + result
            current_head = current_head.get_next()
            if current_head:
                result = ',' + result
        return result


def main():
    a = List(1, 2, 3)
    print(a)
    print('hello')


if __name__ == "__main__":
    main()
