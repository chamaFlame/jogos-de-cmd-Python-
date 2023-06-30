def main():
    from tC8W2a3xNz import EstadoInicial

    #definir o jogo escolhido e a dificuldade 
    jogoEscolhido = EstadoInicial.perguntarJogo()
    while(not(int(jogoEscolhido) == 4)):
        dificuldade = EstadoInicial.perguntarDificuldade()

        #iniciar jogo de Pedra Papel Tesoura
        if(int(jogoEscolhido) == 1):
            from tC8W2a3xNz.jogos.PedraPapelTesoura import ClasseJogo
            objeto = ClasseJogo()
            objeto.iniciarJogo(dificuldade)
                
        #iniciar Jogo da Velha
        elif(int(jogoEscolhido) == 2):
            from tC8W2a3xNz.jogos.JogoDaVelha import ClasseJogo
            objeto = ClasseJogo()
            objeto.iniciarJogo(dificuldade)

        #Iniciar jogo de Acerte a Conta
        else:
            from tC8W2a3xNz.jogos.AcerteAConta import ClasseJogo
            objeto = ClasseJogo()
            objeto.iniciarJogo(dificuldade)

        #quando um jogo for finalizado, perguntar qual será o próximo jogo
        jogoEscolhido = EstadoInicial.perguntarJogo()
        
    #finalizar o programa
    if(int(jogoEscolhido) == 4):
        finalizar = input("\nAperte Enter para finalizar\n")

#rodar algoritmo
if __name__ == '__main__':
    main()