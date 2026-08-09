class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = 0
        for count in freq.values():
            if count == maxFreq:
                maxCount += 1
        return max(
            len(tasks),
            (maxFreq - 1) * (n + 1) + maxCount
        )