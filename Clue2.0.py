import random
from API_Clue import API_Clue

armas = ['castiçal', 'corda', 'faca', 'revólver']
locais = ['coxinha', 'hall', 'sala de estar', 'sala de jantar', 'spa']
suspeitos = ['green', 'mustard', 'peacock', 'plum', 'scarlet', 'white']
baralho = armas + locais + suspeitos

clue = API_Clue(armas, locais, suspeitos)

confidencial = [random.choice(armas), random.choice(locais), random.choice(suspeitos)]
for carta in confidencial:
    baralho.remove(carta)
random.shuffle(baralho)


while True:
    try:
        num_jogadores = int(input("Informe a quantidade de jogadores: "))
        
        if 2 <= num_jogadores <= 4:
        
            break
        
        else:
            print("Número de jogadores inválido. Deve ser entre 2 e 4.")
    
    except ValueError:
        print("Entrada inválida. Tente novamente.")
    
        
jogadores = []
for i in range(num_jogadores):
    jogadores.append({
        'nome': f'Jogador {i+1}',
        'cartas': [],
        'inocentes': [],
        'notas': [],
        'ativo': True
    })