import numpy as np
import matplotlib.pyplot as plt


def V1(t):
    return np.cos(t)

def V1_prime(t):
    return -np.sin(t)

def V2(t):
    return np.sin(t)

def V2_prime(t):
    return np.cos(t)

def V3(t):
    return np.exp(-1/2*t)*(1/13 *(16*np.cos(np.sqrt(3)/2*t)+22/np.sqrt(3)*np.sin(np.sqrt(3)/2*t))+1/13*(-3*np.cos(2*t)+2*np.sin(2*t)))

def V3_prime(t):
    return -1/2*np.exp(-1/2*t)*(1/13*(16*np.cos(np.sqrt(3)/2*t)+22/np.sqrt(3)*np.sin(np.sqrt(3)/2*t)))+np.exp(-1/2*t)*(1/13*(-8*np.sqrt(3)*np.sin(np.sqrt(3)/2)+11*np.cos(np.sqrt(3)/2)))+1/13*(6*np.sin(2*t)+4*np.cos(2*t))

def V4(t):
    return np.exp(-1/2*t)*(1/13 *(3*np.cos(np.sqrt(3)/2*t)+35/np.sqrt(3)*np.sin(np.sqrt(3)/2*t))+1/13*(-3*np.cos(2*t)+2*np.sin(2*t)))

def V4_prime(t):
    return -1/2*np.exp(-1/2*t)*(1/13*(3*np.cos(np.sqrt(3)/2*t)+35/np.sqrt(3)*np.sin(np.sqrt(3)/2*t)))+np.exp(-1/2*t)*(1/13*(-3*np.sqrt(3)/2*np.sin(np.sqrt(3)/2)+35/2*np.cos(np.sqrt(3)/2)))+1/13*(6*np.sin(2*t)+4*np.cos(2*t))



def plot_solution(V,t,v0,v1):
    x=np.arange(0,t,0.1)
    y=V(x)
    plt.plot(x,y)
    plt.title("Graphe de V pour les conditions : V(0)="+str(v0) +", V'(0)="+str(v1))
    plt.show()

def phase_plot(t,f,fprime):
    T=np.arange(0,t,0.1)
    x=f(T)
    y=fprime(T)
    plt.plot(x,y)
    plt.show()


def X1(t):
    return np.exp(-1/200*t)*(200/np.sqrt(399)*np.sin(np.sqrt(399)/200*t))

def X2(t):
    return np.exp(-1/200*t)*(np.cos(np.sqrt(399)/200*t)-np.sqrt(399)*np.sin(np.sqrt(399)/200*t))

