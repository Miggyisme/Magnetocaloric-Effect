import os
import numpy as np
import matplotlib.pyplot as plt
from math import cosh
from scipy.optimize import fsolve  # Não vai mais usar, mas deixei para referência

def sech(x):
    return 1 / np.cosh(x)

# Constantes
g = 2             # Fator de Landé
k = 8.61e-5       # Constante de Boltzmann (eV/K)
mb = 5.78e-5      # mu_B (eV/T)
R = 8.31          # Constante universal dos gases

# Leitura dos dados
data = os.path.join(os.path.dirname(__file__), "input.dat")
with open(data, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

s = float(linhas[0].strip().split("=")[1])
B = float(linhas[1].strip().split("=")[1])
lambdas = []
for linha in linhas[2:]:
    valor = float(linha.strip().split("=")[1])
    lambdas.append(valor)

print("Lambdas:", lambdas)

# Função B efetivo
def B_ef(m, B, lambdas):
    Bef = B
    for i, lmbda in enumerate(lambdas):
        Bef += lmbda * m**(i + 1)
    return Bef

# Função que calcula M via iteração manual
def M_iterativo(T, B, lambdas, tol=1e-8, max_iter=1000):
    m = 1.0  # chute inicial
    for _ in range(max_iter):
        Bef = B_ef(m, B, lambdas)
        arg = (g * mb * Bef) / (2 * k * T)
        m_novo = (g * mb / 2) * np.tanh(arg)
        if abs(m_novo - m) < tol:
            return m_novo
        m = m_novo
    print("Atenção: M_iterativo não convergiu para T =", T)
    return m

# Função TC
def TC(T, B, lambdas):
    m = M_iterativo(T, B, lambdas)
    Bef = B_ef(m, B, lambdas)
    arg = (g * mb * Bef) / (2 * k * T)
    return ((g * mb) ** 2 / (4 * k)) * lambdas[0] * (sech(arg) ** 2)

# Entropia
def S(T, B, lambdas):
    m = M_iterativo(T, B, lambdas)
    arg = (g * mb * B_ef(m, B, lambdas)) / (2 * k * T)
    return k * (np.log(2 * np.cosh(arg)) - arg * np.tanh(arg))

# Calor específico
def C(T, B, lambdas):
    m = M_iterativo(T, B, lambdas)
    Bef = B_ef(m, B, lambdas)
    arg = (g * mb * Bef) / (2 * k * T)
    num = ((g * mb * Bef) ** 2 / (4 * k * T)) * (sech(arg) ** 2)
    return num / (T - TC(T, B, lambdas))

# Susceptibilidade magnética
def qui(T, B, lambdas):
    m = M_iterativo(T, B, lambdas)
    Bef = B_ef(m, B, lambdas)
    arg = (g * mb * Bef) / (2 * k * T)
    num = ((g * mb) ** 2 / (4 * k)) * (sech(arg) ** 2)
    return num / (T - TC(T, B, lambdas))

# Lista de temperaturas
start = 0.01
end = 50
step = 0.05
temperaturas = np.arange(start, end + step, step)

# Fator de escala
def fator_escala(f):
    escalas = {
        M_iterativo: 1 / mb,
        qui: 1 / mb,
        S: R / k,
        C: R / k,
    }
    return escalas.get(f, 1)

# Função para salvar dados
def salvar_dados(funcao):
    nome_funcao = funcao.__name__
    escala = fator_escala(funcao)
    resultados = []
    for T in temperaturas:
        valor = funcao(T, B, lambdas)
        resultados.append(valor * escala)
    max_index = len(lambdas) - 1
    nome_arquivo = f"ferro_{nome_funcao}_B{B}_L{max_index}.dat"
    with open(nome_arquivo, "w") as f:
        for T, valor in zip(temperaturas, resultados):
            f.write(f"{T:.3f} {valor:.6e}\n")

# Rodar o cálculo e salvar magnetização
salvar_dados(M_iterativo)
