C=input('你想要什么样的汽车?:')
print('Let me see if I can find you a',C)

P=int(input('请问你你们有多少人吃饭？:'))
if P < 9:
    print('我们的位置刚好够{}个'.format(P))
elif P > 8:
    print('我们没有位子了')

N=int(input('请输入数字:'))
if N%10==0:
    print('这个数字{}是10的整数倍'.format(N))
else:
    print('这个数字{}不是10的整数倍'.format(N))