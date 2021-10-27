# 力扣4题
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # temp={}
        # temp2={}
        # for i in nums1:
        #     if i in temp:
        #         temp[i]+=1
        #     else:
        #         temp[i]=0
        # for j in nums2:
        #     if j in temp2:
        #         temp2[j]+=1
        #     else:
        #         temp2[j]=0
        # temp2=list(temp.keys())
        for i in nums2:
            nums1.append(int(i))
        nums1.sort()
        if len(nums1)%2==1:
            ans=nums1[len(nums1)//2]
        else:
            ans=(nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        return ans

nums1=[1,3]
nums2=[2]
llll=Solution()
ans=llll.findMedianSortedArrays(nums1,nums2)
print(ans)




