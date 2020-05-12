#alens
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for ailen in aliens:
    print(ailen)

print('')
print('')


aliens_3=[]

for alien_number in range(1,31):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens_3.append(new_alien)

for alien in aliens_3[:6]:
    print(new_alien)

print('................................................')
print('一共创建了:',str(len(aliens_3)),'个外星人')

print('')
print('')


aliens_4=[]

for alien_N in range(0,31):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens_4.append(new_alien)

for alien in aliens_4[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

for alien in aliens_4[0:7]:
    print(alien)

print('')
print('')

#pizza
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }

print('uyuou ordered a',pizza['crust'],'-crust pizza','with the following toppings:')

for topping in pizza ['toppings']:
    print(topping)

print('')
print('')


#favorite_languanges.py

fl={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
    }

for name,languages in fl.items():
    print(name.title(),"'s favorite_languanges are:")
    for language in languages:
        print('\t',language)

print('')
print('')

#many_users.py

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        },
    }

for username,user_info in users.items():
    print('Username:',username)
    print('')
    full_name = user_info['first']+user_info['last']
    location = user_info['location']

    print('Full name:\n'+ str(full_name),'\n')
    
    print('Location:\n'+ str(location),'\n')

print('————————习题————————')

people=[
    {'first_name:':'Bob',
        'first_age:':'年龄：40',
        'last_age:':'年龄：20',
        'last_name:':'Alen',
        'first_city:':'华盛顿',
        'last_city:':'北洋克顿'
    },
    {'first_name:':'马卡洛夫',
        'last_name:':'尼古莱'
    },
    {'first_name:':'卡马洛夫',
        'last_name:':'想不起来了'
    }
]








































