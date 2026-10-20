class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        return self._binarysearch(self.map[key],timestamp)
        


    def _binarysearch(self,arr,target):
        l = 0
        r = len(arr)-1
        res = ""
        while l <= r:
            mid = (l+r) //2
            if arr[mid][1] <= target:
                res = arr[mid][0]
                l = mid +1
            else:
                r=mid-1
                

        return res

