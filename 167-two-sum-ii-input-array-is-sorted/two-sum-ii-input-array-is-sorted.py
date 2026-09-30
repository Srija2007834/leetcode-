class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        s=0
        l =0
        r = len(numbers)-1
        numbers = sorted(numbers)
        for i in numbers:
            s = numbers[l]+numbers[r]
            if s>target:
                r-=1
            elif s<target:
                l+=1
            else:
                return [l+1,r+1]