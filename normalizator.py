import os
import matplotlib.pyplot as plt
arquivo = "29.2.dat" 
diretorio = os.path.dirname(__file__)
endereco = os.path.join(diretorio, arquivo)

x = []
y = []

# Leitura do arquivo
with open(endereco, "r") as file:
    for linha in file:
        if not linha.strip():  # ignora linhas vazias
            continue
        ponto = linha.strip().split()
        x.append(float(ponto[0]))
        y.append(float(ponto[1]))


# Normalizando
TC = 29.2
x_normal=[]
for i in x:
    x_normal.append(i/TC)



# salvar e plotar
def salvar(campos, resultados):
    with open("normal.output.dat", "w") as f:
        for T, res in zip(campos, resultados):
            f.write(f"{T:.6f}\t{res:.6e}\n")
salvar(x_normal, y)
plt.scatter(x_normal, y, label=arquivo)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
