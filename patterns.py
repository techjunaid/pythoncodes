
'''x= int (input('enter the range you want::'))
for i in range(2,x+1):
    for j in range(i-1,x):
        print(j,end= ' ')

    print()



for i in range (5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()'''

for i in range (6):
    for j in range(i):
        print('*',end=' ')
    print()
#pyramid
for i in range(5):
    for j in range(5-i-1):
        print(end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print('')


for i in range(5):
    for j in range(5 - i-1):
        print(end=' ')
    for j in range(i+1):
        print('*',end=' ')

    print('')

for i in range(5,0,-1):
    for j in range(5 - i ):
        print(end=' ')
    for j in range(i ):
        print('*', end=' ')

    print('')


## right triangle

num=int(input('enter the rows you want :'))
n=1
for i in range(num):
    for j in range(i+1):
        print(format(n,'<4'),end=' ')
        n=n+1
    print()
