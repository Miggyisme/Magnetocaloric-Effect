from mpmath import mp, exp, tanh

mp.dps=50 # Define as casas decimais de precisão

def tanh(x):
        # Calculando os termos
        termo1 = mp.exp(x)
        termo2 = mp.exp(-x)

        # Truncando para 40 casas decimais
        termo1_str = str(termo1)[:42]  # Pega a string com os primeiros 50 decimais
        termo2_str = str(termo2)[:42]  # Pega a string com os primeiros 50 decimais

        # Convertendo de volta para mp.mpf
        termo1_trunc = mp.mpf(termo1_str)
        termo2_trunc = mp.mpf(termo2_str)

        # Calculando o valor final de tanh(x)
        return (termo1_trunc - termo2_trunc) / (termo1_trunc + termo2_trunc)