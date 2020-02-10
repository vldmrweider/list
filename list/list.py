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


class ListIterator:
    def __init__(self, source_list):
        self.current_head = source_list.get_head()

    def __next__(self):
        if self.current_head:
            value = self.current_head.get()
            self.current_head = self.current_head.get_next()
            return value
        else:
            raise StopIteration


class List:
    def __init__(self, *args):
        self.__head = None
        for value in args:
            self.__add(value)

    def __iter__(self):
        return ListIterator(self)

    def __str__(self):
        result = ''
        for item in self:
            result = str(item) + result
        return result

    def __add(self, value):
        temp = NodeItem(value)
        temp.set_next(self.__head)
        self.__head = temp

    def get_head(self):
        return self.__head

    def append(self, *args):
        for value in args:
            self.__add(value)

    def print(self):
        print(self)


def main():
    a = List(1, 2, 3)
    a.print()

    # a.append(4, 5)
    # a.print()


if __name__ == "__main__":
    main()
