class ClasseJogo:
    #definir o cálculo mostrado ao jogador e a resposta correta
    def definirStringERespostaCalculo(self, dificuldade):
        from random import choice, uniform
        stringCalculo = None
        simbolos = None
        simboloEscolhido = None
        numeralUm = None
        numeralDois = None

        #dificuldade 1 = soma ou subtração; números de 0 a 10
        if(dificuldade == 1):
            simbolos = ["+", "-"]
            simboloEscolhido = choice(simbolos)
            numeralUm = choice(range(11))
            numeralDois = choice(range(11))
            stringCalculo = str(numeralUm) + simboloEscolhido + str(numeralDois)
        
        #dificuldade 2 = soma, subtração e multiplicação; números de 0 a 100
        elif(dificuldade == 2):
            simbolos = ["+", "-", "*"]
            simboloEscolhido = choice(simbolos)
            numeralUm = round(uniform(0.0, 100.1), 1)
            numeralDois = round(uniform(0.0, 100.1), 1)
            stringCalculo = str(numeralUm) + simboloEscolhido + str(numeralDois)

        #dificuldade 3 = soma, subtração, multiplicação e divisão; números de 0 a 1000
        else:
            simbolos = ["+", "-", "*"]
            simboloEscolhido = choice(simbolos)
            numeralUm = round(uniform(0.0, 1000.1), 1)
            numeralDois = round(uniform(0.0, 1000.1), 1)
            stringCalculo = str(numeralUm) + simboloEscolhido + str(numeralDois)

        return stringCalculo, eval(stringCalculo)

    #mostrar cálculo e esperar o input do usuário
    def mostrarCalculo(self, dificuldade):
        stringCalculo, resultadoCalculo = self.definirStringERespostaCalculo(dificuldade)
        respostaUsuario = input("\n" + stringCalculo + "? ")
        try: respostaUsuario = float(respostaUsuario)
        except:respostaUsuario = float(resultadoCalculo) - 1
        if(respostaUsuario == float(resultadoCalculo)):
            print('Correto!')
            return True
        else:
            print('Errado!')
            continuar = input("\nContinuar jogando? (s/n)\n")
            while(not(continuar == "s" or continuar == "n")):
                continuar = input("\nEscolha inválida!\nContinuar jogando? (s/n)\n")
            if(continuar == "s"): return True
            else: return False

    def iniciarJogo(self, dificuldade):
        continuarJogo = True
        while(continuarJogo == True):
            continuarJogo = self.mostrarCalculo(dificuldade)
