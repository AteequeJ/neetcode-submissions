class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        myList = []
        
        while i < j and i != j:
            print('i',i)
            print(j)
            print(target)
            if numbers[i] + numbers[j] == target:
                print('yes')
                myList.append(i+1)
                myList.append(j+1)
                return myList
            if (numbers[i] + numbers[j]) > target:
                j -= 1
            else:
                i += 1
        
        return myList

