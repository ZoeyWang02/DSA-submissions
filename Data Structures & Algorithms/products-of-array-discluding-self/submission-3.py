class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return [0]*len(nums)
        elif (nums.count(0)==1):
            p=[0]*len(nums)
            zero_pos=0
            z=1
            for i in range(len(nums)):
                if nums[i]==0:
                    zero_pos=i
                    continue
                z=z*nums[i]
            p[zero_pos]=z
            return p
        p = [1]*len(nums)
        s=1
        for i in range(len(nums)):
            s=s*nums[i]
        for i in range(len(nums)):
            p[i]=s//nums[i]
        return p

            