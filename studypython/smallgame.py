# 舒服了



# 判断用户输入选项
def correct_input(input_user,len_choise):

    input_user=input_user.lower()

    aa=ord('a')+len_choise-1
    bb=chr(aa)
    if 'a'<= input_user <= bb:
        return True
    else:
        print('请输入正确的选项编号:')
        return False



# 返回正确值
def correct_answer(input_user,correctanswer):
    input_user=input_user.lower()
    if ord(input_user)-ord('a') == correctanswer:
        return 1
    else:
        return 0





def main():

    # 编写题目列表
    question_lists=[
        {
            'question':'''
S先生、P先生、Q先生他们知道桌子的抽屉里有16张扑克牌：
红桃A、Q、4
黑桃J、8、4、2、7、3
梅花K、Q、5、4、6
方块A、5
约翰教授从这16张牌中挑出一张牌来，并把这张牌的点数告诉 P先生，把这张牌的花色告诉Q先生。这时，约翰教授问P先生和Q 先生：你们能从已知的点数或花色中推知这张牌是什么牌吗？ 于是，S先生听到如下的对话：
P先生：我不知道这张牌。
Q先生：我知道你不知道这张牌。
P先生：现在我知道这张牌了。
Q先生：我也知道了。
听罢以上的对话，S先生想了一想之后，就正确地推出这张牌是什么牌。
请问：这张牌是什么牌？''',
        'choise':['红桃Q','黑桃8','梅花6','方块5'],
        'answer':3


        },
        {
            'question':'''
机器人 Marin 今天的心情怎么样？''',
        'choise':['他自我感觉良好','他可能需要一些心理辅导','他非常开心','生活中需要一些小惊喜','他在思考人生'],
        'answer':3
        }
    ]
    len_question=len(question_lists)
    total_correct_question=0

    for i in range(len_question):


        # 打印题目
        print(question_lists[i]['question'],'\n')

        len_choise=len(question_lists[i]['choise'])
        # 打印选项
        for j in range(len_choise):
            
            print('选项{0}:{1}'.format(chr(ord('A')+j),question_lists[i]['choise'][j]))

        print('\n请输入选项字母序号,由A到{}:'.format(chr(ord('A')+len_choise-1)))
        ok = False
        while not ok:

            input_user=input()
            
            ok=correct_input(input_user,len_choise)

        correctanswer=question_lists[i]['answer']

        temp=correct_answer(input_user,correctanswer)
        if temp == 1:
            total_correct_question+=1


    print('答题结束，总共{0}道题，正确{1}道题'.format(len_question,total_correct_question))


    


if __name__=='__main__':
    main()
