import cmath
import math
a= float(input('what is the value of a ? '))
b= float(input('what is the value of b ? '))
e= float(input('what is the termination value  ? '))
print('given intervel ',(a,b))
A=int(0)
B=int(1)
l=B-A
print('l= ',l)
w1=A+(0.618*l)
w2=B-(0.618*l)
x1=((b-a)*w1+a)
x2=((b-a)*w2+b)
print('x2=',x2)
print('l is this' ,l)
i=int(input('if it is iterative then give the value of i'))
if i==0:
      while l>e:
        w1=A+(0.618*l)
        print(w1)
        w2=B-(0.618*l)
        print(w2)
        x1= ((b-a)*w1+a)
        x2= ((b-a)*w2+a)
        f1=float((x1**2)+(54/x1))
        f2=float((x2**2)+(54/x2))
        print('f1=',f1)
        print('f2=',f2)
        if (f1<f2):
            A=w2
            B=B
            print(x2)
            print('new intervel is',(A,B))
            l=B-A
            print('l is this',l)
        else:
            A=A
            B=w1
            print('new intervel is',(A,B))
            l=B-A

n=1            
if i>0:
    for i in range(1,i):
        w1=A+(0.618*l)
        print(w1)
        w2=B-(0.618*l)
        print(w2)
        x1= ((b-a)*w1+a)
        x2= ((b-a)*w2+a)
        f1=float((x1**2)+(54/x1))
        f2=float((x2**2)+(54/x2))
        print('f1=',f1)
        print('f2=',f2)
        if (f1<f2):
            A=w2
            B=B
            print(x2)
            print('new intervel is',(A,B))
            l=B-A
            print('l is this',l)
        else:
            A=A
            B=w1
            print('new intervel is',(A,B))
            l=B-A
         

C=A*(b-a)+a
D=B*(b-a)+a
print('Final  intervel is',(C,D))


           
    

        
   

            
            
        
   
    

    
    
    
