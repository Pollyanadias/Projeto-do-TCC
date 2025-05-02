
class API_Clue:
    
    
    ## Inicializa a classe com as cartas de armas, locais e suspeitos
    def __init__(self, armas, locais, suspeitos):
        self.armas = armas
        self.locais = locais
        self.suspeitos = suspeitos
    
    
    ##define o baralho com as cartas de armas, locais e suspeitos    
    def validar_carta(self, carta):
        return carta in self.armas or carta in self.locais or carta in self.suspeitos
        
    
    ## define a função para responder a pergunta do jogador
    def responder(self, jogador_Questionado, jogador_Perguntador, cartas_Perguntadas):
        cartas_comuns = [i for i in jogador_Questionado['cartas'] if i in cartas_Perguntadas]
        
        if cartas_comuns:
            ## Se o jogador questionado tem cartas que podem ajudar
            print(f"{jogador_Questionado['nome']} tem cartas que podem ajudar!")
            
            ## Se o jogador questionado tem apenas uma carta que pode ajudar, ele mostra essa carta
            if len(cartas_comuns) == 1:
                carta_escolhida = cartas_comuns[0]
            
            else:
                ## Se o jogador questionado tem mais de uma carta que pode ajudar, ele escolhe uma carta para mostrar
                print(f"{jogador_Questionado['nome']}, você tem mais de uma carta que pode ajudar. Escolha uma para mostrar.")
            
                while True:
                    carta_escolhida = input(f"{jogador_Questionado['nome']}, escolha uma carta para mostrar: {cartas_comuns} ")
                    
                    if carta_escolhida in cartas_comuns:
                    
                        break
                    
                    print("Carta inválida. Tente novamente.")
            
            print(f"{jogador_Questionado['nome']} mostrou a carta: {carta_escolhida} para {jogador_Perguntador['nome']}")
            
            ## Adiciona a carta mostrada lista de inocentes do jogador questionador
            ## Se a carta já estiver na lista de inocentes, não adiciona novamente
            if carta_escolhida not in jogador_Perguntador['inocentes']:
                jogador_Perguntador['inocentes'].append(carta_escolhida)
            jogador_Perguntador['notas'].append(f"Recebeu {carta_escolhida} de {jogador_Questionado['nome']}")
            
            ## mostra que a carta foi mostrada
            return True
        
        print(f"{jogador_Questionado['nome']} não pode ajudar.")
        
        ## Se o jogador questionado não tem cartas que podem ajudar, ele diz que não pode ajudar
        return False
    
    
    ## define a função para fazer uma pergunta ao jogador
    def fazer_pergunta(self, jogador_atual, jogadores):
        print(f"{jogador_atual['nome']}, faça uma pergunta ao jogador a sua esquerda.")
        
        while True:
            carta1 = input("Digite a primeira carta: ").strip().lower()
            carta2 = input("Digite a segunda carta: ").strip().lower()
            
            ## Verifica se as cartas são válidas
            if self.validar_carta(carta1) and self.validar_carta(carta2):
                
                break
            
            print("Uma ou mais cartas inválidas. Tente novamente.")
        
        
        num_jogadores = len(jogadores)
        index = jogadores.index(jogador_atual)
        
        ## Pergunta ao jogador a sua esquerda
        for i in range(1, num_jogadores):
            jogador_questionado_index = (index + i) % num_jogadores
            jogador_questionado = jogadores[jogador_questionado_index]
            
            ## Verifica se o jogador questionado está ativo
            if not jogador_questionado['ativo']:
                
                continue
            
            ## Para no loop se o jogador questionado responder
            if self.responder(jogador_questionado, jogador_atual, [carta1, carta2]):
                
                return
        
        print("Não posso ajudar")
        
    
    ## define a função para fazer uma acusação ao jogador
    def fazer_acusacao(self, jogador, confidencial):
        print(f"{jogador['nome']}, faça uma acusação.")
        
        ## pede para o jogador informar a arma, o local e o suspeito para fazer a acusação
        while True:
            arma = input("Digite o nome da arma: ").strip().lower()
            local = input("Digite o nome do local: ").strip().lower()
            suspeito = input("Digite o nome do suspeito: ").strip().lower()
            acusacao = [arma, local, suspeito]
            
            ##verifica se a acusação é válida
            if sorted(acusacao) == sorted(confidencial):
                print(f"Acusação correta! {jogador['nome']} ganhou o jogo.")
               
                return True
            
            ## Se a acusação não for válida, o jogador perde e não pode mais jogar
            else:
                print("Acusação incorreta. Você está fora do jogo.")
                jogador['ativo'] = False
               
                return False
            