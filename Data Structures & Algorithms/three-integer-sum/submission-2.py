class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                
                if current == 0:
                    myList = []
                    myList.append(nums[i])
                    myList.append(nums[j])
                    myList.append(nums[k])
                    result.append(myList)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif current < 0:
                    j += 1
                else :
                    k -= 1
            
            
        return result
        
        