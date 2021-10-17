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
    