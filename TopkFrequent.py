class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1={}
        res=[]
        for ele in nums:
            dict1[ele]=dict1.get(ele,0)+1
        
        sorted_lstt=sorted(dict1.items(),key= lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(sorted_lstt [i][0])
        return res