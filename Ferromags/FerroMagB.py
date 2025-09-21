import os
from numpy import sinh, cosh, tanh, log, arange
import matplotlib.pyplot as plt
def sech(x):
  return 1/cosh(x)

# Constantes
g = 2             # Fator de landé
k = 8.61e-5       # Constalte de Boltzmann (eV/K)
mb = 5.78e-5      # mi bohr (eV/T)
R = 8.31          # Constante universal dos gases
e = 2.71828

# Leitura dos dados: s, B, lista de lambdas
data = os.path.join(os.path.dirname(__file__), "input.dat")
with open(data, "r") as arquivo:
    linhas = arquivo.readlines()

s = float(linhas[0].strip().split("=")[1])
B = float(linhas[1].strip().split("=")[1])
lambdas = []
for linha in linhas[2:]:
    valor = float(linha.strip().split("=")[1])
    lambdas.append(valor)

# Lista de temperaturas
start = 0.01
end = 50
step = 0.05
temperaturas = list(map(float, arange(start, end + step, step)))


# ----- Funções físicas -----
def Bef(m, B):
    Bef_ = B
    for i, lambda_ in enumerate(lambdas):
        Bef_ += lambda_ * m**(i+1)
    return Bef_
Bef_results = []


def E1(Bef_):
    return -(g*mb*Bef_)/(2)
def E2(Bef_):
    return (g*mb*Bef_)/(2)


def Z(T,Bef_): # Função partição
    return e**(-((1/k*T)*E1(Bef_)))+e**(-((1/k*T)*E2(Bef_)))
Z_results=[]

def F(T,Bef_):
    return -k*T*log(Z(T,Bef_))
F_results=[]




def M(T,B):
    m = 1
    tol=1e-8
    while True:
        Bef_ = Bef(m,B)
        arg = (g*mb*Bef_) / (2*k*T)
        m_ = (g*mb/2) * tanh(arg)
        if abs(m_ - m) < tol:
            return m_
        m = m_
M_results=[]

def TC(T,Bef_):
    arg = (g*mb*Bef_) / (2*k*T)
    return ((g*mb)**2 / (4*k)) * lambdas[0] * (sech(arg)**2)
TC_results=[]

def S(T,Bef_):
    arg = (g*mb*Bef_) / (2*k*T)
    return k * (log(2 * cosh(arg)) - arg * tanh(arg))
S_results=[]

def C(T,Bef_):
    arg = (g * mb * Bef_) / (2 * k * T)
    num = ((g * mb * Bef_)**2 / (4 * k * T)) * (sech(arg)**2)
    return num / (T - TC(T, B))
C_results=[]

def qui(T,Bef_):
    arg = (g * mb * Bef_) / (2 * k * T)
    num = ((g * mb)**2 / (4 * k)) * (sech(arg)**2)
    return num / (T - TC(T, B))
qui_results=[]


'''
def Del(T, B):
    m = M(T,B)
    Bef = Bef(m)
    arg = (g*mb*Bef)/(2*k*T)
    num = (((g*mb)**2)*Bef)/(4*k*(T**2)) * ((sech(arg))**2)
    den = 1 - ((((g*mb)**2)/(4*k*T)) * lambdas[0] * ((sech(arg))**2))
    return -(num/den)
'''

# ------ Loop principal ------
for T in temperaturas:
    M_ = M(T,B)
    Bef_ = Bef(M_,B)

    # Em cada temperatra da lista
    M_results.append((1/mb) * M_)
    S_results.append((R/k) * S(T,Bef_))
    C_results.append((R/k) * C(T,Bef_))
    qui_results.append((1/mb) * qui(T,Bef_))
    TC_results.append(TC(T,Bef_))
    F_results.append(F(T, Bef_))
    Z_results.append(Z(T, Bef_))
    Bef_results.append(Bef_)


# Salvar e plotar gráfico
def salvar(temperaturas, resultados):
    with open("output.dat", "w") as f:
        for T, res in zip(temperaturas, resultados):
            f.write(f"{T:.6f}\t{res:.6e}\n")
salvar(temperaturas, Bef_results)

plt.scatter(temperaturas, Bef_results)
plt.xlabel("Temperatura (K)")
plt.ylabel("Magnetização M(T)")
plt.grid(True)
plt.show()

