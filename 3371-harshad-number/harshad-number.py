class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        temp = x
        while(temp>0):
            dig = temp%10
            s+=dig
            temp//=10
        if(x%s==0):
            return s
        else:
            return -1