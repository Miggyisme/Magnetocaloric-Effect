import numpy as np
import matplotlib.pyplot as plt
from math import cosh, log
from scipy.optimize import fsolve
def sech(x):
  return 1/np.cosh(x)

# Constantes
g = 2
k = 8.61e-5       # Constalte de Boltzmann (eV/K)
mb = 5.78e-5      # mi bohr (eV/T)
R = 8.31          # Constante universal dos gases

# Funções para descobrir lambda e TC
def TC_const(lambda0):
    return ((g**2)*(mb**2)*lambda0)/(4*k)
def lambda_const(TC):
    return (4 * k * TC) / (g**2 * mb**2)

# Lista de campos
start = 0
end = 50
# end = 10 teste
step = 0.05
campos = np.arange(start, end + step, step)


# 773158.5  ... TC = 30
# 644298.75 ... TC = 25
# 515439.0  ... TC = 20
# 386579.25 ... TC = 15
# 257719.5  ... TC = 10



# Possivelmente seja mais seguro de deixar como variavel as funcoes como funcao de (T,B,lambda_)
# Magnetização
def M(T, B):
    def f(m_):
        Bef = B + lambda0 * m_
        arg = (g*mb*Bef) / (2*k*T)
        return (g*mb/2) * np.tanh(arg) - m_
    m0 = 1
    sol = fsolve(f, m0)
    return sol[0]

# TC
def TC(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb)**2/(4*k)) * ((sech(arg))**2)
    TC = ((g*mb)**2/(4*k)) * lambda0 * ((sech(arg))**2)
    return TC

# Entropia
def S(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g * mb * Bef) / (2 * k * T)
    return k * (np.log(2 * np.cosh(arg)) - arg * np.tanh(arg))

# Calor Específico
def C(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb*Bef)**2/(4*k*T)) * ((sech(arg))**2)
    return num/(T - TC(T, B))

# Qui
def qui(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb)**2/(4*k)) * ((sech(arg))**2)
    return num/(T - TC(T, B))

# Qui^-1 Geral
def inv_quiG(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb)**2/(4*k)) * ((sech(arg))**2)
    return (T - TC(T, B))/num

# Qui^-1 Particular
def inv_quiP(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g*mb*Bef)/(2*k*T)
    num = ((g*mb)**2/(4*k)) * ((sech(arg))**2)
    return (T - TC_const(lambda0))/num


# (DelM/DelT)
def Del(T, B):
    Bef = B + lambda0 * M(T, B)
    arg = (g*mb*Bef)/(2*k*T)
    num = (((g*mb)**2)*Bef)/(4*k*(T**2)) * ((sech(arg))**2)
    den = 1 - ((((g*mb)**2)/(4*k*T)) * lambda0 * ((sech(arg))**2))
    return -(num/den)









# Fator de escala
def fator_escala(f):
      escalas = {
        M: 1/mb,
        qui: 1/mb,
        Del: 1/mb,
        S: R/k,
        C: R/k,
        inv_quiP: 1/mb,
    }
      return escalas.get(f, 1)  # Caso a função não esteja no dicionário, retorna 1 (sem escala)

# Função salvar os arquivos
def salvar_dados(funcao, T, lambda_):
    global lambda0
    lambda0 = lambda_

    nome_funcao = funcao.__name__  # Ex: nome_funcao = "M" (vai receber o que for posto de argumento)
    escala = fator_escala(funcao) # Pega a escala certa da função selecionada.

    # Cria uma lista com os valores calculados
    resultados = []
    for B in campos:
        valor = funcao(T, B)
        resultados.append(valor * escala)

    # Salva os dados em duas colunas: A primeira sendo os campos é a lista "resultados"
    nome_arquivo = f"ferro_{nome_funcao}_T{T}_L{lambda_}.dat"
    with open(nome_arquivo, "w") as f:
        for B, valor in zip(campos, resultados):
            f.write(f"{B:.3f} {valor:.3e}\n")

# Plotar varios gráficos ao mesmo tempo
def plot(funcoes, temperaturas, lambdas):
    for funcao in funcoes:
        for T in temperaturas:  # agora T é fixo (pode ser só [10], por exemplo)
            for lambda_ in lambdas:
                global lambda0
                lambda0 = lambda_
                escala = fator_escala(funcao)

                resultados = []
                for B in campos:
                    valor = funcao(T, B)
                    resultados.append(valor * escala)

                plt.scatter(campos, resultados,
                         label=f"{funcao.__name__}, T={T} K, λ={lambda_:.2f}")

    plt.xlabel("Campo Magnético B (T)")
    plt.ylabel("Grandeza (escalada)")
    plt.title("Dependência com o Campo (T fixo)")
    plt.grid(True)
    plt.legend(fontsize='small')
    plt.tight_layout()
    plt.show()

# plot([nome],[temperatura],[lambda])
# salvar_dados(nome,temperatura,lambda)