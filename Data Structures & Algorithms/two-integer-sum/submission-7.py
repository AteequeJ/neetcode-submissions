class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        a = []
        for i in range(len(nums)):
            print(1)
            a.append(i)
            res1 = target - nums[i]
            for j in range(len(nums)):
                if j != i and nums[j] == res1:
                    return [i, j]
            # if res1 in nums:
            #     print(2)
            #     if nums.index(res1) not in a:
            #         print(3)
            #         a.append(nums.index(res1))
            #     else:
            #         print(4)
            #         continue
            # return a