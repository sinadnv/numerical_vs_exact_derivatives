## Initiate the values
import numpy as np
import matplotlib.pyplot as plt

T = 1      # end of time domain
Num = 50   # number of time intervals, increase to see how exact and numerical derivatives line up
tau = 1     # period
omega = 2*np.pi/tau     # omega


## Define the function of interest
def f(t):
    x = np.sin(omega*t)+np.cos(omega*t)
    return x


def fprime_num(t):
    dt = t[1]-t[0]
    x = f(t)
    xprime = np.zeros(x.shape)
    for i in range(1,len(t)-1):
        xprime[i] = (x[i+1]-x[i-1])/(2*dt)

    xprime[0] = (x[1]-x[0])/dt
    xprime[-1] = (x[-1]-x[-2])/dt
    return xprime


def fprime_exact(t):
    x = omega*np.cos(omega*t)-omega*np.sin(omega*t)
    return x


## To view the difference between numerical and exact derivatives for a given Num
# t = np.linspace(0,T,Num)
# x = f(t)
# xprime_exact = fprime_exact(t)
# xprime_num = fprime_num(t)
# plt.plot(t,x)
# plt.plot(t, xprime_num)
# plt.plot(t, xprime_exact)
# plt.legend(['Function','Numerical', 'Exact'])
# plt.grid()

## To view the RMS deviation of the numerical derivative for different values of Num
error = []
for n in range(3,Num+1):
    t = np.linspace(0,T,n)
    x = f(t)
    xprime_exact = fprime_exact(t)
    xprime_num = fprime_num(t)
    errSQ = 0
    for i in range(len(x)):
        errSQ += (xprime_num[i]-xprime_exact[i])*(xprime_num[i]-xprime_exact[i])/n
    err = (errSQ**.5)*100
    error.append(err)

plt.plot(range(3,Num+1),error)
plt.grid()
plt.show()