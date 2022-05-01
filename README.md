# leetcode_practicing

1.twoSum<br>
class Soluton: <br>
  &emsp;def twoSum(self, nums:List[int], target:int) -> List[int]:<br>
    &emsp;&emsp;n = len(nums)<br>
    &emsp;&emsp;for i in range(n):<br>
      &emsp;&emsp;&emsp;for j in range(i+1,n):<br>
        if nums[i]+nums[j] == target:<br>
          return [i,j]<br>
    return []
