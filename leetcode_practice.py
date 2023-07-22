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

#First Unique Character in a String    
class Solution:  # 这行定义了一个名为Solution的类。
    
    def firstUniqChar(self,s) ->str:  # 在Solution类内部，我们定义了一个名为firstUniqChar的方法。这个方法接受一个参数s，代表一个字符串。
        
        count = Counter(s)  # 这行代码创建一个名为Counter的计数器对象，传入的参数是字符串s。Counter是Python collections库的一个类，它会为输入的可迭代对象中的每个元素创建一个字典，字典的键是元素，值是元素在可迭代对象中的出现次数。
        
        for idx,ch in enumerate(s):  # 这行代码开始一个循环，它会遍历字符串s中的每个字符。enumerate函数会返回字符串中每个字符的索引和字符本身。所以，对于每次循环，idx会被设为字符的索引，ch会被设为字符本身。
            
            if count[ch] ==1:  # 这行代码检查字符ch在Counter对象中的值是否为1。如果为1，表示这个字符在字符串s中只出现一次。
                
                return idx  # 如果前面的if语句为真，就执行这行代码。这行代码会结束方法的执行并返回字符的索引。
        
        return -1  # 如果for循环结束也没有找到只出现一次的字符，这行代码会执行。这行代码结束方法的执行并返回-1，表示没有找到只出现一次的字符。

