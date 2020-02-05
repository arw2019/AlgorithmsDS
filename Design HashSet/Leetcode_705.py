class MyHashSet:

    def __init__(self):
        self.sz = 1000
        self.buckets = [list() for _ in range(self.sz)]
        
    def _get_bucket(self, key):
        return self.buckets[key % self.sz] 
        

    def add(self, key: int) -> None:
        """O(N) worst case"""    
        bucket = self._get_bucket(key)
        if key not in bucket:
            bucket += [key]

    def remove(self, key: int) -> None:
        """O(N) worst case"""
        bucket = self._get_bucket(key)
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        O(N) worst case
        """
        bucket = self._get_bucket(key)
        return key in bucket 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
