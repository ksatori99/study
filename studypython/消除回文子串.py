def longestPalindrome(s):

    # 情况一：如果字符串为空或者长度为1
    if len(s)<2:
        return s
    
    sDict = {}              # 字典存储，键为字符，值为字符的下标
    for i in range(len(s)):
        if s[i] in sDict.keys():
            sDict[s[i]].append(i)
        else:
            sDict[s[i]]=[i]

    subset = ''              #记录最长回文
    sublen = 0               #记录当前回文中的最大长度
    a=1
    # 情况二：一般情况下的字符串回文判断
    for k in sDict.keys():
        for i in sDict[k]:
            for j in sDict[k]:
                if j<=i:
                    continue
                else:
                    temp = s[i:j+1]     # 子串截取
                    temp2 = temp[::-1]  # 子串翻转
                    if temp==temp2 and len(temp)>=sublen:
                        sublen = len(temp)
                        subset = temp
                        
    # 情况三：如果字符串中的每个字符均不相同，则情况二后的sublen长度仍为0           
    if sublen==0:
        print('该字符串中已经没有回文')
        a=0

    return subset,a

def severaltimes(s):
    Palindrome,judge=longestPalindrome(s)
    print(Palindrome,judge)
    
    
    if judge == 0:
        print(s)
        
    else:
        aa=s.replace(Palindrome,'')
        severaltimes(aa)
    
    
    return s



if __name__=='__main__':
    # ss='abcdefghijklmndadaaiiiffffll123321laeg132sd'
    ss=input().strip()
    b=severaltimes(ss)
    