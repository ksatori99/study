# 力扣5题
#哈希表记录
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s)<2:
#             return s
#         sdict={}
#         for i in range(len(s)):
#             if s[i] in sdict.keys():

#                 sdict[s[i]].append(i)
#             else:

#                 sdict[s[i]]=[i]
        
#         subset=''
#         sublen=0
#         for k in sdict.keys():
#             for i in sdict[k]:
#                 for j in sdict[k]:
#                     if j <=i:
#                         continue
#                     else:
#                         temp=s[i:j+1]
#                         temp2=temp[::-1]
#                         if temp==temp2 and len(temp)>sublen:
#                             subset=temp
#                             sublen=len(temp)

#         if sublen==0:
#             subset=s[0]

#         return subset


#中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxl=0
        max_len=0
        n = len(s)
        for i in range(2*n-1):
            l = i//2
            r = i//2+i%2
            while l>=0 and r < n and s[l]==s[r]:
                if r-l+1>max_len: 
                    maxl=l
                    max_len = r-l+1
                l-=1
                r+=1
        return s[maxl:maxl+max_len]


# 回文串：1个中心 + 左右等距扩散
# 回文中心：奇数长回文串1个中心字符，偶数长2个中心字符
# 中心数目：对于n长原始字符串s，一共有2n-1个回文中心
# 遍历2n-1个回文中心，确定中心后，check能否左右扩散
# 左右扩散：l>=0 and r<n and s[l]==s[r]
# 左右指针：l=i//2,r=i//2+i%2
# 扩散过程中通过maxl,max_len确定最长回文串的左端点和长度
# 结果返回：s[maxl:maxl+max_len]
# 时间：o(n^2)
# 空间：o(1)