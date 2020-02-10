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
        self.__tail = None
        for value in args:
            self.__add(value)

    def __iter__(self):
        return ListIterator(self)

    def __str__(self):
        return " ".join(map(str, self))

    def __iadd__(self, other):
        for item in other:
            self.__add(item)
        return self

    def __add(self, value):
        temp = NodeItem(value)
        temp.set_next(self.__head)
        self.__head = temp

    def get_head(self):
        return self.__head

    def append(self, *args):
        for value in args:
            self.__add(value)

    def print_reversed(self):
        print(self)

    def print(self):
        reversed = List()
        for item in self:
            reversed.__add(item)
        print(reversed)


def main():
    a = List(1, 2, 3)
    a.append(4, 5)
    a.print()
    a.print_reversed()

    b = List(7, 8)
    b.print()

    a += b
    a += [9, 10]
    a.print()

    d = List()
    d.print()

    e = List(None)
    e.print()


if __name__ == "__main__":
    main()
