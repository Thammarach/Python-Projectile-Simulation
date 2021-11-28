import matplotlib.pyplot as plt
import math

def check(a):
    x=0
    status=1
    for c in a :
        if ord(c)==46 and x==0 :
            status=0
        elif ord(c)!=46  :
           if ord(c)<48 or ord(c)>57 :
               status=0
        x+=1
    if status==0 :
        print("The value is incorrect")
    return status     
print("Hello,I am projectile calculate project")

u=0
vy=0
Sy_t=0
g=-9.8
t=0
Sx=0
angle=0
vx=0
t_stop=0
uy=0
ux=0
while True:
        while True:
            while True:
                angle=input("Enter Angle between move direction and x-axis in positive term degree(number only) : ")
                if check(angle)==1 :
                    angle=int(angle)
                    break
            while True:
                u=input("Enter start velocity in meter per second(number only): ")
                if check(u)==1 :
                    break
            if len(u)!=0:
                u=float(u)
            if angle != 0 and u !=0  :
                break
            else :
                print("Please Enter angle and start velocity")
        while True:
            vy=input("Input final vertical velocity in meter per second(number only): ")
            if check(vy)==1 or vy=="" :
                break
        if len(vy)!=0:
                vy=float(vy)
        while True:
            Sy_t=input("Input vertical distance in meter(number only) : ")
            if check(Sy_t)==1 or Sy_t=="" :
                break
        if len(Sy_t)!=0:
                Sy_t=float(Sy_t)
        while True:
            Sx=input("Input horizontal distance in meter(number only) : ")
            if check(Sx)==1 or Sx=="" :
                break
        if len(Sx)!=0:
                Sx=float(Sx)
        while True:
            t=input("Input movement time in second(number only) : ")
            if check(t)==1 or t=="" :
                break
        if len(t)!=0:
                t=float(t)
        while True:
            vx=input("enter final horizontal velocity in meter per second(number only) : ")
            if check(vx)==1 or vx=="" :
                    break
        if len(vx)!=0:
                Sy_t=float(vx)
        count=0
        check_list=[u,vy,Sy_t,t]
        for i in range(4) :
            if check_list[i] == "" :
                count+=1
        if count <=2 :
            break
        else :
            print("Please enter more value ")
############################################################################################
print("t",t)
print("u",u)
t_stop=0
uy=0
ux=0
t_stop=0
rad=(angle*math.pi)/180.0

if  u!= "" :
    uy=u*math.sin(rad)
    ux=u*math.cos(rad)
    t_stop=-uy/g
    print("ux",ux)
if Sx== "" and t != "" :
    Sx=0
    Sx=ux*t
    print("Sx",Sx)
if Sy_t== "" :
    if vy == "" and t!=""  :
        vy=0
        vy=uy+(g*t)
    elif uy == "" and t!="" :
        uy=0
        uy=vy-(g*t)
    elif t=="" and vy!="" and uy!="" :
        t=0
        t=(vy-uy)/g
    if uy!="" and t!="" :
        Sy_t=uy*t+(g*t**2)/2.0
elif t=="" :
    if vy=="" and uy !="" and Sy_t!="" :
        vy=0
        vy=math.sqrt(uy**2+(2*g*Sy_t))
    elif uy=="" and vy !="" and Sy_t!="" :
        uy=0
        uy=math.sqrt(vy**2-(2*g*Sy_t))
    elif Sy_t =="" and vy!="" and uy!="" :
        Sy_t=0
        Sy_t=(vy**2-uy**2)/g
    if uy!="" and t!="" :
        vy=uy+g*t
if Sx== "" and ux!="" and t!="" :
    Sx=ux*t
########################
Sy_tf=0
t_list=[]
Sy_list=[]
Sy=0
t_int=int(t)
print("t_stop",t_stop)
for i in range(0,t_int+1) :
        if i>t_stop :
            t_list.append(i)
            Sy_stop=uy*(t_stop)+(g*t_stop**2)/2.0
            Sy_tf=(-g*(i-t_stop)**2)/2.0
            Sy=Sy_stop-Sy_tf
            Sy_list.append(Sy)
        else :
            t_list.append(i)
            Sy=(uy*i)+(g*(i**2))/2.0
            Sy_list.append(Sy)
################################
print("variable choice\n1.vy\n2.Sy_t\n3.t\n4.Sx\n5.vx\n6.t_stop\n7.uy\nif you do not want to know any variable key None")
ans=input("What is the thing which you want to know ?\n" )
anslist1=["vy","Sy_t","t","Sx","vx","t_stop","uy"]
ans_var=0
for i in range(7):
    if ans==anslist1[i]:
        ans_var=i
anslist=[vy,Sy_t,t,Sx,vx,t_stop,uy]
if ans!="None" :
    print("The value of variable which you want to know is",anslist[ans_var]) 
#################################
print("time list is ",t_list,"vertical distance is ",Sy_list)

plt.plot(t_list,Sy_list,color="blue",linewidth=5)
plt.xlabel("t (s)")
plt.ylabel("Sy (m)")
plt.title("relationship between vertical distance and time")
plt.grid()
plt.show()
