E={'first_name:':'Bob',
   'first_age:':'年龄：40',
   'last_age:':'年龄：20',
   'last_name:':'Alen',
   'first_city:':'华盛顿',
   'last_city:':'北洋克顿'
   }
print(E['first_name:'])
print(E['first_age:'])
print(E['first_city:'])
print(len(E))

print('')

print(E['last_name:'])
print(E['last_age:'])
print(E['last_city:'])

print('')
print('')
print('')

human={'A:':'5','B:':'2'}
print('A:','我非常喜欢数字：',human['A:'])
print('B:','我非常喜欢数字：',human['B:'])

print('')
print('')

cihuibiao={
   'if':'如果',
   'elif':'否则如果',
   'or':'或',
   'and':'和',
   'for':'for循环'
   }
print('if:',cihuibiao['if'])
print('elif:',cihuibiao['elif'])
print('or:',cihuibiao['or'])
print('and:',cihuibiao['and'])
print('for:',cihuibiao['for'])

print('')
print('')


cihuibiao2={
   'if':'如果',
   'elif':'否则如果',
   'or':'或',
   'and':'和',
   'for':'for循环',
   'key':'键',
   'value':'值对',
   'del':'删除',
   'print':'打印',
   'imput':'导入库',
   }
for key,value in cihuibiao2.items():
   print('\n键:',key)
   print('值:',value)

print('')
print('')

rver={
   'nile':'egypt',
   'yellow rivr':'china',
   'yangtze':'china',
   'amazon rivr':'brazil, peru, colombia'
   }
for keys,value in rver.items():
   print('The ',keys,' runs through',value)

print('')
print('')

for key in rver:
   print(key)

print('')


for values in rver.values():
   print(values)


print('')



favorite_languages = { 'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python',
                       }

Should_people_surveyed_list={'jen',
                             'edward'
                             }
for i in favorite_languages:
   if i in Should_people_surveyed_list:
      print(i,'感谢您参加调查\n')
   
   if i not in Should_people_surveyed_list:
      print(i,'没参加调查\n')
   





