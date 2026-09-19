class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        res = []
        for num in nums:
            m[num] = m.get(num, 0) + 1

        for key in m:
            n = len(res)
            if (n < k):
                res.append(key)
            else:
                min_idx = 0
                for i in range(1, k):
                    if m[res[i]] < m[res[min_idx]]:
                        min_idx = i
                    
                if m[key] > m[res[min_idx]]:
                    res[min_idx] = key

        return res
        