# 力扣3题
class Solution:
    def __init__(self) -> None:
        pass
    def lengthOfLongestSubstring(self, s: str) -> int:



        st={}
        i,ans=0,0
        for j in range(len(s)):

            if s[j] in st:
                i=max(i,st[s[j]])
            ans=max(ans,j-i+1)


            st[s[j]]=j + 1
        return ans

if __name__=='__main__':
    s='qwqqqq'
    llll=Solution()
    answer=llll.lengthOfLongestSubstring(s)
    print(answer)

