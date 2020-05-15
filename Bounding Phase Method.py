import math
val=0
def update(x,k):
    global dell,f,val
    if(f==1):
        val=x+(pow(2,k)*dell)
    elif(f==-1):
        val=x-(pow(2,k)*dell)
    return val

def function(fx,x):
    global val
    try:
        val=eval(fx)
    except:
        val=9999999999
    return val

def log(line):
	global file
	file.write(str(line)+'\n')

def check(x0):
    global dell,val
    x1=x0+dell
    xn1=x0-dell
    if(function(fx,xn1)>function(fx,x0) and function(fx,x0)>function(fx,x1)):
        val=1
    elif(function(fx,xn1)<function(fx,x0) and function(fx,x0)<function(fx,x1)):
        val=-1
    else:
        print("error")
    return val
x=[]
f=[]
c=[]
print("Bounding Search  Method")
fx=str(input("Function: "))
x0=float(input("Initial Value(x0): "))
x.append(x0)
dell=float(input("Del value: "))
f=check(x0)
#file
file=open('bounding_log','w')
file.write("\n\n^^^Bounding Search Method^^^\n\n")
file.write("GIVEN DATA:\n\tf(x)={}\n\tx0={}\n\tdel={}\n\n".format(fx,x0,dell))

log('xk\txk(+/-)1\tf(xk)\t\t\tf(xk+1)\t\t\tCONDITION')
k=0
while(1):
	x.append(update(x[k],k))
	a=function(fx,x[k])
	b=function(fx,x[k+1])
	if(len(str(a))<17):
		c=str(a).zfill(17)
	else:
		c=a
	if(len(str(b))<17):
		d=str(b).zfill(17)
	else:
		d=b
	if(a<b):
		log('{}\t{}\t{}\t{}\tTRUE'.format(x[k],x[k+1],c,d))
		break
	log('{}\t{}\t{}\t{}\tFALSE'.format(x[k],x[k+1],c,d))
	k=k+1
#print(x)
log("\n[+]Interval found at [{},{}]".format(x[k-1],x[k+1]))
file.close()
file=open('bounding_log','r')
print(file.read())
file.close()
print("\n\n[-]Program has ended")
input("press [RETURN] to continue")
