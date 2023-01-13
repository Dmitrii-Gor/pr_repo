class FlatIterator:

    def __init__(self, list_of_list):
        self.a = list_of_list
        self.end = len(list_of_list)

    def __iter__(self):
        self.cursor = 0
        self.cursor2 = -1 # показатель внутреннего цикла
        return self

    def __next__(self):
        self.cursor2 += 1
        if self.cursor2 < len(self.a[self.cursor]):
            item = self.a[self.cursor][self.cursor2]
        else:
            self.cursor += 1
            self.cursor2 = 0
            if self.cursor != self.end:
                item = self.a[self.cursor][self.cursor2]
            else:
                raise StopIteration
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    test_1()

