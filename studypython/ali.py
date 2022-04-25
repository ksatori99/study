#转化二进制
def erjinzhi(array):
    
    temp=[]
    for i in array:
        temp.append(bin(i).replace('0b',''))
    
    return temp

# sadadadada
#判定是否都为1
def judge(array):
    temp={}
    number=len(array)
    a=0
    a2=0
    b=0
    for i in range(0,len(array)):
        a2=len(array[i])
        if b<=a2:
            b=a2
    for i in range(0,b):
        temp[i]=0

    for i in range(0,len(array)):

        iii=0
        
        for j in range(len(array[i])-1,-1,-1):
            

            if array[i][j]=='1':
                temp[iii]=temp[iii]+1
            
            iii+=1
    for i in temp.keys():
        if temp[i]==number:
            a=i
            break
    if a==0:
        a=-1
        return a
    
    return a+1

    

if __name__=='__main__':
    t=int(input())
    i=0
    ii=0
    n2=[]
    array2=[]
    while i<=t-1:
        n=int(input())
        array=list(map(int,input().strip().split()))
        n2.append(n)
        array2.append(array)
        i+=1
    c=len(array2)
    while ii<=c-1:
        temp=erjinzhi(array2[ii])
        temp2=judge(temp)
        print(temp2)
        ii+=1

# a={0:1}
# b=a[0]+1
# print(b)

#     # b=erjinzhi(array)
#     # print(b)
#     # c=judge(b)
    
#     # print(c)

# a=[1,2,3,4]
# b=a[-len(a)+1]
# for i in range(-1,-len(a)):
#     print(a[i])

# a=[1,2,3,4,5]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])


