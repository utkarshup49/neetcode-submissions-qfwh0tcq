class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = {}
        result = []
        for n in nums:
            if n not in freq_num:
                freq_num[n] = 1
            else:
                freq_num[n] += 1
        sorted_dict = sorted(freq_num.items(), key = lambda item:item[1], reverse = True)
        
        
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result