T='输入一些你想要的披萨配料：'
ingredients_list=[]
while True:
    CM=input(T)
    if CM == '退出':
        break
    else:
        ingredients_list.append(CM)
        print('我们会为你添加',ingredients_list,'配料')
        print("\n输入'退出',结束你想要添加的配料")
        continue



print('--------------------------------------')

age=int(input('你的年龄:'))
while age:
    if age < 3:
        print('三岁以下免费')
        break
    elif 3<=age<12:
        print('收费10$')
        break
    else:
        print('收费15$')
        break


import time

start=time.time()
age=10
while age:
    if age < 3:
        print('三岁以下免费')
        break
    elif 3<=age<12:
        print('收费10$')
        break
    else:
        print('收费15$')
        break
end=time.time()
print('%s'%(end-start))

print(' ')

start=time.time()
age=10
while age:
    if age < 3:
        print('三岁以下免费')
        break
    elif 3<=age and age<12:
        print('收费10$')
        break
    else:
        print('收费15$')
        break
end=time.time()
print('%s'%(end-start))







