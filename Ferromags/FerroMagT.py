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
T = float(linhas[2].strip().split("=")[1])
lambdas = []
for linha in linhas[3:]:
    valor = float(linha.strip().split("=")[1])
    lambdas.append(valor)

# Lista de campos
start = -50
end = 50
step = 0.05
campos = list(map(float, arange(start, end + step, step)))


# ----- Funções físicas -----
def Bef(m, B):
    Bef_ = B
    for i, lambda_ in enumerate(lambdas):
        Bef_ += lambda_ * m**(i+1)
    return Bef_
Bef_results = []


def E1(Bef_):
    return -(g*mb*Bef_)/(2)
E1_results = []

def E2(Bef_):
    return (g*mb*Bef_)/(2)
E2_results = []


def Z(T,Bef_): # Função partição
    return e**(-((1/k*T)*E1(Bef_)))+e**(-((1/k*T)*E2(Bef_)))
Z_results=[]

def F(T,Bef_):
    return -k*T*log(Z(T,Bef_))
F_results=[]




def M(T,B):
    m = -0.5
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
    return ((g*mb)**2 / (4*k)) * (lambdas[0]+3*lambdas[2]*M(T,B)) * (sech(arg)**2)
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

def Del(T, Bef_):
    arg = (g*mb*Bef_)/(2*k*T)
    num = (((g*mb)**2)*Bef_)/(4*k*(T**2)) * ((sech(arg))**2)
    den = 1 - ((((g*mb)**2)/(4*k*T)) * lambdas[0] * ((sech(arg))**2))
    return -(num/den)
Del_results=[]

# ------ Loop principal ------
for B in campos:
    M_ = M(T,B)
    Bef_ = Bef(M_,B)

    # Em cada campo da lista
    M_results.append((1/mb) * M_)
    Del_results.append((1/mb) * Del(T,Bef_))
    S_results.append((R/k) * S(T,Bef_))
    C_results.append((R/k) * C(T,Bef_))
    qui_results.append((1/mb) * qui(T,Bef_))
    TC_results.append(TC(T,Bef_))
    F_results.append(F(T, Bef_))
    Z_results.append(Z(T, Bef_))
    Bef_results.append(Bef_)
    E1_results.append(E1(Bef_))
    E2_results.append(E2(Bef_))


# Salvar e plotar gráfico
def salvar(campos, resultados):
    with open("output.dat", "w") as f:
        for T, res in zip(campos, resultados):
            f.write(f"{T:.6f}\t{res:.6e}\n")
salvar(campos, M_results)


plt.scatter(campos, M_results)
plt.xlabel("Campos (T)")
plt.ylabel("Magnetização M(T)")
plt.grid(True)
plt.show()

