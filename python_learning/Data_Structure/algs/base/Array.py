class Array():

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> object:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        for item in self:
            print(item)


if __name__ == "__main__":
    '''
    1 增 删 随机查找
    2 假设数据类型为整型'''
    MyArray = Array(capacity=5)
    MyArray.insert(0, 0)
    MyArray.insert(1, 2)
    MyArray.insert(2, 4)
    MyArray.insert(3, 0)
    MyArray.insert(4, 5)
    MyArray.print_all()
    assert MyArray.insert(0, 5) is False
    assert MyArray.__len__() == 5
    assert MyArray.find(1) == 2
    assert MyArray.delete(3) is True
    print("-" * 20)
    MyArray.print_all()
