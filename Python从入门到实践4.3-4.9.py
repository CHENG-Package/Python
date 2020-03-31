for U in range(1,21):#循环U在1,21的范围内的数字
    print(U)#并打印

print('')


import time  #导入时间库
start=time.time()#开始时间

#开始计算代码段运行时间
L=[L for L in range (1,1000001)]#L=循环L在1到1百万里的数字，并强制转换为列表
print(min(L))#打印循环数字里最小的值
print(max(L))#打印循环数字里最大的值
print(sum(L))#打印循环内数字的总和
#结束计算代码段运行时间

end=time.time()#结束时间
print('%s'%(end-start))#用结束时间减去开始时间，计算出总运行时间并打印

print('')


for T in range (1,21):#循环1到20
    if T%2!=0:  #如果有21以内除以2不等于0的数
        print(T) #就打印

print('')


for E in range (3,31):#循环E在3到31以内的数字
    if E%3==0:#31以内除3等于0的数,31以内除3得不到余数的数
        print(E)#就打印

print('')


for S in range(1,11):#循环1,到10
    print(S**3)#打印每个数字的立方m³
