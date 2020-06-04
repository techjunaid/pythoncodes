x = int(input('enter the row no::'))
for i in range (1,x):
    #print('#')
    for j in range(1,i+1):
        print('*',end=' ')
    print('')

#x = int(input('enter the row no::'))
for i in range (x,1,-1):
    #print('#')
    for j in range(2,i):
        print('*',end=' ')
    print('')


x= int (input('enter the no you want::'))
for i in range(2,x+1):
    for j in range(i-1,x):
        print(j,end= ' ')

    print()

##axe ka code

k = 5 - 1
for i in range(5):
    print('  ' * k, end=' ')
    print(' *' * i)
    k -= 1


for i in range(6):

    print(' *'* i , end=' ')
    k+=1

for i in range (6-1,0,-1):
    print(' *'*i,' ')
