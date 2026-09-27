class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        
        arr=[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)

        return [item[1] for item in arr[:k]]