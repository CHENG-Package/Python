#mountain_poll,例子
UnC_users=['candace','brian','alice']
conf_uesrs=[]

while UnC_users:
    current_users=UnC_users.pop()
    conf_uesrs.append(current_users)
    current_users=current_users.split()
    current_users.sort()
    print('效验用户:',current_users)
print('\n以下用户已确认:')
for current_user in conf_uesrs:
    print(current_user)

print('习题:\n')

sandwich_orders=['口袋三明治','火腿三明治','烤肉三明治']
finished_sandwiches=[]

for sandwich_order in sandwich_orders:
    print('I made your:',sandwich_order)


while sandwich_orders:
    finished_sandwiche=sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwiche)
    print(finished_sandwiches)

print('')


sandwich_orders=['pastrami','口袋三明治','pastrami','火腿三明治','烤肉三明治','pastrami']
print('pastrami卖完了')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

print('')

input('如果你能去世界上某一个地方，你会去哪里?\n')


























