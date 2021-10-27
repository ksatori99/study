class huiwen:
    def __init__(self,a,s):
        
        self.s=s
        self.a=a

    def longestPalindrome(self):

        # 情况一：如果字符串为空或者长度为1
        if len(self.s)<2:
            return self.s
        
        sDict = {}              # 字典存储，键为字符，值为字符的下标
        for i in range(len(self.s)):
            if self.s[i] in sDict.keys():
                sDict[self.s[i]].append(i)
            else:
                sDict[self.s[i]]=[i]

        subset = ''              #记录最长回文
        sublen = 0               #记录当前回文中的最大长度
        
        # 情况二：一般情况下的字符串回文判断
        for k in sDict.keys():
            for i in sDict[k]:
                for j in sDict[k]:
                    if j<=i:
                        continue
                    else:
                        temp = self.s[i:j+1]     # 子串截取
                        temp2 = temp[::-1]  # 子串翻转
                        if temp==temp2 and len(temp)>=sublen:
                            sublen = len(temp)
                            subset = temp
                            
        # 情况三：如果字符串中的每个字符均不相同，则情况二后的sublen长度仍为0           
        if sublen==0:
            print('该字符串中已经没有回文')
            self.a=0

        return subset

    def severaltimes(self):
        Palindrome=self.longestPalindrome()
        print(Palindrome,self.a)
        
        
        if self.a == 0:
            pass
            
        else:
            self.s=self.s.replace(Palindrome,'')
            self.severaltimes()
        
        return self.s

if __name__=='__main__':
    ss='abcdefghijklmndadaaiiiffffll123321laeg132sd'
    # ss=input().strip()
    a=1
    b=huiwen(a,ss)
    c=b.severaltimes()
    print(c)
    


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         maxl,max_len,n = 0,0,len(s)
#         for i in range(2*n-1):
#             l,r = i//2,i//2+i%2
#             while l>=0 and r < n and s[l]==s[r]:
#                 if r-l+1>max_len: maxl,max_len = l,r-l+1
#                 l-=1
#                 r+=1
#         return s[maxl:maxl+max_len]

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

