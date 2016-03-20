x= int(input('Enter first number: '))
y= int(input('Enter second number: '))
flag=0
for i in range(x,y+1):
    if i > 1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
            flag=1
if flag==0:
    print('No primes found')
