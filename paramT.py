# Usando uma biblioteca nativa do python
from math import *

# Definindo as constantes
g = 2
k = 1.38*10**-23    # Constante de Boltzmann (J/K)
mb = 9.27*10**-24   # mi bohr
m1 = g*mb/2
m2 = -g*mb/2

# Entrando com um valor B fixo
B=10

# Definindo a magnetização paramagnética
def m(T,B):
    if T==0:
        return g*mb/2
        # Valor máximo da magnetizacao. Para evitar divisão por 0.   
    else:
        return (g*mb/2)*tanh((g*mb*B)/(2*k*T))
        # Valor da magnetizacao para T>0

# Define o arquivo .dat de saída
paramT = "C:\\Users\\Miguel\\Desktop\\paramT.dat"

# Gera uma sequencia de 0 a 50 (51 valores) e armazena na variavel 'temperaturas'
temperaturas = range(51) 

# Abrindo o arquivo para escrita
with open(paramT, "w") as file:

    # Um loop para calcular a magnetizacao para cada temperatura. 
    # "Para cada valor de T na sequencia temperaturas, calcule seu m_valor especifico."
    for T in temperaturas:
        m_valor=m(T,B)

        # Escrevendo um valor de T e seu valor de m respectivo.
        file.write(f"{T} {m_valor:.3e}\n")
        # 'f' na frente indica uma f-string. Em python é uma forma de escrever uma string e embutir expressões dentro dela sem formatações complexas.
        # 'm_valor:.3e' ira formatar o m_valor em notacao cientifica com 3 casas decimais.
        # '\n' ira pular uma linha