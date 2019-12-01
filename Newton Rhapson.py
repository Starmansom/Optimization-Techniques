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
def ftwo(z):
    if(-0.01<z<0.01):
        delz=0.01*z
    else:
        delz=0.0001*z
    f2=(f(fx,z+delz)+f(fx,z-delz)-(2*f(fx,z)))/(delz**2)
    return f2
print("Enter the initial point: ")
a=float(input())

print("Enter '1' if No.of iterations or '0' if termination constant is given: ")
y=int(input())
n=0
if(y==1):
    print("Enter the number of iterations n: ")
    n=int(input())
    for i in range(0,n):
        a=a-(fone(a)/ftwo(a)) 
    print('Minimum value :{}'.format(a))
else:
    print("Enter value of termination constant 'e': ")
    e=float(input())
    while True:   
        if abs(fone(a))<e:
            print('Minimum value: {}'.format(a))
            break
        a=a-(fone(a)/ftwo(a))
        n=n+1
print('Number of iterations: {}'.format(n))