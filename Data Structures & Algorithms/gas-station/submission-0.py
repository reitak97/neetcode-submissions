class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = 0

        for i in range(len(gas)):
            cur_gas += gas[i]
            cur_gas -= cost[i]
            if cur_gas > 0:
                return i

        return -1