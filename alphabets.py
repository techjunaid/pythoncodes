
## ALPHABET FORMAT

'''for i in range():
    for j in range ():
        if
            print('*',end=' ')
        else:
            print(end='  ')
    print()'''


##code for A
for i in range (4):
    for j in range(3):
        if j==1 or (i==0 and j!=1  ) or (i==3 and j!=1):
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


    ## code for O
for i in range(7):
    for j in range (5):
        if ((j==0 or j==4) and (i==2 or i==3 or i==4))  or ((j==1 or j==3) and (i==1 or i==5))  or (j==3  and (i==0 or i==6)):
            print('*',end=' ')
        else:
            print(end=' ')
    print()

## code for F
for i in range(5):
    for j in range(3):
        if (j==0 or (i==0 and j!=0)) or (i==2 and (j!=0)):
            print('*', end=' ')
        else:
            print(end='  ')
    print()

##code for R

for i in range(5):
    for j in range (4):
        if j==0 or ( j==1 and (i==0 or i==2)) or ( j==2 and (i==0 or i==1 or i==3)) or (j==3 and i==4):
            print('*',end=' ')
        else:
            print(end=' ')
    print()


    ## code for A

for i in range(5):
    for j in range (5):
        if ((j==0 or j==4) and (i==2 or i==3 or i==4)) or ((i==1 or i==3) and (j==1 or j==3)) or (j==2 and (i==0 or i==3)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()




