import os
import matplotlib.pyplot as plt

diretorio = os.path.dirname(__file__)
arquivos = [
    "dados0.dat",
#    "dados1.dat",
    "dados2.dat",
#    "dados3.dat",
#    "dados4.dat",
]


for arquivo in arquivos:
    endereco = os.path.join(diretorio, arquivo)
    x = []
    y = []

    with open(endereco, "r") as file:
        for linha in file:
            ponto = linha.strip().split()
            x.append(float(ponto[0]))
            y.append(float(ponto[1]))
    
    legenda = arquivo
    plt.scatter(x,y, label=legenda) 


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
