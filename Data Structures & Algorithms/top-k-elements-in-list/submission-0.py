class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        pairs = list(freq.items())
        pairs.sort(key=lambda pair: pair[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(pairs[i][0])
        return ans