class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sortedArray1 = sorted(s)
        sortedArray2 = sorted(t)

        if len(s) != len(t):
            return False
        for i in range(len(sortedArray1)):
            if sortedArray1[i] != sortedArray2[i]:
                return False
        return True
