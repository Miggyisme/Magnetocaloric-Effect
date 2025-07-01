import os
import matplotlib.pyplot as plt

diretorio = os.path.dirname(__file__)
arquivos = [
    "ferro_S_B0.0_L2.dat",
    "ferro_S_B1.0_L2.dat",
    "ferro_S_B3.0_L2.dat",
    "ferro_S_B5.0_L2.dat",
    "ferro_S_B7.0_L2.dat"
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



# Definicao de limites do grafico
largura_esquerda = 0
largura_direita = 50
altura_min=0
altura_max=6
plt.xlim(largura_esquerda,largura_direita)
plt.ylim(altura_min,altura_max)


# Legendas e limites
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
# Exibir o gráfico
plt.title("")
plt.grid(True)
plt.legend()
plt.show()
