
a = 1 #a是1
while a < 7: #判断a<7是几？
    if(a % 2 == 0):#判断6除以2 不等于0 是 a是奇数还是偶数
        print(a,"is even")#是偶数
    else:
        print(a,"is odd")#是奇数
    a += 1 #这块什么意思呢？
#当a小于7时，while循环，如果不满足a小于7这个条件的话就不循环
# 懂了 a=8时 while就不会循环     a=a+1 这个意思就是一直相加循环 一直到不满足a小于7这个条件的话就不循环

flag = False
name = 'luren'
if name == 'python':  # 判断变量是否为 python
    flag = True  # 条件成立时设置标志为真
    print
    'welcome boss'  # 并输出欢迎信息
else:
    print(name)
a = 2 + 2
print(a)

num = 5
if num == 3:           # 判断num的值
    print ("boss")
elif num == 2:
    print ("user")
elif num == 2:
    print ("worker")
elif num < 0:          # 值小于零时输出
    print("error")
else:
    print("牛批")       # 条件均不成立时输出


num = 10
if (num >= 0 and num <= 5) or (num >=10 and num <=15) : #判断数字是否满足该条件
    print("正确")                                        #满足条件打印
else:                                                   #否则
    print("未定义")                                      #不满足条件打印
