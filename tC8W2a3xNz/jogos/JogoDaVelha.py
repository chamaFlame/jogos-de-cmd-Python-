class ClasseJogo:
    casas = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]
    
    #mostrar todas as casas
    def mostrarCasas(self):
        print("\n" + self.casas[0] + "   " + self.casas[1] + "   " + self.casas[2] + "\n" + self.casas[3] + "   " + self.casas[4] + "   " + self.casas[5] + "\n" + self.casas[6] + "   " + self.casas[7] + "   " + self.casas[8] + "\n")
    
    #alterar o simbolo da casa escolhida
    def jogadaDoJogador(self):
        casaEscolhida = input("Escolha uma das casas disponíveis: ")
        while(not(casaEscolhida == "1" or casaEscolhida == "2" or casaEscolhida == "3" or casaEscolhida == "4" or casaEscolhida == "5" or casaEscolhida == "6" or casaEscolhida == "7" or casaEscolhida == "8" or casaEscolhida == "9")):
            self.mostrarCasas()
            casaEscolhida = input("Escolha inválida!\nEscolha uma das casas disponíveis: ")
        while(not(self.casas[int(casaEscolhida) - 1] == "?")):
            self.mostrarCasas()
            casaEscolhida = input("Escolha inválida!\nEscolha uma das casas disponíveis: ")
        self.casas[int(casaEscolhida) - 1] = "O"
        self.mostrarCasas()

    #máquina fazer a sua escolha e alterar o símbolo da casa
    def jogadaDaMaquina(self, dificuldade):
        from random import choice as escolher
        escolhaMaquina = 0

        #dificuldade 1 = escolher aleatoriamente
        if(dificuldade == 1):
            escolhaMaquina = escolher(range(9))
            while(not(self.casas[escolhaMaquina] == "?")):
               escolhaMaquina = escolher(range(9))

        #dificuldade 2 = escolher de modo defensivo
        if(dificuldade == 2):
            if((self.casas[1] == self.casas[2] == "O" or self.casas[3] == self.casas[6] == "O" or self.casas[4] == self.casas[8] == "O") and self.casas[0] == "?"):
                escolhaMaquina = 0
            elif((self.casas[0] == self.casas[2] == "O" or self.casas[4] == self.casas[7] == "O") and self.casas[1] == "?"):
                escolhaMaquina = 1
            elif((self.casas[0] == self.casas[1] == "O" or self.casas[4] == self.casas[6] == "O" or self.casas[5] == self.casas[8] == "O") and self.casas[2] == "?"):
                escolhaMaquina = 2
            elif((self.casas[0] == self.casas[6] == "O" or self.casas[4] == self.casas[5] == "O") and self.casas[3] == "?"):
                escolhaMaquina = 3
            elif((self.casas[0] == self.casas[8] == "O" or self.casas[6] == self.casas[2] == "O" or self.casas[3] == self.casas[5] == "O") and self.casas[4] == "?"):
                escolhaMaquina = 4
            elif((self.casas[2] == self.casas[8] == "O" or self.casas[3] == self.casas[4] == "O") and self.casas[5] == "?"):
                escolhaMaquina = 5
            elif((self.casas[0] == self.casas[3] == "O" or self.casas[2] == self.casas[4] == "O" or self.casas[7] == self.casas[8] == "O") and self.casas[6] == "?"):
                escolhaMaquina = 6
            elif((self.casas[1] == self.casas[4] == "O" or self.casas[6] == self.casas[8] == "O") and self.casas[7] == "?"):
                escolhaMaquina = 7
            elif((self.casas[0] == self.casas[4] == "O" or self.casas[2] == self.casas[5] == "O" or self.casas[6] == self.casas[7] == "O") and self.casas[8] == "?"):
                escolhaMaquina = 8

            #caso não seja necessária a defesa, escolher uma casa aleatóriamente
            else:
               escolhaMaquina = escolher(range(9))
               while(not(self.casas[escolhaMaquina] == "?")):
                   escolhaMaquina = escolher(range(9))

        #dificuldade 3 = escolher de modo ofensivo e defensivo
        else:
            if((self.casas[1] == self.casas[2] == "X" or self.casas[3] == self.casas[6] == "X" or self.casas[4] == self.casas[8] == "X") and self.casas[0] == "?"):
                escolhaMaquina = 0
            elif((self.casas[0] == self.casas[2] == "X" or self.casas[4] == self.casas[7] == "X") and self.casas[1] == "?"):
                escolhaMaquina = 1
            elif((self.casas[0] == self.casas[1] == "X" or self.casas[4] == self.casas[6] == "X" or self.casas[5] == self.casas[8] == "X") and self.casas[2] == "?"):
                escolhaMaquina = 2
            elif((self.casas[0] == self.casas[6] == "X" or self.casas[4] == self.casas[5] == "X") and self.casas[3] == "?"):
                escolhaMaquina = 3
            elif((self.casas[0] == self.casas[8] == "X" or self.casas[6] == self.casas[2] == "X" or self.casas[3] == self.casas[5] == "X") and self.casas[4] == "?"):
                escolhaMaquina = 4
            elif((self.casas[2] == self.casas[8] == "X" or self.casas[3] == self.casas[4] == "X") and self.casas[5] == "?"):
                escolhaMaquina = 5
            elif((self.casas[0] == self.casas[3] == "X" or self.casas[2] == self.casas[4] == "X" or self.casas[7] == self.casas[8] == "X") and self.casas[6] == "?"):
                escolhaMaquina = 6
            elif((self.casas[1] == self.casas[4] == "X" or self.casas[6] == self.casas[8] == "X") and self.casas[7] == "?"):
                escolhaMaquina = 7
            elif((self.casas[0] == self.casas[4] == "X" or self.casas[2] == self.casas[5] == "X" or self.casas[6] == self.casas[7] == "X") and self.casas[8] == "?"):
                escolhaMaquina = 8
            elif((self.casas[1] == self.casas[2] == "O" or self.casas[3] == self.casas[6] == "O" or self.casas[4] == self.casas[8] == "O") and self.casas[0] == "?"):
                escolhaMaquina = 0
            elif((self.casas[0] == self.casas[2] == "O" or self.casas[4] == self.casas[7] == "O") and self.casas[1] == "?"):
                escolhaMaquina = 1
            elif((self.casas[0] == self.casas[1] == "O" or self.casas[4] == self.casas[6] == "O" or self.casas[5] == self.casas[8] == "O") and self.casas[2] == "?"):
                escolhaMaquina = 2
            elif((self.casas[0] == self.casas[6] == "O" or self.casas[4] == self.casas[5] == "O") and self.casas[3] == "?"):
                escolhaMaquina = 3
            elif((self.casas[0] == self.casas[8] == "O" or self.casas[6] == self.casas[2] == "O" or self.casas[3] == self.casas[5] == "O") and self.casas[4] == "?"):
                escolhaMaquina = 4
            elif((self.casas[2] == self.casas[8] == "O" or self.casas[3] == self.casas[4] == "O") and self.casas[5] == "?"):
                escolhaMaquina = 5
            elif((self.casas[0] == self.casas[3] == "O" or self.casas[2] == self.casas[4] == "O" or self.casas[7] == self.casas[8] == "O") and self.casas[6] == "?"):
                escolhaMaquina = 6
            elif((self.casas[1] == self.casas[4] == "O" or self.casas[6] == self.casas[8] == "O") and self.casas[7] == "?"):
                escolhaMaquina = 7
            elif((self.casas[0] == self.casas[4] == "O" or self.casas[2] == self.casas[5] == "O" or self.casas[6] == self.casas[7] == "O") and self.casas[8] == "?"):
                escolhaMaquina = 8

            #caso não seja necessária a defesa ou ofensiva, escolher uma casa aleatóriamente
            else:
               escolhaMaquina = escolher(range(9))
               while(not(self.casas[escolhaMaquina] == "?")):
                   escolhaMaquina = escolher(range(9))

        #alterar o valor da casa escolhida
        self.casas[escolhaMaquina] = "X"

    #checar se o jogo acabou
    def checarFimDeJogo(self):
        self.mostrarCasas()
        jogoAcabou = False
        if(set([self.casas[0], self.casas[1], self.casas[2]]) == set(["O"]) or set([self.casas[0], self.casas[1], self.casas[2]]) == set(["X"])):
            if(self.casas[0] == self.casas[1] == self.casas[2] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[0] == self.casas[1] == self.casas[2] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[0], self.casas[4], self.casas[8]]) == set(["O"]) or set([self.casas[0], self.casas[4], self.casas[8]]) == set(["X"])):
            if(self.casas[0] == self.casas[4] == self.casas[8] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[0] == self.casas[4] == self.casas[8] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[0], self.casas[3], self.casas[6]]) == set(["O"]) or set([self.casas[0], self.casas[3], self.casas[6]]) == set(["X"])):
            if(self.casas[0] == self.casas[3] == self.casas[6] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[0] == self.casas[3] == self.casas[6] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[1], self.casas[4], self.casas[7]]) == set(["O"]) or set([self.casas[1], self.casas[4], self.casas[7]]) == set(["X"])):
            if(self.casas[1] == self.casas[4] == self.casas[7] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[1] == self.casas[4] == self.casas[7] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[2], self.casas[4], self.casas[6]]) == set(["O"]) or set([self.casas[2], self.casas[4], self.casas[6]]) == set(["X"])):
            if(self.casas[2] == self.casas[4] == self.casas[6] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[2] == self.casas[4] == self.casas[6] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[2], self.casas[5], self.casas[8]]) == set(["O"]) or set([self.casas[2], self.casas[5], self.casas[8]]) == set(["X"])):
            if(self.casas[2] == self.casas[5] == self.casas[8] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[2] == self.casas[5] == self.casas[8] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[3], self.casas[4], self.casas[5]]) == set(["O"]) or set([self.casas[3], self.casas[4], self.casas[5]]) == set(["X"])):
            if(self.casas[3] == self.casas[4] == self.casas[5] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[3] == self.casas[4] == self.casas[5] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[6], self.casas[7], self.casas[8]]) == set(["O"]) or set([self.casas[6], self.casas[7], self.casas[8]]) == set(["X"])):
            if(self.casas[6] == self.casas[7] == self.casas[8] == "X"):
                print("Você perdeu!")
                jogoAcabou = True
            elif(self.casas[6] == self.casas[7] == self.casas[8] == "O"):
                print("Você venceu!")
                jogoAcabou = True
        elif(set([self.casas[0], self.casas[1], self.casas[2], self.casas[3], self.casas[4], self.casas[5], self.casas[6], self.casas[7], self.casas[8]]) == set(["X", "O"])):
            print("Empate!")
            jogoAcabou = True
        return jogoAcabou

    #definir se o jogador ou a máquina vai começar
    def escolherIniciante(self):
        from random import choice as escolher
        iniciante = escolher(range(2))
        self.mostrarCasas()
        return iniciante

    #definir se o jogador irá jogar novamente
    def jogarNovamente(self):

        #fazer pergunta ao jogador e continuar perguntando caso não seja feita uma escolha válida
        escolha = input("\nJogar novamente? (s/n)\n")
        escolha = escolha.lower()
        while(not(escolha == "s" or escolha == "n")):
            escolha = input("\nEscolha inválida!\nJogar novamente? (s/n)\n")
            escolha = escolha.lower()

        #se for escolhido que "sim", voltar o array das casas para o estado inicial, mostrá-la e retornar False, indicando que o jogo não será finalizado
        if(escolha == "s"): 
            for x in range(len(self.casas)):
                self.casas[x] = "?"
            return False
        
        #se for escolhido que "não", retornar valor True, indicando que o jogo será finalizado
        else: return True

    #método que rodará o jogo
    def iniciarJogo(self, dificuldade):
        jogoFinalizado = False
        #jogador começa
        if(self.escolherIniciante() == 0):
            while(jogoFinalizado == False):
                self.jogadaDoJogador()
                jogoFinalizado = self.checarFimDeJogo()
                if(jogoFinalizado == True): 
                    jogoFinalizado = self.jogarNovamente()
                    if(jogoFinalizado == False):
                        self.mostrarCasas()
                else:
                    self.jogadaDaMaquina(dificuldade)
                    jogoFinalizado = self.checarFimDeJogo()
                    if(jogoFinalizado == True): 
                        jogoFinalizado = self.jogarNovamente()
                        if(jogoFinalizado == False):
                            self.mostrarCasas()

        #cpu começa
        else:
            while(jogoFinalizado == False):
                self.jogadaDaMaquina(dificuldade)
                jogoFinalizado = self.checarFimDeJogo()
                if(jogoFinalizado == True): 
                    jogoFinalizado = self.jogarNovamente()
                    if(jogoFinalizado == False):
                        self.mostrarCasas()
                else:
                    self.jogadaDoJogador()
                    jogoFinalizado = self.checarFimDeJogo()
                    if(jogoFinalizado == True): 
                        jogoFinalizado = self.jogarNovamente()
                        if(jogoFinalizado == False):
                            self.mostrarCasas()