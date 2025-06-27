import numpy as np
import matplotlib.pyplot as plt
from math import cosh, log
from scipy.optimize import fsolve
def sech(x):
  return 1/np.cosh(x)

# 773158.5  ... TC = 30
# 644298.75 ... TC = 25
# 515439.0  ... TC = 20
# 386579.25 ... TC = 15
# 257719.5  ... TC = 10

# Constantes
g = 2             # Fator de landé
k = 8.61e-5       # Constalte de Boltzmann (eV/K)
mb = 5.78e-5      # mi bohr (eV/T)
R = 8.31          # Constante universal dos gases


# comando que vai ler o arquivo de input
lambda0 = 10
lambda1 = 20
lambda2 = 30


# Pre-requisitos

# Função B efetivo
lambdas = [lambda0, lambda1, lambda2]
def B_ef(m, B, lambdas):
    Bef = B
    for i, lmbda in enumerate(lambdas):
        Bef = Bef + lmbda*m**(i+1)
    return Bef

# Função TC
def TC(T,B,lambdas):
    m = M(T,B,lambdas)
    Bef = B_ef(m,B,lambdas)
    arg = (g*mb*Bef) / (2*k*T)
    return ((g*mb)**2 / (4*k)) * lambda0 * (sech(arg)**2)


# Lista de temperaturas
start = 0.01
end = 50
step = 0.05
temperaturas = np.arange(start, end + step, step)







# Magnetização
def M(T, B, lambdas):
    def f(m_):
        Bef = B_ef(m_,B,lambdas)
        arg = (g*mb*Bef) / (2*k*T)
        return (g*mb/2) * np.tanh(arg) - m_
    m0 = 1
    sol = fsolve(f, m0)
    return sol[0]

# Entropia
def S(T, B, lambdas):
    m = M(T,B,lambdas)
    arg = (g * mb * B_ef(m, B, lambdas)) / (2 * k * T)
    return k * (np.log(2 * np.cosh(arg)) - arg * np.tanh(arg))

# Calor Específico
def C(T, B, lambdas):
    m = M(T,B,lambdas)
    Bef = B_ef(m,B,lambdas)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb*Bef)**2/(4*k*T)) * ((sech(arg))**2)
    return num/(T - TC(T, B, lambdas))

# Qui
def qui(T, B, lambdas):
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







# Fator de escala. Caso a função não esteja no dicionário, retorna 1 (sem escala)
def fator_escala(f):
      escalas = {
        M: 1/mb,
        qui: 1/mb,
        S: R/k,
        C: R/k,
    }
      return escalas.get(f, 1)

# Função salvar os arquivos
def salvar_dados(funcao, B, lambdas):
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

# Plotar varios gráficos ao mesmo tempo
def plot(funcoes, Bs, lista_de_lambdas):
    for funcao in funcoes:
        for B in Bs:
            for lambdas in lista_de_lambdas:
                escala = fator_escala(funcao)
                resultados = []
                for T in temperaturas:
                    valor = funcao(T, B, lambdas)
                    resultados.append(valor * escala)

                label_lambdas = f"L{len(lambdas)-1}"
                plt.scatter(temperaturas, resultados,
                            label=f"{funcao.__name__}, B={B}, {label_lambdas}")

    plt.xlabel("Temperatura (K)")
    plt.ylabel("Grandeza")
    plt.title("Plot")
    plt.grid(True)
    plt.legend(fontsize='small')
    plt.tight_layout()
    plt.show()

# plot([nome],[campo],[lambda])
# salvar_dados(nome,campo,lambda)

# plot([qui], [0], [773158.5,644298.75,515439.0,386579.25,257719.5])
# salvar_dados(M, 0, 773158.5)
# plot([TC],[0],[773158.5,644298.75,515439.0,386579.25,257719.5])



plot([M],[15],[515439.0])

salvar_dados(M,15,515439.0)

