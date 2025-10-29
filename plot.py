import os
import matplotlib.pyplot as plt

diretorio = os.path.dirname(__file__)
arquivos = [
#    "257719.5.dat","386579.25.dat","515439.0.dat","644298.75.dat","773158.5.dat",
#    "10.dat","15.dat","20.dat","25.dat","30.dat",
#     "14.7.dat","17.8.dat","21.1.dat","24.3.dat","31.1.dat",
     "13.6.dat","16.6.dat","19.9.dat","22.9.dat","29.2.dat",
#    "5.dat","10.dat","15.dat","20.dat"
#    "20.dat","40.dat","50.dat","60.dat"
#     "1.dat","5.dat","10.dat","15.dat"


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
altura_max=1
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
