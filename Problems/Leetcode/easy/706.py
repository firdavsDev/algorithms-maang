# 706. Design HashMap


class MyHashMap:

    def __init__(self):
        self.dic_values = {}

    def put(self, key: int, value: int) -> None:
        self.dic_values[key] = value

    def get(self, key: int) -> int:
        if self.dic_values.get(key):
            return self.dic_values.get(key)
        return -1

    def remove(self, key: int) -> None:
        return self.dic_values.pop(key) if self.dic_values.get(key) else -1


myHashMap = MyHashMap()
print(myHashMap.put(1, 1))
print(myHashMap.put(2, 2))
print(myHashMap.get(1))
print(myHashMap.get(3))
print(myHashMap.put(2, 1))
print(myHashMap.get(2))
print(myHashMap.remove(2))
print(myHashMap.get(2))


# Expect
# null
# null
# 1
# -1
# null
# 1
# null
# -1
