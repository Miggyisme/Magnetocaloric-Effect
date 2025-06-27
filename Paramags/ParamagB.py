# Definindo operacoes
from math import *
import numpy as np
def sech(x):        # Secante hiperbolico
    return 1/cosh(x)

# Definindo as constantes
g = 2
k = 1.38*10**-23    # Constante de Boltzmann (J/K)
mb = 9.27*10**-24   # mi bohr
m1 = g*mb/2
m2 = -g*mb/2
R = 8.31

# Input de campo (B) constante fixo.
B = float(input("Insira um valor para o campo "))

# Definindo funções
def m(T,B):
    return (1/mb)*(g*mb/2)*tanh((g*mb*B)/(2*k*T)) # Magnetizaçao/mb
def S(T,B):
#    return k*(log(2*cosh((g*mb*B)/(2*k*T)))-((g*mb*B)/(2*k*T))*tanh((g*mb*B)/(2*k*T)))/k           # Versão antiga Entropia/k
     return R*(log(2*cosh((g*mb*B)/(2*k*T)))-((g*mb*B)/(2*k*T))*tanh((g*mb*B)/(2*k*T))) # Entropia/n
def C(T,B):
#    return (((g*mb*B/2)**2)/(k*T**2))*(sech((g*mb*B)/(2*k*T)))**2                                  # Versão antiga Capacidade térmica
     return (R/k)*(((g*mb*B/2)**2)/(k*T**2))*(sech((g*mb*B)/(2*k*T)))**2 # Capacidade térmica/n
def qui(T,B):
    return (1/mb)*(1/(k*T))*((g*mb/2)*sech(((g*mb*B)/(2*k*T))))**2 # Qui/mb
def Del(T,B):
    return (1/mb)*-(B/(4*k))*((g*mb/T)*sech((g*mb*B)/(2*k*T)))**2 # (DelM/DelT)/mb

# Arquivos de saída
paraMagB = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagB\\paraMB{B}.dat"
paraEntB = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagB\\paraEntB{B}.dat"
paraCapB = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagB\\paraCapB{B}.dat"
paraSusB = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagB\\paraSusB{B}.dat"
paraDelB = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagB\\paraDelB{B}.dat"

# Lista de temperaturas
start = 0.01 #Não pode ser 0
end = 50
step = 0.05
temperaturas = np.arange(start,end,step).tolist()

# Abrindo todos os arquivos de saída
with open(paraMagB, "w") as file_paraMagB, \
     open(paraEntB, "w") as file_paraEntB, \
     open(paraCapB, "w") as file_paraCapB, \
     open(paraSusB, "w") as file_paraSusB, \
     open(paraDelB, "w") as file_paraDelB:
    T = start
    while T<end: # while pra calcular e imprimir todos os pontos e formar todas as coordenadas
        
        # Calcular os valores para cada B
        m_valor = m(T, B)
        S_valor = S(T, B)
        C_valor = C(T, B)
        qui_valor = qui(T, B)
        Del_valor = Del(T, B)
        # Escrever os resultados nos arquivos respectivos
        file_paraMagB.write(f"{T} {m_valor:.3e}\n")
        file_paraEntB.write(f"{T} {S_valor:.3e}\n")
        file_paraCapB.write(f"{T} {C_valor:.3e}\n")
        file_paraSusB.write(f"{T} {qui_valor:.3e}\n")
        file_paraDelB.write(f"{T} {Del_valor:.3e}\n")
        # Incrementar com o passo
        T = T + step