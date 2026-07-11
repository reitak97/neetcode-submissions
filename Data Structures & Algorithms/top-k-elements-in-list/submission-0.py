class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      numCount = Counter(nums)
      numCount = dict(sorted(numCount.items(),key=lambda item: item[1]))
      return list(numCount.keys())[-k:]

