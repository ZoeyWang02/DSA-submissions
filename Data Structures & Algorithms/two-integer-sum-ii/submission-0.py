class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp={}
        for i,num in enumerate(numbers):
            if target-num in tmp:
                return [tmp[target-num],i+1]
            tmp[num]=i+1
        return []