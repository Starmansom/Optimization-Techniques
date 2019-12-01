import math
def f(x):
    fun=x**2+(54/x)
    return fun  
print("Enter the initial point: ")
a=float(input())
print("Enter step size delta: ")
de=float(input())
b=a+de
if f(a)>f(b):
    c=a+(2*de)
else:
    c=a-de
print("Enter '1' if No.of iterations or '0' if termination constant is given: ")
y=int(input())
if(y==1):
    print("Enter the number of iterations: ")
    n=int(input())
    for i in range(0,n):
        fmin=min(f(a),f(b),f(c))
        if fmin==f(a):
            xmin=a
        elif(fmin==f(b)):
            xmin=b
        else:
            xmin=c   
        a0=f(a)
        a1=(f(b)-f(a))/(b-a)
        a2=(((f(c)-f(a))/(c-a))-a1)*1/(c-b)
        xbar=(((a+b)/2))-(a1/(2*a2))
        fmin1=min(f(a),f(b),f(c),f(xbar))
        if ((xbar>=a) and (xbar<=b)):
            b=xbar
            c=b
        else:
            a=b
            b=xbar
            
else:
    n=11
    print("Enter value of termination constant 'e': ")
    e=float(input())
    while True:
        fmin=min(f(a),f(b),f(c))
        if fmin==f(a):
            xmin=a
        elif(fmin==f(b)):
            xmin=b
        else:
            xmin=c   
        a0=f(a)
        a1=(f(b)-f(a))/(b-a)
        a2=(((f(c)-f(a))/(c-a))-a1)*1/(c-b)
        xbar=(((a+b)/2))-(a1/(2*a2))
        n=n+1
        if((xbar>=a) and (xbar<=b)):
            b=xbar
            c=b
        else:
            a=b
            b=xbar
        if((abs(xbar-xmin)<e) and (abs((f(xbar)-f(xmin))<e))):
            break
            
if fmin1==f(a):
    xmin=a
elif(fmin1==f(b)):
    xmin=b
elif(fmin1==f(c)):
    xmin=c 
else:
    xmin=xbar
print('Minimum value: {}'.format(xmin))
print('Number of iterations: {}'.format(n))













        