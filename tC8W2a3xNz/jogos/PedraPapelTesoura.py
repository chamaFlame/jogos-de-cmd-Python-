class ClasseJogo:
    itensJogo = ["Pedra", "Papel", "Tesoura"]
    escolhaMaquina = None
    escolhaJogador = None

    #definir a escolha do jogador
    def fazerEscolhaJogador(self):
        self.escolhaJogador = input("\nEscolha:\n1- Pedra\n2- Papel\n3- Tesoura\n")
        self.escolhaJogador = self.escolhaJogador.lower()

        #continuar perguntando um item valido caso o jogador tenha feito uma escolha inválida
        while(not(self.escolhaJogador == "1" or self.escolhaJogador == "2" or self.escolhaJogador == "3" or self.escolhaJogador == "pedra" or self.escolhaJogador == "papel" or self.escolhaJogador == "tesoura")):
            print("\nEscolha inválida! Por favor escolha um dos ítens abaixo.")
            self.escolhaJogador = input("\nEscolha:\n1- Pedra\n2- Papel\n3- Tesoura\n")
            self.escolhaJogador = self.escolhaJogador.lower()

        #se o item for escolhido através de números, fazer a conversão abaixo
        try:
            self.escolhaJogador = int(self.escolhaJogador)
            self.escolhaJogador = self.escolhaJogador - 1
            self.escolhaJogador = self.itensJogo[self.escolhaJogador]

        #caso o item tenha sido escrito por extenso, fazer a conversão abaixo
        except:
            if(self.escolhaJogador == "pedra"):
                self.escolhaJogador = self.itensJogo[0]
            elif(self.escolhaJogador == "papel"):
                self.escolhaJogador = self.itensJogo[1]
            else:
                self.escolhaJogador = self.itensJogo[2]
    
        #mostrar a escolha final do jogador
        print("\nVocê escolheu: " + self.escolhaJogador)

    #definir a escolha da máquina
    def fazerEscolhaCpu(self, dificuldade):
        from random import choice as escolher
        chances = None
        #definir as possibilidades de vitória, empate e derrota através da dificuldade escolhida
        if(dificuldade == 1):
            chances = ["vencer", "vencer", "vencer", "empate", "perder"]
        elif(dificuldade == 2):
            chances = ["vencer", "empate", "empate", "empate", "perder"]
        else:
            chances = ["vencer", "empate", "perder", "perder", "perder"]

        #definir a escolha final da máquina através de uma das possibilidades escolhidas
        resultado = escolher(chances)
        if(resultado == "vencer"):
            #pedra vs tesoura, papel vs pedra, tesoura vs papel
            if(self.escolhaJogador == "Pedra"): self.escolhaMaquina = self.itensJogo[2]
            elif(self.escolhaJogador == "Papel"): self.escolhaMaquina = self.itensJogo[0]
            else: self.escolhaMaquina = self.itensJogo[1]
        elif(resultado == "empate"): self.escolhaMaquina = self.escolhaJogador
        else:
            #pedra vs papel, papel vs tesoura, tesoura vs pedra
            if(self.escolhaJogador == "Pedra"): self.escolhaMaquina = self.itensJogo[1]
            elif(self.escolhaJogador == "Papel"): self.escolhaMaquina = self.itensJogo[2]
            else: self.escolhaMaquina = self.itensJogo[0]

        #mostrar escolha da máquina
        print("\nEu escolho " + self.escolhaMaquina + "!\n")

    #definir o resultado final
    def resultadoFinal(self):
        print(self.escolhaJogador + " VS " + self.escolhaMaquina)
        resultadoJogo = None
        if(self.escolhaJogador == self.escolhaMaquina):
            resultadoJogo = "Empate!"

        #resultados caso as escolhas não sejam iguais
        else:
            if(self.escolhaJogador == "Pedra"):
                if(self.escolhaMaquina == "Papel"): resultadoJogo = "Você perdeu!"
                else: resultadoJogo = "Você venceu!"
            elif(self.escolhaJogador == "Papel"):
                if(self.escolhaMaquina == "Tesoura"): resultadoJogo = "Você perdeu!"
                else: resultadoJogo = "Você venceu!"
            else:
                if(self.escolhaMaquina == "Pedra"): resultadoJogo = "Você perdeu!"
                else: resultadoJogo = "Você venceu!"

        #mostrar resultado final
        print(resultadoJogo + "\n")

    #definir se o jogo será jogado novamente ou se o programa será fechado
    def jogarDenovo(self):
        escolha = input("Jogar novamente? (s/n): ")
        escolha = escolha.lower()
        while(not(escolha == "s" or escolha == "n")):
            print("\nEscolha inválida! Por favor escolha uma dos ítens abaixo.\n")
            escolha = input("Jogar novamente? (s/n): ")
        #if(escolha == "n"): quit()
        if(escolha == "s"): return True
        else: return False

    #função que rodará todo o jogo
    def iniciarJogo(self, dificuldade):
        continuarJogo = True
        while(continuarJogo == True):
            self.fazerEscolhaJogador()
            self.fazerEscolhaCpu(dificuldade)
            self.resultadoFinal()
            continuarJogo = self.jogarDenovo()
