class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] > stones[-2]:
                stones[-1] -= stones[-2]
                stones.pop(-2)
        return stones[0] if stones else 0