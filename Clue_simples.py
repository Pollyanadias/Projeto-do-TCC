import random

# cartas do baralho
armas = ['castiçal', 'corda', 'faca', 'revolver']
locais = ['cozinha', 'hall', 'sala de estar', 'sala de jantar', 'spa']
suspeitos = ['green', 'mustard', 'peacock', 'plum', 'scarlet', 'white']

# cria o baralho
baralho = suspeitos + armas + locais
random.shuffle(baralho)

# seleciona as cartas confidenciais
confidencial = [
    random.choice(armas),
    random.choice(locais),
    random.choice(suspeitos)
]

# remove cartas confidenciais do baralho
for carta in confidencial:
    baralho.remove(carta)

# distribui cartas entre os jogadores
jogadores = []
num_jogadores = 4
for i in range(num_jogadores):
    jogadores.append({
        'nome': f'Jogador {i+1}',
        'cartas': [],
        'inocentes': [],
        'ativo': True
    })

# vai distribuir as cartas entre os jogadores
for i, carta in enumerate(baralho):
    jogadores[i % num_jogadores]['cartas'].append(carta)


# vai mostrar a mão de cada jogador
def mostrar_mao(jogador):
    print(f"{jogador['nome']}, suas cartas: {jogador['cartas']}")
    print(f"Inocentes: {jogador['inocentes']}")


# as funções para perguntar e acusar
def perguntar(jogador_atual, jogadores):
    print(f"\n{jogador_atual['nome']} está perguntando...")
    carta1 = input("Digite a primeira carta que deseja perguntar: ")
    carta2 = input("Digite a segunda carta que deseja perguntar: ")

    # descobre a posição do jogador que vai responder a pergunta
    index_pergunta = jogadores.index(jogador_atual)
    proximo = (index_pergunta + 1) % len(jogadores)
    jogador_quest = jogadores[proximo]

    cartas_para_mostrar = [c for c in jogador_quest['cartas'] if c == carta1 or c == carta2]
    if cartas_para_mostrar:
        # aqui a escolha esta aleatória, mas a ideia e que seja possivel fazer a escolha, mas para fins de teste resolvi fazer assim
        carta_mostrada = random.choice(cartas_para_mostrar)
        print(f"{jogador_quest['nome']} mostrou a carta: {carta_mostrada}")
        jogador_atual['inocentes'].append(carta_mostrada)
    else:
        print(f"{jogador_quest['nome']} disse: 'Não posso ajudá-lo.'")


def acusar(jogador_atual):
    print(f"\n{jogador_atual['nome']} está fazendo uma acusação!")
    arma = input("Arma: ")
    local = input("Local: ")
    suspeito = input("Suspeito: ")

    acusacao = [arma, local, suspeito]
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

print("Bem-vindo ao Clue! Vamos começar!\n")

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
