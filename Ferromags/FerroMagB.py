import os
import numpy as np
import matplotlib.pyplot as plt
from math import cosh, log
from scipy.optimize import fsolve
def sech(x):
  return 1/np.cosh(x)


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



# Pre-requisitos
def B_ef(m, B, lambdas): # Função B efetivo
    Bef = B
    for i, lmbda in enumerate(lambdas):
        Bef = Bef + lmbda*m**(i+1)
    return Bef

def TC(T,B,lambdas): # Função TC
    m = M(T,B,lambdas)
    Bef = B_ef(m,B,lambdas)
    arg = (g*mb*Bef) / (2*k*T)
    return ((g*mb)**2 / (4*k)) * lambdas[0] * (sech(arg)**2)


# Lista de temperaturas
start = 0.01
end = 50
step = 0.05
temperaturas = np.arange(start, end + step, step)





# Grandezas
def M(T, B, lambdas): # Magnetização
    def f(m_):
        Bef = B_ef(m_,B,lambdas)
        arg = (g*mb*Bef) / (2*k*T)
        return (g*mb/2) * np.tanh(arg) - m_
    m0 = 1
    sol = fsolve(f, m0)
    return sol[0]

def S(T, B, lambdas): # Entropia
    m = M(T,B,lambdas)
    arg = (g * mb * B_ef(m, B, lambdas)) / (2 * k * T)
    return k * (np.log(2 * np.cosh(arg)) - arg * np.tanh(arg))

def C(T, B, lambdas): # Calor Específico
    m = M(T,B,lambdas)
    Bef = B_ef(m,B,lambdas)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb*Bef)**2/(4*k*T)) * ((sech(arg))**2)
    return num/(T - TC(T, B, lambdas))

def qui(T, B, lambdas): # Susceptibilidade magnética
    m = M(T,B,lambdas)
    Bef = B_ef(m,B,lambdas)
    arg = (g*mb*Bef) / (2*k*T)
    num = ((g*mb)**2/(4*k)) * ((sech(arg))**2)
    return num/(T - TC(T, B, lambdas))


'''
# (DelM/DelT) # Precisa de cuidados porque a derivada não é a mesma.
def Del(T, B):
    m = M(T,B)
    Bef = B_ef(m,B)
    arg = (g*mb*Bef)/(2*k*T)
    num = (((g*mb)**2)*Bef)/(4*k*(T**2)) * ((sech(arg))**2)
    den = 1 - ((((g*mb)**2)/(4*k*T)) * lambda0 * ((sech(arg))**2))
    return -(num/den)
'''





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

salvar_dados(S) #Executar

