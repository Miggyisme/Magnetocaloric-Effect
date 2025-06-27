# Plotar um único gráfico isolado (funcao original)
def plot(funcao, B, lambda_):
    global lambda0
    lambda0 = lambda_

    escala = fator_escala(funcao)
    resultados = []

    for T in temperaturas:
        valor = funcao(T, B)
        resultados.append(valor * escala)

    plt.scatter(temperaturas, resultados, label=f"{funcao.__name__} (B={B}, λ={lambda_})")
    plt.xlabel("Temperatura (K)")
    plt.ylabel(f"{funcao.__name__}")
    plt.title(f"{funcao.__name__}")
    plt.grid(True)
    plt.legend()
    plt.show()



# Funções de plot e salvar_dados com input

def salvar_dados(funcao, lambda_):
    global lambda0
    lambda0 = lambda_
    T = float(input("Digite a temperatura: "))

    nome_funcao = funcao.__name__
    escala = fator_escala(funcao)

    resultados = []
    for B in campos:
        valor = funcao(T, B)
        resultados.append(valor * escala)

    nome_arquivo = f"ferro_{nome_funcao}_T{T}_L{lambda_}.dat"
    with open(nome_arquivo, "w") as f:
        for B, valor in zip(campos, resultados):
            f.write(f"{B:.3f} {valor:.3e}\n")

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

def plot(funcoes, lambdas):
    T = float(input("Digite a temperatura: "))
    for funcao in funcoes:
        for lambda_ in lambdas:
            global lambda0
            lambda0 = lambda_
            escala = fator_escala(funcao)

            resultados = []
            for B in campos:
                valor = funcao(T, B)
                resultados.append(valor * escala)

            plt.plot(campos, resultados,
                     label=f"{funcao.__name__}, T={T} K, λ={lambda_:.2f}")

    plt.xlabel("Campo Magnético B (T)")
    plt.ylabel("Grandeza (escalada)")
    plt.title("Dependência com o Campo (T fixo)")
    plt.grid(True)
    plt.legend(fontsize='small')
    plt.tight_layout()
    plt.show()


# salvar_dados(nome,lambda)
# plot([nome],[lambda])


# salvar_dados(M, 0)
# plot([M], [0])
