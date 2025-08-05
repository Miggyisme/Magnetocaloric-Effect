import os
from numpy import sinh, cosh, tanh, log, arange
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def sech(x):
  return 1/cosh(x)

# Constantes
g = 2             # Fator de landé
k = 8.61e-5       # Constalte de Boltzmann (eV/K)
mb = 5.78e-5      # mi bohr (eV/T)
R = 8.31          # Constante universal dos gases

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

def Bef(m,B): # Função B efetivo
    Bef_ = B
    for i, labmda in enumerate(lambdas):
        Bef_ = Bef_ + labmda*m**(i+1)
    return Bef_

def M(T, B):
    m = 1
    tol=1e-8
    while True:
        Bef_ = Bef(m,B)
        arg = (g*mb*Bef_) / (2*k*T)
        m_ = (g*mb/2) * tanh(arg)
        if abs(m_ - m) < tol:
            return m_
        m = m_
        print(Bef_)
        #print(m)
        input()
M_results=[]

# Esse lambda nao parece estar certo
# Bef quase não muda


def TC(T, B):
    m = M(T, B)
    Bef_ = Bef(m,B)
    arg = (g * mb * Bef_) / (2 * k * T)
    return ((g * mb)**2 / (4 * k)) * lambdas[0] * (sech(arg)**2)
TC_results=[]

def S(T, B):
    m = M(T, B)
    Bef_ = Bef(m, B)
    arg = (g * mb * Bef_) / (2 * k * T)
    return k * (log(2 * cosh(arg)) - arg * tanh(arg))
S_results=[]

def C(T, B):
    m = M(T, B)
    Bef_ = Bef(m,B)
    arg = (g * mb * Bef_) / (2 * k * T)
    num = ((g * mb * Bef_)**2 / (4 * k * T)) * (sech(arg)**2)
    return num / (T - TC(T, B))
C_results=[]

def qui(T, B):
    m = M(T, B)
    Bef_ = Bef(m,B)
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
    

def escala(f): # Fator de escala. Caso a função não esteja no dicionário, retorna 1 (sem escala)
      escalas = {
        M: 1/mb,
        qui: 1/mb,
        S: R/k,
        C: R/k,
    }
      return escalas.get(f, 1)


# Loop principal
for T in temperaturas:
    # Em cada temperatra da lista

    M_results.append(float(M(T,B)))
    S_results.append(float(S(T,B)))
    C_results.append(float(C(T,B)))
    qui_results.append(float(qui(T,B)))


# Salvar e plotar gráfico
plt.scatter(temperaturas, M_results)
plt.xlabel("Temperatura (K)")
plt.ylabel("Magnetização M(T)")
plt.grid(True)
plt.show()

def salvar(temperaturas, resultados):
    with open("dados.dat", "w") as f:
        for T, res in zip(temperaturas, resultados):
            f.write(f"{T:.6f}\t{res:.6e}\n")
salvar(temperaturas, M_results)


