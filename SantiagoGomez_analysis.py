import numpy as np
import matplotlib.pyplot as plt

#Funcion que calcula la densidad de probabilidad normal en x con media mean y desviacion sigma

def normal_dist(x,mean,sigma):
    pi = np.pi
    p = np.sqrt(1/(2*pi*sigma**2))*np.exp(-(x - mean)**2/sigma**2)
    return p

def get_fit(filename):
    datos = np.loadtxt(filename + '.txt')
    plt.figure()
    plt.hist(datos)
    plt.savefig(filename + '.png')
    
archivos = ['sample_1_10','sample_1_100','sample_1_1000','sample_2_10','sample_2_100','sample_2_1000']    
    
