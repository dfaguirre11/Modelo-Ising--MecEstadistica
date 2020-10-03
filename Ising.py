#Tarea 3- Mecanica Estadistica - modelo de Ising
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

#%%% Calculo de energia
def Estado(i,j):
    A[i,j] = -A[i,j] # Cambio de estado de un espin
    
def Energia(): # Energia total de la red
    E_T = 0
    for i in range(N):
        for j in range(N):
            E_T += -A[i,j]*(A[(i+1)%N,j]+ A[(i-1)%N,j]+A[i,(j+1)%N]+A[i,(j-1)%N])
            # calculo de la energia de interaccion y sumado
def Magnetizacion():
    return np.sum(A)/N**2 # Calculo magnetizacion
    
def Metstep(alpha): # Algoritmo metropolis
    for k in range(N**2):
        i = rand.randint(N) # Seleccion de espin a la azar
        j = rand.randint(N)
        dE = 2*A[i,j]*(A[(i+1)%N,j]+ A[(i-1)%N,j]+A[i,(j+1)%N]+A[i,(j-1)%N])
        # Cambio de energia
        if (dE <=0 or np.exp(-alpha*dE)> rand.rand()):
            Estado(i,j) # Cambiar de estado
def CalculoVariables(alpha,A,mcsteps):
    # simulacion
    t = np.linspace(1,mcsteps,mcsteps)
    E = [] # Energia
    M = [] # Magnetizacion
    for i in range(mcsteps):
        Metstep(alpha) # Paso
        E.append(Energia())
        M.append(Magnetizacion())
    return (t,E,M)
#%%
T_f = np.array([1/4,1/2,3/4,7/8,15/16,17/16,9/8,5/4,3/2,7/4])
# Temperaturas
alpha_c = 0.44069 # DEfinido en el informe
#Critico
alpha = alpha_c/T_f
#%%
N = 40
EE = []
MM = []
for l in range(8):
    rand.seed(6)
    A_0 = np.ones([N,N])
    A = A_0 + 2*rand.randint(-1,1,(N,N))
    # Inicializacion de la matriz de espines
    (t,E,M) = CalculoVariables(alpha[l],A,10000)
    EE.append(np.mean(E[2000:]))
    MM.append(np.mean(M[2000:]))

#%% Graficas 
plt.figure()
plt.scatter(T_f,np.abs(MM))
plt.xlabel('T/Tc')
plt.ylabel('M/N')
plt.savefig('Mac.jpg') 
#%%
plt.figure()
plt.scatter(T_f,EE)
plt.xlabel('T/Tc')
plt.ylabel('E/JN')
plt.savefig('Ener.jpg') 
    
