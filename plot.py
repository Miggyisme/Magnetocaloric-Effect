import os
import matplotlib.pyplot as plt

diretorio = os.path.dirname(__file__)
arquivos = [
#   "10.dat","15.dat","20.dat","25.dat","30.dat",
#   "d10.dat","d15.dat","d20.dat","d25.dat","d30.dat",
#   "14.7.dat","17.8.dat","21.1.dat","24.3.dat","31.1.dat",
#   "13.6a.dat","16.6a.dat","19.9a.dat","22.9a.dat","29.2a.dat",
#   "5.dat","10.dat","15.dat","20.dat","40.dat"
#   "0.01.dat","0.05.dat","0.1.dat","0.15.dat","0.2.dat"
#   "d5.dat","d10.dat","d15.dat","d20.dat","d40.dat"
#   "20.dat","40.dat","50.dat","60.dat"
#   "1.dat","5.dat","10.dat","15.dat",
#   "0.dat","1.dat","3.dat","5.dat","7.dat",
#   "1.dat","2.dat","3.dat","4.dat",#"5.dat"
#   "d0.dat","d1.dat","d3.dat","d5.dat","d7.dat",
   "5.dat","20.dat","15.dat"
#   "0.dat","0.1.dat","0.2.dat"
#   "0a.dat","1a.dat","3a.dat","5a.dat","7a.dat",
#   "E1.dat","E2.dat"



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
teto=0
chao=-0.5
plt.xlim(largura_esquerda,largura_direita)
plt.ylim(chao,teto)
'''

# Legendas e limites
plt.xlabel("Campos (T)")
plt.ylabel("Magnetização")
# Exibir o gráfico
plt.title("Magnetização")
plt.grid(True)
plt.legend()
plt.show()
