class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        fw = arr[:k]
        cs = sum(fw)
        c = 0
        if cs/k >= threshold:
            c+=1
        for i in range(k,len(arr)):
            cs = cs+arr[i]-arr[i-k]
            if cs/k >= threshold:
                c+=1
        return c