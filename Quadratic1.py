import math
fx=str(input("Function: "))
def f(fx,x):
    val=eval(fx)
    return val
print("Enter the initial point: ")
a=float(input())
print("Enter step size delta: ")
de=float(input())
b=a+de
if f(fx,a)>f(fx,b):
    c=a+(2*de)
else:
    c=a-de
print("Enter '1' if No.of iterations or '0' if termination constant is given: ")
y=int(input())
if(y==1):
    print("Enter the number of iterations: ")
    n=int(input())
    for i in range(0,n):
        fmin=min(f(fx,a),f(fx,b),f(fx,c))
        if fmin==f(fx,a):
            xmin=a
        elif(fmin==f(fx,b)):
            xmin=b
        else:
            xmin=c   
        a0=f(fx,a)
        a1=(f(fx,b)-f(fx,a))/(b-a)
        a2=(((f(fx,c)-f(fx,a))/(c-a))-a1)*1/(c-b)
        xbar=(((a+b)/2))-(a1/(2*a2))
        fmin1=min(f(fx,a),f(fx,b),f(fx,c),f(fx,xbar))
        if ((xbar>=a) and (xbar<=b)):
            b=xbar
            c=b
        else:
            a=b
            b=xbar
            
else:
    n=1
    print("Enter value of termination constant 'e': ")
    e=float(input())
    while True:
        fmin=min(f(fx,a),f(fx,b),f(fx,c))
        if fmin==f(fx,a):
            xmin=a
        elif(fmin==f(fx,b)):
            xmin=b
        else:
            xmin=c   
        a0=f(fx,a)
        a1=(f(fx,b)-f(fx,a))/(b-a)
        a2=(((f(fx,c)-f(fx,a))/(c-a))-a1)*1/(c-b)
        xbar=(((a+b)/2))-(a1/(2*a2))
        n=n+1
        if((xbar>=a) and (xbar<=b)):
            b=xbar
            c=b
        else:
            a=b
            b=xbar
        if((abs(xbar-xmin)<e) and (abs((f(fx,xbar)-f(fx,xmin))<e))):
            break
            
if fmin1==f(fx,a):
    xmin=a
elif(fmin1==f(fx,b)):
    xmin=b
elif(fmin1==f(fx,c)):
    xmin=c 
else:
    xmin=xbar
print('Minimum value: {}'.format(xmin))
print('Number of iterations: {}'.format(n))