from numpy import log
g = 2             # Fator de landé
k = 8.61e-5       # Constalte de Boltzmann (eV/K)
mb = 5.78e-5      # mi bohr (eV/T)
R = 8.31          # Constante universal dos gases
e = 2.71828




B=0
lambdas = [0,0,0,0]
T=0.01



def E1(Bef_):
    return -(g*mb*Bef_)/(2)

def E2(Bef_):
    return (g*mb*Bef_)/(2)

# print("E1=",E1(1),"\nE2=",E2(1))

print(e**((1/(k*T))*E2(1))+e**((1/(k*T))*E1(1)))


def Z(T,Bef_):
    return e**(-((1/k*T)*E1(Bef_)))+e**(-((1/k*T)*E2(Bef_)))


def F(T,Bef_): 
    return -k*T*log(Z(T,Bef_))
