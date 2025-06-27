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

# Input de temperatura (T) constante fixo.
T = float(input("Insira um valor para a temperatura "))

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
paraMagT = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagT\\paraMT{T}.dat"
paraEntT = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagT\\paraEntT{T}.dat"
paraCapT = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagT\\paraCapT{T}.dat"
paraSusT = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagT\\paraSusT{T}.dat"
paraDelT = f"C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ParamagT\\paraDelT{T}.dat"

# Lista de campos
start = 0
end = 50
step = 0.001
campos = np.arange(start,end,step).tolist()

# Abrindo todos os arquivos de saída
with open(paraMagT, "w") as file_paraMagT, \
     open(paraEntT, "w") as file_paraEntT, \
     open(paraCapT, "w") as file_paraCapT, \
     open(paraSusT, "w") as file_paraSusT, \
     open(paraDelT, "w") as file_paraDelT:
    B = start
    while B<end: # while pra calcular e imprimir todos os pontos e formar todas as coordenadas
        
        # Calcular os valores para cada B
        m_valor = m(T, B)
        S_valor = S(T, B)
        C_valor = C(T, B)
        qui_valor = qui(T, B)
        Del_valor = Del(T, B)
        # Escrever os resultados nos arquivos respectivos
        file_paraMagT.write(f"{B} {m_valor:.3e}\n")
        file_paraEntT.write(f"{B} {S_valor:.3e}\n")
        file_paraCapT.write(f"{B} {C_valor:.3e}\n")
        file_paraSusT.write(f"{B} {qui_valor:.3e}\n")
        file_paraDelT.write(f"{B} {Del_valor:.3e}\n")
        # Incrementar com o passo
        B = B + step