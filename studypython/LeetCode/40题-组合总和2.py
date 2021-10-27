# 力扣40题
class Solution:

    def __init__(self) -> None:
        pass

    def lalala(self, c, t):
        
        a = []
        b = []
        c.sort()

        def llll(ii, total):
            
            if total > t:
                return
            
            elif total == t:
                a.append(b[::])
                return
            
            else:
            
                for i in range(ii, len(c)):
                    # 去重元素
                    if i>ii and c[i]==c[i-1]:    
                        continue
                    total += c[i]
                    b.append(c[i])
                    llll(i+1, total)
                    b.pop()
                    total -= c[i]   
        total = 0
        llll(0, total)
        return a

if __name__=='__main__':
#     c=input().strip().split()
#     c=list(map(int,c))
#     t=int(input())
    c=[100,10,20,70,60,10,50]
    t=80
    func=Solution()
    ans=func.lalala(c,t)
    print(ans)

