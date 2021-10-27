# 力扣1题
class Solution:
    def twoSum(self, nums, target: int):
        temp=0
        array=[]
        for i in range(0,len(nums)):
            
            
            temp=nums[i]
            array=[i]
            
            for j in range(i+1,len(nums)):                  
                temp+=nums[j]
                array.append(j)
                if temp==target:
                    return array
                else:
                    temp=nums[i]
                    array=[i]
    

if __name__=='__main__':
    nums=input()
    nums=eval(nums)
    target=int(input())
    lalala=Solution()
    array=lalala.twoSum(nums,target)
    print(array)