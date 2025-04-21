import random

# Categorias
armas = ['castiçal', 'corda', 'faca', 'revolver']
locais = ['cozinha', 'hall', 'sala de estar', 'sala de jantar', 'spa']
suspeitos = ['green', 'mustard', 'peacock', 'plum', 'scarlet', 'white']

# Criação do baralho
baralho = suspeitos + armas + locais
random.shuffle(baralho)

# Selecionar as cartas confidenciais
confidencial = [
    random.choice(armas),
    random.choice(locais),
    random.choice(suspeitos)
]

# Remover cartas confidenciais do baralho
for carta in confidencial:
    baralho.remove(carta)

# Distribuir cartas entre os jogadores
jogadores = []
num_jogadores = 4
for i in range(num_jogadores):
    jogadores.append({
        'nome': f'Jogador {i+1}',
        'cartas': [],
        'inocentes': [],
        'ativo': True
    })

for i, carta in enumerate(baralho):
    jogadores[i % num_jogadores]['cartas'].append(carta)

# Funções auxiliares
def mostrar_mao(jogador):
    print(f"{jogador['nome']}, suas cartas: {jogador['cartas']}")
    print(f"Inocentes: {jogador['inocentes']}")

def perguntar(jogador_atual, jogadores):
    print(f"\n{jogador_atual['nome']} está perguntando...")
    item1 = input("Digite a primeira carta para perguntar: ")
    item2 = input("Digite a segunda carta para perguntar: ")

    index_pergunta = jogadores.index(jogador_atual)
    proximo = (index_pergunta + 1) % len(jogadores)
    jogador_respondente = jogadores[proximo]

    cartas_para_mostrar = [c for c in jogador_respondente['cartas'] if c == item1 or c == item2]
    if cartas_para_mostrar:
        carta_mostrada = random.choice(cartas_para_mostrar)
        print(f"{jogador_respondente['nome']} mostrou a carta: {carta_mostrada}")
        jogador_atual['inocentes'].append(carta_mostrada)
    else:
        print(f"{jogador_respondente['nome']} disse: 'Não posso ajudá-lo.'")

def acusar(jogador_atual):
    print(f"\n{jogador_atual['nome']} está fazendo uma acusação!")
    suspeito = input("Suspeito: ")
    arma = input("Arma: ")
    comodo = input("Local: ")

    acusacao = [suspeito, arma, comodo]
    if sorted(acusacao) == sorted(confidencial):
        print(f"\n{jogador_atual['nome']} acertou a acusação! Venceu o jogo!")
        return True
    else:
        print(f"\n{jogador_atual['nome']} errou! Agora só poderá responder perguntas.")
        jogador_atual['ativo'] = False
        return False

# Loop principal do jogo
jogo_ativo = True
turno = 0

print("Bem-vindo ao Clue no Terminal! Vamos começar!\n")

while jogo_ativo:
    jogador = jogadores[turno % num_jogadores]

    if not jogador['ativo']:
        turno += 1
        continue

    print(f"\nTurno de {jogador['nome']}")
    mostrar_mao(jogador)

    acao = input("Escolha uma ação: (1) Para perguntar ou (2) para acusar: ").lower()

    if acao == '1':
        perguntar(jogador, jogadores)
    elif acao == '2':
        venceu = acusar(jogador)
        if venceu:
            jogo_ativo = False

    turno += 1
