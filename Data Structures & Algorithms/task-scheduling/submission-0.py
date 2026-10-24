class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] +=1

        heap = []
        for t in counter:
            heapq.heappush(heap,-counter[t])

        q = deque()
        time = 0
        while heap or q:
            if heap:
                curr = 1 + heapq.heappop(heap)
                #only add if not 0
                if curr:
                    q.append((curr,time+n))

            if q and q[0][1] == time:
                count = q.popleft()[0]
                heapq.heappush(heap, count)

            time +=1

        return time
        