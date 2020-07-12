class LRUCache:

    def __init__(self, capacity: int):
        # print (sys.version) # 3.8.2 (default, Feb 26 2020, 04:23:39) 
        self.capacity = capacity
        self.size = 0
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            ret = self.cache[key]
            del self.cache[key]
            self.cache[key] = ret
            return ret

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity and key not in self.cache:
            # 获取第一个键值，也就是最早使用的
            # k = list(self.cache.keys())[0]
            k = next(iter(self.cache))
            del self.cache[k]
        if key in self.cache:
            del self.cache[key]
        else:
            if self.size < self.capacity:
                self.size += 1
        self.cache[key] = value