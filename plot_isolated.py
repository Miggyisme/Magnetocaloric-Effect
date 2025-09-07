import matplotlib.pyplot as plt

# lambda ao quadrado
x2=[14.7,17.8,21.1,24.3,31.1]
y2=[5154390000.0,7731585000.0,10308780000.0,12885975000.0,18040365000.0]

# 5154390000.0  ... TC = 14.7
# 7731585000.0  ... TC = 17.8
# 10308780000.0 ... TC = 21.1
# 12885975000.0 ... TC = 24.3
# 18040365000.0 ... TC = 31.1

y3=[103087800000000.0,153087800000000.0,206175600000000.0,253087800000000.0,353087800000000.0]
x3=[13.6,16.6,19.9,22.9,29.2]
# 103087800000000.0                 ...           TC = 13.6
# 103087800000000.0 * 1.5 = 153087800000000.0 ... TC = 16.6
# 103087800000000.0 * 2.0 = 206175600000000.0 ... TC = 19.9 aprox 20
# 103087800000000.0 * 2.5 = 253087800000000.0 ... TC = 22.9
# 103087800000000.0 * 3.5 = 353087800000000.0 ... TC = 29.2



plt.scatter(x2,y2,label="lambda2")

# plt.scatter(x3,y3,label="lambda3")


'''
# Definicao de limites do grafico
largura_esquerda = 0
largura_direita = 50
altura_min=0
altura_max=1
plt.xlim(largura_esquerda,largura_direita)
plt.ylim(altura_min,altura_max)
'''

# Legendas e limites
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
# Exibir o gráfico
plt.title("")
plt.grid(True)
plt.legend()
plt.show()
