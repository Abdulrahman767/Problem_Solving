class Solution:
    def decompressRLElist(self, nums):
      result = [] # [1,1,2,3]
      for index_of_freq_num in range(0,len(nums),2): 
        val = nums[index_of_freq_num + 1]
        for j in range(0,nums[index_of_freq_num],1):
            result.append(val)
      return result