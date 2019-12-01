import math
fx=str(input("Function: "))
def f(fx,x):
    val=eval(fx)
    return val 
def fone(z):
    if(-0.01<z<0.01):
        delz=0.01*z
    else:
        delz=0.0001*z
    f1=(f(fx,z+delz)-f(fx,z-delz))/(2*delz)
    return f1

print("Enter lower limit a: ")
a=float(input())
print("Enter upper limit 'b': ")
b=float(input())
print("Enter '1' if No.of iterations and '0' if termination constant is given: ")
y=int(input())
if(y==1):
    print("Enter the number of iterations n: ")
    n=int(input())
    for i in range(0,n):
        z=b-(((b-a)*fone(b))/(fone(b)-fone(a)))
        fsingle=fone(z)
        if (fsingle>0):
            b=z
        else:
            a=z
else:
    n=0
    print("Enter the value of termination constant 'e': ")
    e=float(input())
    z=(a+b)/2
    while True:
        z=b-(((b-a)*fone(b))/(fone(b)-fone(a)))
        fsingle=fone(z)
        if (fsingle>0):
            b=z
        else:
            a=z
        n=n+1
        if(abs(fsingle)<e):
            break
print('Minimum value :{}'.format(z))
print('Number of iterations: {}'.format(n))
