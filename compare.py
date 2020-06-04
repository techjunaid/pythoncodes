x = str(input('enter three numbers'))
x = tuple(x)
print(type(x))
a,b,c = x
a=int(a)
b=int(b)
c=int(c)
print(a,b,c)
if a>b&a>c:
    print('a is greater')
elif b>a&b>c:
    print('b is greater')
else:
    print('c is greater')
