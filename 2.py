'''
age=int(input("请输入年龄："))
if age >= 18:
    print("请您输入的年龄是{age}，已经成年，可以上网")
else:
    print("吃屎吧你，未成年上毛网")
'''


age = int(input("请输入您的年龄："))
if age < 18:
    print(f"您输入的年龄{age}，童工")
elif (age >= 18) and (age <=60):
    print(f'您输入的年龄{age}，合法了')
elif (age > 60):
    print(f'{age},已到退休年龄')