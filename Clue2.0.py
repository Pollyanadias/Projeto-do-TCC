import os
import random
from API_Clue import API_Clue

## Definindo as cartas do jogo
armas = ['castiçal', 'corda', 'faca', 'revólver']
locais = ['cozinha', 'hall', 'sala de estar', 'sala de jantar', 'spa']
suspeitos = ['green', 'mustard', 'peacock', 'plum', 'scarlet', 'white']
baralho = armas + locais + suspeitos

## instanciando a classe API_Clue
clue = API_Clue(armas, locais, suspeitos)

## definindo o baralho com as cartas confidenciais
confidencial = [random.choice(armas), random.choice(locais), random.choice(suspeitos)]
for carta in confidencial:
    ## removendo as cartas confidenciais do baralho para que não sejam distribuídas para os jogadores
    baralho.remove(carta)
## embaralhando o baralho    
random.shuffle(baralho)

## Definindo o número de jogadores
while True:
    try:
        num_jogadores = int(input("Informe a quantidade de jogadores: "))
        
        if 2 <= num_jogadores <= 4:
        
            break
        
        else:
            print("Número de jogadores inválido. Deve ser entre 2 e 4.")
    
    except ValueError:
        print("Entrada inválida. Tente novamente.")
    
##definido as informações dos jogadores        
jogadores = []
for i in range(num_jogadores):
    jogadores.append({
        'nome': f'Jogador {i+1}',
        'cartas': [],
        'inocentes': [],
        'notas': [],
        'ativo': True
    })

## Distribuindo as cartas entre os jogadores, uma a uma    
for i, carta in enumerate(baralho):
    jogadores[i % num_jogadores]['cartas'].append(carta)
        

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    

## Função para mostrar a mão do jogador
def mostar_mao(jogador):
    print(f"\n {jogador['nome']}, é a sua vez!")
    print("Cartas:, ", jogador['cartas'])
    print("Inocentes: ", jogador['inocentes'])
    print("Notas: ", jogador['notas'])
    print("-" * 50)

print("Pressione ENTER para continuar...")
input()

jogo_ativo = True
turno = 0

## Loop principal do jogo
while jogo_ativo:
    jogador = jogadores[turno % num_jogadores]
    
    if not jogador['ativo']:
        turno += 1
    
        continue
    
    limpar_tela()
    
    print(f"Turno do {jogador['nome']}")
    print("Pressione ENTER para continuar...")
    input()
    
    limpar_tela()
    
    mostar_mao(jogador)
    
    while True:
        acao = input("Escolha uma ação: (1) Fazer pergunta, (2) Fazer acusação: ").strip()
    
        if acao == '1':
            clue.fazer_pergunta(jogador, jogadores)
            
            break
        
        elif acao == '2':
        
            if clue.fazer_acusacao(jogador, confidencial):
                jogo_ativo = False
            
            break    
        
        else:
            print("Ação inválida. Tente novamente, escolha entre 1 e 2.")
            
    input("Pressione ENTER para continuar...")
    turno += 1
    
    
print("Fim do jogo!")
