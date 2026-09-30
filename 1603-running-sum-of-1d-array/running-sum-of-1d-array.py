class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        l = []
        s=0
        for i in nums:
            s+=i
            l.append(s)
        return l