import math
#internal halfing method
def f(fx,x):
    val=eval(fx)
    return val

p=input("Interval: ")
p=p.strip('[]').split(',')
a=float(p[0])
b=float(p[1])
tol=float(input('Termination Factor: '))
eq=str(input('Function: '))
l=float(abs(b-a))
xm=(a+b)/2
x1=a+l/4
x2=b-l/4
fx1=f(eq,x1)
fx2=f(eq,x2)
fxm=f(eq,xm)
#fx1=x1*x1+54/x1#equation
#fx2=x2*x2+54/x2#equation
#fxm=xm*xm+54/xm
while l>=tol:
    x1=a+l/4
    x2=b-l/4
    fx1=f(eq,x1)
    fx2=f(eq,x2)
    #fx1=x1*x1+54/x1  #function()
    #fx2=x2*x2+54/x2 #function()
    if fx2<=fxm:
        a = xm
        xm = x2
        fxm = fx2
    elif (fx1<=fxm):

        b = xm
        xm = x1
        fxm = fx1
            
    else :
        a = x1
        b = x2
    l=float(abs(b-a))
print("\n[-]DATA: \n\tf(x)={}\n\tInterval={}\n\tTermination Factor={}".format(eq,p,tol))
print('\n[+]Interval found at [{},{}]'.format(a,b))
input("\npress [RETURN] to continue")