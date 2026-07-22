class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fullList = []
        used = []
        for i in range(len(strs)):
            if i in used:
                continue

            minList = [strs[i]]

            for j in range(i+1, len(strs)):

                if j in used:
                    continue

                if len(strs[i]) == len(strs[j]):

                    if sorted(strs[i]) == sorted(strs[j]):
                        minList.append(strs[j])
                        used.append(j)

            fullList.append(minList)

        print(fullList)    
        return fullList    