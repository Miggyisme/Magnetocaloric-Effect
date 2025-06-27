import matplotlib.pyplot as plt

# Definindo arquivos
arquivos = [
    "C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ferromagB\\ferroMB5.0.dat",
    "C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ferromagB\\paraMB5.0.dat",
#    "C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ferromagB\\paraMB6.0.dat",
#    "C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ferromagB\\paraMB8.0.dat",
#    "C:\\Users\\Miguel\\ic\\Programas\\Arquivos saída ferromagB\\paraMB10.0.dat",
]
# Plotando os dados em cada arquivo
for arquivo in arquivos:
    x = []
    y = []

    with open(arquivo, "r") as file:
        for linha in file:
            ponto = linha.strip().split()
            x.append(float(ponto[0]))
            y.append(float(ponto[1]))
    legenda = arquivo.split("\\")[-1]       # Faz a legenda
    plt.scatter(x,y, label=legenda)         # Montar o gráfico

# Definicao de limites do grafico
largura_esquerda=-1
largura_direita=50
altura_min=0
altura_max=1.1

# Legendas e limites
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.xlim(largura_esquerda,largura_direita)
plt.ylim(altura_min,altura_max)

# Exibir o gráfico
plt.title("")
plt.grid(True)
plt.legend()
plt.show()
