#exhaustive search method
import math

def update(x):
    global dell
    val=x+dell
    return val

def function(fx,x):
    try:
        #print("in try")
        val=float(eval(fx))      
    except:
        #print('in except')
        val=float(9999999)
    return val
def log(x):
    file.write(str(x)+'\n')


print("Exhaustive Search Method")
rage=[]
fx=str(input("Function: "))
ipoints=int(input("Intermediate points: "))
interval=str(input("Interval: "))
interval=interval.strip('[]').split(',')
rage.append(float(interval[0]))
dell=float((float(interval[1])-float(interval[0]))/ipoints)

#file
file=open('exhaustive_log','w')
file.write("\n\n^^^Exhaustive Search Method^^^\n\n")
file.write("GIVEN DATA:\n\tf(x)={}\n\tn={}\n\tdel={}\n\n".format(fx,ipoints,dell))

log('x1\tx2\tx3\tf(x1)\t\t\t\tf(x2)\t\t\t\tf(x3)\t\t\t\tCONDITION\n')
k=0
while(1):
    rage.append(update(rage[k]))
    rage.append(update(rage[k+1]))
    a=function(fx,float(rage[k]))
    b=function(fx,float(rage[k+1]))
    c=function(fx,float(rage[k+2]))
    print(str(a)+str(b)+str(c))
    if(len(str(a))<17):
        aa=str(a).zfill(17)
    else:
        aa=a
    if(len(str(b))<17):
        bb=str(a).zfill(17)
    else:
        bb=b
    if(len(str(c))<17):
        cc=str(c).zfill(17)
    else:
        cc=c
    if(a>=b and b<=c):
        log('{}\t{}\t{}\t{}\t\t{}\t\t{}\t\tTRUE'.format(rage[k],rage[k+1],rage[k+2],aa,bb,cc))
        break
    else:
        log('{}\t{}\t{}\t{}\t\t{}\t\t{}\t\tFALSE'.format(rage[k],rage[k+1],rage[k+2],aa,bb,cc))
    k=k+1
    rage.append(rage[k])
    k+=2
log("\n[+]Interval found at [{},{}]".format(rage[k-2],rage[k+2]))
file.close()
file=open('exhaustive_log','r')
print(file.read())
file.close()
print("\n\n[-]Program has ended")
input("press [RETURN] to continue")