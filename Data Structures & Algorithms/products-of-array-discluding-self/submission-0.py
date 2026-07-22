class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        myList = []
        i = 0
        
        while i < len(nums):
            fullList = nums.copy()            
            fullList.pop(i)
            myList.append(math.prod(fullList))
            i = i+1
        return myList