import os
import matplotlib.pyplot as plt

diretorio = os.path.dirname(__file__)
arquivos = [
#   "257719.5.dat","386579.25.dat","515439.0.dat","644298.75.dat","773158.5.dat",
   "10.dat","15.dat","20.dat","25.dat","30.dat",
#   "10a.dat","15a.dat","20a.dat","25a.dat","30a.dat",
#   "14.7.dat","17.8.dat","21.1.dat","24.3.dat","31.1.dat",
#   "13.6a.dat","16.6a.dat","19.9a.dat","22.9a.dat","29.2a.dat",
#   "5.dat","10.dat","15.dat","20.dat"
#   "20.dat","40.dat","50.dat","60.dat"
#   "1.dat","5.dat","10.dat","15.dat",
#   "0.dat","1.dat","3.dat","5.dat","7.dat",
#   "output.dat",
#   "0a.dat","1a.dat","3a.dat","5a.dat","7a.dat",



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
teto=100
chao=0
plt.xlim(largura_esquerda,largura_direita)
plt.ylim(chao,teto)
'''

# Legendas e limites
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
# Exibir o gráfico
plt.title("")
plt.grid(True)
plt.legend()
plt.show()
