import random

def gerar_combinacoes(historico, qtd, dezenas, excluir, estrategia):
    numeros = list(range(1, 26))
    freq = {n: 0 for n in numeros}

    # Conta frequência no histórico
    for col in historico.columns:
        for n in numeros:
            freq[n] += (historico[col] == n).sum()

    # Remove excluídos
    numeros = [n for n in numeros if n not in excluir]

    # Estratégias
    if estrategia == 'mais_frequentes':
        numeros.sort(key=lambda x: freq[x], reverse=True)
    elif estrategia == 'menos_frequentes':
        numeros.sort(key=lambda x: freq[x])
    else:
        random.shuffle(numeros)

    # Gera combinações
    jogos = []
    for _ in range(qtd):
        jogo = random.sample(numeros, dezenas)
        jogos.append(sorted(jogo))

    return jogos
