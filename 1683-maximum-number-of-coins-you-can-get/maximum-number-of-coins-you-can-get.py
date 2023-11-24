class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i, j = 0, len(piles)-2
        res = 0
        while i < j:
            res += piles[j]
            i+=1
            j-=2
        return res