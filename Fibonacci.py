import math
def fib(n):
    x=[0]*n
    if n==1:
        return 1
    if n==2:
        return 2
    x[0]=1
    x[1]=2
    for i in range(2,n):
        x[i]=x[i-1]+x[i-2]
    return x[n-1]
    

def f(fx,x):
    val=eval(fx)
    return val

print("Fibonacci Search Method")
k=2
limit=[]
fx=str(input("Function: "))
limit=list(map(float,input('Interval: ').split(',')))
m=int(input("Function Evaluations: "))
i=1
L=limit[1]-limit[0]
while(i<m):
        #print(limit)        
        LL=(fib(m-k+1)/fib(m+1))*L
        x1=limit[0]+LL
        x2=limit[1]-LL
        print("{} {} {} {}".format(L,LL,x1,x2))
        if(f(fx,x1)>f(fx,x2)):  
            limit[0]=x1
        elif(f(fx,x2)>f(fx,x1)):
            limit[1]=x2
        else:
            print("error")
        k+=1
        i+=1
print("[+] Interval found at {}".format(limit))
input("press [RETURN] to continue")