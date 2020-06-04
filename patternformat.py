
## ALPHABET FORMAT

'''for i in range():
    for j in range ():
        if
            print('*',end=' ')
        else:
            print(end='  ')
        print()'''


    ##i shape
for i in range (6):
    for j in range(5):
        if j==2 or (i==0 and j!=2  ) or (i==5 and j!=2):
            print('*',end=' ')
        else:
            print(end='  ')
    print()


    ## j shape

for i in range(5):
    for j in range(3):
        if j==1 or (i==0 and j!=1) or(i==4 and j<=1):
            print('*',end=' ')
        else:
            print(end='  ')
    print()



## s shape

for i in range(5):
    for j in range (3):
        if (i==0 or (i==1 and j<1 )) or (i==2 or (i==3 and j==2)) or (i==4 ):
            print('* ',end=' ')

        else:
            print( end='  ')
    print()