
class API_Clue:
    
    
    def __init__(self, armas, locais, suspeitos):
        self.armas = armas
        self.locais = locais
        self.suspeitos = suspeitos
        
    def validar_carta(self, carta):
        return carta in self.armas or carta in self.locais or carta in self.suspeitos
        
    
    def responder(self, jogador_Questionado, jogador_Perguntador, cartas_Perguntadas):
        cartas_comuns = [i for i in jogador_Questionado['cartas'] if i in cartas_Perguntadas]
        
        if cartas_comuns:
            print(f"{jogador_Questionado['nome']} tem cartas que podem ajudar: {cartas_comuns}")
            
            if len(cartas_comuns) == 1:
                carta_escolhida = cartas_comuns[0]
            
            else:
                
                while True:
                    carta_escolhida = input(f"{jogador_Questionado['nome']}, escolha uma carta para mostrar: {cartas_comuns} ")
                    
                    if carta_escolhida in cartas_comuns:
                    
                        break
                    
                    print("Carta inválida. Tente novamente.")
            
            print(f"{jogador_Questionado['nome']} mostrou a carta: {carta_escolhida} para {jogador_Perguntador['nome']}")
            
            if carta_escolhida not in jogador_Perguntador['inocentes']:
                jogador_Perguntador['inocentes'].append(carta_escolhida)
            jogador_Perguntador['notas'].append(f"Recebeu {carta_escolhida} de {jogador_Questionado['nome']}")
            
            return True
        
        return False
    
    
    def fazer_pergunta(self, jogador_atual, jogadores):
        print(f"{jogador_atual['nome']}, faça uma pergunta ao jogador a sua esquerda.")
        
        while True:
            carta1 = input("Digite a primeira carta: ").strip().lower()
            carta2 = input("Digite a segunda carta: ").strip().lower()
            
            if self.validar_carta(carta1) and self.validar_carta(carta2):
                
                break
            
            print("Uma ou mais cartas inválidas. Tente novamente.")
        
        num_jogadores = len(jogadores)
        index = jogadores.index(jogador_atual)
        
        for i in range(1, num_jogadores):
            jogador_questionado_index = (index + i) % num_jogadores
            jogador_questionado = jogadores[jogador_questionado_index]
            
            if not jogador_questionado['ativo']:
                
                continue
            
            if self.responder(jogador_questionado, jogador_atual, [carta1, carta2]):
                
                return
        
        print("Não posso ajudar")
        
    
    def fazer_acusacao(self, jogador, confidencial):
        print(f"{jogador['nome']}, faça uma acusação.")
        
        while True:
            arma = input("Digite o nome da arma: ").strip().lower()
            local = input("Digite o nome do local: ").strip().lower()
            suspeito = input("Digite o nome do suspeito: ").strip().lower()
            acusacao = [arma, local, suspeito]
            
            if sorted(acusacao) == sorted(confidencial):
                print(f"Acusação correta! {jogador['nome']} ganhou o jogo.")
               
                return True
            
            else:
                print("Acusação incorreta. Você está fora do jogo.")
                jogador['ativo'] = False
               
                return False
            