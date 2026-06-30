class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rem = None
        count = 0
        for i in nums:
            if count == 0:
                rem = i
            
            if i == rem:
                count += 1
            else:
                count -= 1
        return rem

        