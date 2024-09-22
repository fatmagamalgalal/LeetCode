class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums)-1
        for j in range(len(nums)):
            while nums[j] == val and j < i:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i-=1
        s = 0
        for n in nums:
            if n == val: break
            s+=1    
        print(nums)    
        return s
        