a=int(input('enter a numbr '))
b=int(input('enter another number '))
c=input('enter the math operation /,*,+,- ')
if(c=='/'):
    print(a/b)
elif(c=='*'):
    print(a*b)
elif(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
else:
    print('invalid operation')
