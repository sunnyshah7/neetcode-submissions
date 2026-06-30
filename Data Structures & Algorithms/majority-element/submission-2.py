class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        sol = {}

        for ele in nums:
            if ele in sol:
                sol[ele] = sol.get(ele,0) + 1
            else:
                sol[ele] = 1
        ans = 0
        for key,val in sol.items():
            ans = max(ans ,val)

        key = next((k for k, v in sol.items() if v == ans), None)
    
        return key
            
        