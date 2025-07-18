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
with open(data, "r", encoding="utf-8") as arquivo:
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

def Bef(m): # Função B efetivo
    Bef_ = B
    for i, labmda in enumerate(lambdas):
        Bef_ = Bef_ + labmda*m**(i+1)
    return Bef_


def M(T, B):
    m = 1.0
    tol=1e-8
    while True:
        Bef_ = Bef(m)
        arg = (g * mb * Bef_) / (2 * k * T)
        m_new = (g * mb / 2) * tanh(arg)
        if abs(m_new - m) < tol:
            return m_new
        m = m_new


M_results=[]
for T in temperaturas:
    # Em cada temperatra da lista

    M_results.append(float(M(T,B)))

   #print(M_results)
   #input()

plt.plot(temperaturas, M_results)
plt.xlabel("Temperatura (K)")
plt.ylabel("Magnetização M(T)")
plt.grid(True)
plt.show()






def TC(T,B,lambdas): # Função TC
    m = M(T,B,lambdas)
    Bef = Bef(m,B,lambdas)
    arg = (g*mb*Bef) / (2*k*T)
    return ((g*mb)**2 / (4*k)) * lambdas[0] * (sech(arg)**2)










# Grandezas


def S(T, B, lambdas): # Entropia
    m = M(T,B,lambdas)
    arg = (g * mb * Bef(m, B, lambdas)) / (2 * k * T)
    return k * (log(2 * cosh(arg)) - arg * tanh(arg))

def C(T, B, lambdas): # Calor Específico
    m = M(T,B,lambdas)
    Bef = Bef(m,B,lambdas)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb*Bef)**2/(4*k*T)) * ((sech(arg))**2)
    return num/(T - TC(T, B, lambdas))

def qui(T, B, lambdas): # Susceptibilidade magnética
    m = M(T,B,lambdas)
    Bef = Bef(m,B,lambdas)
    arg = (g*mb*Bef) / (2*k*T)
    num = ((g*mb)**2/(4*k)) * ((sech(arg))**2)
    return num/(T - TC(T, B, lambdas))



# (DelM/DelT) # Precisa de cuidados porque a derivada não é a mesma.
def Del(T, B):
    m = M(T,B)
    Bef = Bef(m)
    arg = (g*mb*Bef)/(2*k*T)
    num = (((g*mb)**2)*Bef)/(4*k*(T**2)) * ((sech(arg))**2)
    den = 1 - ((((g*mb)**2)/(4*k*T)) * lambdas[0] * ((sech(arg))**2))
    return -(num/den)






# Tratamento de dados e salvar
def fator_escala(f): # Fator de escala. Caso a função não esteja no dicionário, retorna 1 (sem escala)
      escalas = {
        M: 1/mb,
        qui: 1/mb,
        S: R/k,
        C: R/k,
    }
      return escalas.get(f, 1)


def salvar_dados(funcao): # Função salvar os arquivos
    nome_funcao = funcao.__name__
    escala = fator_escala(funcao)

    resultados = []
    for T in temperaturas:
        valor = funcao(T, B, lambdas)
        resultados.append(valor * escala)

    # Da o nome do arquivo
    max_index = len(lambdas)-1 
    nome_arquivo = f"ferro_{nome_funcao}_B{B}_L{max_index}.dat"

    with open(nome_arquivo, "w") as f:
        for T, valor in zip(temperaturas, resultados):
            f.write(f"{T:.3f} {valor:.3e}\n")
salvar_dados(M) #Executar