class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # if n's is not created it will default to 0
        for n, c in count.items(): # returns every single key value pair
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # return(sorted(dic, key=dic.get, reverse=True)[:k])

        
