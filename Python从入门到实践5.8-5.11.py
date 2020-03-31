user=['A','B','C','D','admin']
if 'admin'in user:
        print('Hello admin, would you liketo seeastatus report?')
for users in user[:4]:
    print('Hello ',users,', thank you for logging in again')

print('')
print('')

del user[0:]
if user==[]:
        print('We neeed to find some users')
else:
        print('你没删完')

print('')
print('')
print('')


current_users=['1','2','3','4','5']
new_users=['2','3','5','6','7']

for i in new_users:
     if i in current_users:
            print(i,'这不能用') 
     else: print(i,'可以用')


print('')
print('')
print('')

L1=[1,2,3,4,5,6,7,8,9]

for i in L1:
        if i==1:
                print(str(i)+'st')
                print('')
        elif i==2:
                print(str(i)+'nd')
                print('')
        elif i==3:
                print(str(i)+'rd')
                print('')
        else:
                print(str(i)+'th\n')
