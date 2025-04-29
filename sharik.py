import math

import matplotlib.pyplot as plt



omega = math.pi # угловая частота
A = 1 # амплитуда
alpha = 0 # потери
fita = 0.5*math.pi # начальная фаза
deltat = 0.001 # шаг симуляции
time = 0 # счётчик времени
g = 10 
Xball = 1 #начальная высота
vball = 10 #начальная скорость

yv=[]
xt=[]
xy=[]

xrody=[]

Hmax = 0 # максимальная высота


def xrod(t):
    return A*math.sin(omega*t+fita)
def vrod(t):
    return omega*A*math.cos(omega*t+fita)
def Hball_():
    return xball(vball/g)
def xball(t):
    return Xball+vball*t-(g / 2)*t**2
def vball_(t):
    return -g*t+vball
coltimee = 0 # время прошедшее с прошлого удара

def tick():
    global coltimee
    global time
    coltimee += deltat
    time += deltat


if xball(0)<xrod(0):
    print("шарик оказался под стержнем")
    input()
    exit(1)
    

    
while time<1000:
    if xball(coltimee)<xrod(time):
        plt.axvline(time,color="black")
        Xball=xrod(time)

        vball = -vball_(coltimee)+2*vrod(time)
        vball *= math.sqrt(1-alpha)
        Hmaxball = Hball_()
        plt.plot(time,Hmaxball, color='green',marker='+')
        if Hmaxball >Hmax :
            Hmax=Hmaxball
        # if Hmaxball>A:
            # st = math.sqrt(vball**2+2*g*(Hmaxball-xball(coltimee)))/(-g) # попытки оптимизации
            # ttt = max(vball / g + st, vball / g - st)
            # if ttt<0:
                # print("Р·РµРїР°")
                # input()
            # time += ttt
            # coltimee += ttt 
        # else:
            # tick()
        coltimee = 0
        tick()
    else:
        tick()
    yv.append(vball_(coltimee))
    xt.append(time)
    xy.append(xball(coltimee))
    xrody.append(xrod(time))

plt.plot(xt,yv,color="red")

plt.plot(xt,xy)
plt.plot(xt,xrody,color="gray")
plt.show()