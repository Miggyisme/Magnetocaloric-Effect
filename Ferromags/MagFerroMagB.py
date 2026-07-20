import os
from numpy import cosh, tanh, log, exp
import matplotlib.pyplot as plt

def sech(x):
    return 1/cosh(x)

# Constantes
g = 2             # Fator de Landé
k = 8.617e-5      # Constante de Boltzmann (eV/K)
mb = 5.78838e-5   # Magnéton de Bohr (eV/T)
R = 8.31          # Constante universal dos gases
e = 2.71828

# Extração dos parametros no arquivo input.dat
data = os.path.join(os.path.dirname(__file__), "input.dat") if '__file__' in locals() else "input.dat"

with open(data, "r") as arquivo:
    linhas = arquivo.readlines()

s = float(linhas[0].strip().split("=")[1])
B = float(linhas[1].strip().split("=")[1])
lambdas = []
for linha in linhas[3:]:
    valor = float(linha.strip().split("=")[1])
    lambdas.append(valor)


# Controle da temperatura
T_inicial = 0.01
T_final = 50
N = 5000
dT = (T_final - T_inicial) / N
temperaturas = [T_inicial + i * dT for i in range(N + 1)]





# Chute inicial e nome do arquivo
chute_adimensional = 1.0
nome_saida = "output.dat"




# Funções físicas
def Bef(m_adim, B):
    Bef_ = B
    for i, lambda_ in enumerate(lambdas):
        Bef_ += (lambda_ * mb**(i+1)) * (m_adim ** (i+1))
    return Bef_

def E1(Bef_):
    return -(g*mb*Bef_)/(2)
E1_results = []

def E2(Bef_):
    return (g*mb*Bef_)/(2)
E2_results = []

def Z(T, Bef_):
    return exp(-(E1(Bef_)/(k*T))) + exp(-(E2(Bef_)/(k*T)))

def F(T, Bef_):
    a = -E1(Bef_) / (k*T)
    b = -E2(Bef_) / (k*T)
    maior = a if a > b else b
    return -k*T*(maior + log(exp(a - maior) + exp(b - maior)))
F_results = []

def M_autoconsistente(T, B, chute_adim):
    tol = 1e-5      
    max_iter = 100000
    m_adim = chute_adim

    if abs(m_adim) < 1e-10 and B == 0:
        m_adim = 1e-7

    for _ in range(max_iter):
        Bef_ = Bef(m_adim, B)

        arg = (g * mb * Bef_) / (2 * k * T)

        # Evita overflow numérico em temperaturas extremamente baixas
        if arg > 50:
            m_nova_adim = 1.0
        elif arg < -50:
            m_nova_adim = -1.0
        else:
            m_nova_adim = tanh(arg)

        # Critério de parada
        if abs(m_nova_adim - m_adim) < tol:
            return m_nova_adim

        # Iteração direta, sem amortecimento (igual ao goto do Fortran)
        m_adim = m_nova_adim

    return m_adim
M_results = []

def dBef_dm(m_adim):
    derivada = 0.0
    for i, lambda_ in enumerate(lambdas):
        derivada += (lambda_ * mb**(i+1)) * (i + 1) * (m_adim ** i)
    return derivada


def TC(T, B, m_adim):
    arg = (g * mb * Bef(m_adim, B)) / (2 * k * T)
    sech2 = 0.0 if abs(arg) > 50 else sech(arg) ** 2
    return (g * mb / (2 * k)) * dBef_dm(m_adim) * sech2
TC_results = []

def dM_dT(T, B, m_adim):
    arg = (g * mb * Bef(m_adim, B)) / (2 * k * T)
    sech2 = 0.0 if abs(arg) > 50 else sech(arg) ** 2
    num = (g * mb * Bef(m_adim, B) / (2 * k * T**2)) * sech2
    den = 1 - (g * mb * dBef_dm(m_adim) / (2 * k * T)) * sech2
    return -(num / den)
dM_dT_results = []

def dM_dB(T, B, m_adim):
    deltaB = 1e-5
    m_perturbado = M_autoconsistente(T, B + deltaB, m_adim)
    return (m_perturbado - m_adim) / deltaB
dM_dB_results = []


# ------ Loop principal ------
chute = chute_adimensional
for T in temperaturas:
    m_atual = M_autoconsistente(T, B, chute)
    Bef_ = Bef(m_atual, B)
    M_results.append(m_atual)
    dM_dT_results.append(dM_dT(T, B, m_atual))
    dM_dB_results.append(dM_dB(T, B, m_atual))
    E1_results.append(E1(Bef_))
    E2_results.append(E2(Bef_))
    F_results.append(F(T, Bef_))
    TC_results.append(TC(T, B, m_atual))
    chute = m_atual  # Efeito memória

# Salvar e plotar gráfico
def salvar(nome_arquivo, temperaturas, resultados):
    with open(nome_arquivo, "w") as f:
        for T, res in zip(temperaturas, resultados):
            f.write(f"{T:.6f}\t{res:.6e}\n")
salvar(nome_saida, temperaturas, M_results)

plt.scatter(temperaturas, M_results)
plt.xlabel("Temperatura (K)")
plt.ylabel("Magnetização")
plt.grid(True)
plt.show()
