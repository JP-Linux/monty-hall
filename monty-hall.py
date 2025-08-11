from random import randint, choice

ganho = 0
perda = 0
simulacoes = 1000000

for _ in range(simulacoes):
    premio = randint(0, 2)
    escolha = randint(0, 2)

    # O apresentador abre uma caixa vazia que não é o prêmio nem a escolha
    caixas_disponiveis = [0, 1, 2]
    caixas_disponiveis.remove(escolha)
    if premio in caixas_disponiveis:
        caixas_disponiveis.remove(premio)
    aberta = choice(caixas_disponiveis)

    # Troca de caixa: escolhe a que não é a original nem a aberta
    nova_escolha = next(i for i in [0, 1, 2] if i != escolha and i != aberta)

    if nova_escolha == premio:
        ganho += 1
    else:
        perda += 1

print(f"Resultado após {simulacoes} simulações (sempre trocando):")
print(f"Vitórias: {ganho} ({ganho/simulacoes*100:.2f}%)")
print(f"Derrotas: {perda} ({perda/simulacoes*100:.2f}%)")
