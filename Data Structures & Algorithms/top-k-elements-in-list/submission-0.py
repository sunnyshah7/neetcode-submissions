class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        for i in nums:
            if i in sol:
                sol[i] = sol.get(i,0) + 1
            else:
                sol[i] = 1
        
        sorted_dict = dict(sorted(sol.items(), key=lambda item: item[1],reverse = True))
        return list(sorted_dict.keys())[:k]
        