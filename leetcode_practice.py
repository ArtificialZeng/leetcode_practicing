1.twoSum
class Soluton:
  def twoSum(self, nums:List[int], target:int) -> List[int]:
    n = len(nums)
    for i in range(n):
      for j in range(i+1,n):
        if nums[i]+nums[j] == target:
          return [i,j]
    return []


66.class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits
class Solution:
  def plusOne(self,digits:List[int]) -> List[int]:
    n = len(digits)
    for i in range(n-1,-1,-1):
       if digits[i]!=9:
          digits[i] +=1
          for j in range(i+1,n):
            digits[j] =0
           return digits
    return [1]+[0] *n

        # digits 中所有的元素均为 9
        return [1] + [0] * n

  addOne
class Solution:
  def addOne(self,List[int]) ->
    
    
    for
    
    return [1] + [0] *n
