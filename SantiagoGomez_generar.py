import numpy as np

#Definimos la primera funcion de sampleo
def sample_1(N):
    # Inicializamos el array y los numeros de samplep
    n_aleat = np.zeros(N)
    a = [-10,-5,3,9]
    #Ciclo que en cada iteracion hace el sampleo 
    for i in range(N):
        n_aleat[i] = np.random.choice(a, p = [0.1,0.4,0.2,0.3])
    return n_aleat

#Segunda funcion de sampleo con funcion de distribucion exponencial
def sample_2(N):
    #Inicializamos el array
     n_aleat = np.zeros(N)
     #Llenamos el array con este ciclo
     for i in range(N):
        n_aleat[i] = np.random.exponential(0.5)
     return n_aleat

#Funcion que halla M promedios de una funcion de sampleo
def get_mean(sampling_fun, N, M):
    promedios = np.zeros(M)
    #Ciclo que calcula el promedio de N numeros aleatorios en cada iteracion
    for i in range(M):
        promedios[i] = np.average(sampling_fun(N))
    return promedios

M = 10000
N = [10, 100, 1000]

#Ciclo que genera M promedios para 10, 100 y 1000 numeros aleatorios
for n in N:
    promedio_s1 = get_mean(sample_1,n,M)
    promedio_s2 = get_mean(sample_2,n,M)
    np.savetxt('sample_1_' + str(n) + '.txt',promedio_s1)
    np.savetxt('sample_2_' + str(n) + '.txt',promedio_s2)
    
