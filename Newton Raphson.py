import math
def f(x):
    fun=x**2+(54/x)
    return fun  
def fone(z):
    if(-0.01<z<0.01):
        delz=0.01*z
    else:
        delz=0.0001*z
    f1=(f(z+delz)-f(z-delz))/(2*delz)
    return f1
def ftwo(z):
    if(-0.01<z<0.01):
        delz=0.01*z
    else:
        delz=0.0001*z
    f2=(f(z+delz)+f(z-delz)-(2*f(z)))/(delz**2)
    return f2
print("Enter the initial point: ")
a=float(input())
print("Enter value of termination constant 'e': ")
e=float(input())
while True:    
    if abs(fone(a))<e:
        print('Minimum value: {}'.format(a))
        break
    a=a-(fone(a)/ftwo(a))