name=['1','2','3','4']
print(name)
print('3,无法赴约')
name.remove('3')
print(name)

print('')

print('找到了一个更大的餐桌')
name.insert(0,'6')
print(name)

print('')
name.insert(3,'5')
print(name)

print('')
name.append('7')
print(name)

print('')
print('')
print('')

print('抱歉，新餐桌遇到意外，无法及时送达，现在只能邀请两位')

print('非常抱歉:',name.pop(0),'你不在我名单里')

print('非常抱歉:',name.pop(3),'你不在我名单里')

print('非常抱歉:',name.pop(3),'你不在我名单里')

print('')

for names in name:
    print('很高兴你还在我名单里:',names,'!')

print('')

del name[0:]
print(name)


print('')
print('')

T=['New York','Washington','Beijing','Shanghai','Sydney','Tokyo']
print(T)

print('')

print(sorted(T))

print('')

print(T)

print('')

print(T[::-1])
#倒着打印列表

print('')

print(T)

T.reverse()

print('')

print(T)

T.reverse()

print('')

print(T)

print('')

T.sort()

print(T)

print('')

T.sort(reverse=True)

print(T)

print('')

print(len(name))



