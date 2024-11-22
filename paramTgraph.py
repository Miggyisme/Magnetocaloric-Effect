import matplotlib.pyplot as plt
from math import *

# Definindo as constantes
g = 2
k = 1.38*10**-23
mb = 9.27*10**-24
m1 = g*mb/2
m2 = -g*mb/2

# Entrando com um valor B fixo
B=100

# Definindo a magnetização paramagnética
def m(T,B):
    if T==0:
        return g*mb/2
    else:
        return (g*mb/2)*tanh(g*mb*B/2*k*T)

# Gera uma sequencia de 0 a 50 (51 valores) e armazena na variavel 'temperaturas'
temperaturas = range(51) 

# Calcula os valores de m para cada T e insere eles dentro da lista 'm_valores'
m_valores = [m(T,B) for T in temperaturas]

# Criando o grafico em python
plt.plot(temperaturas,m_valores)

# Títulos e rótulos
plt.title("Magnetização paramagnética")
plt.xlabel("Temperatura")
plt.ylabel("Magnetização")
plt.grid(True)

# Mostrar o gráfico
plt.show()