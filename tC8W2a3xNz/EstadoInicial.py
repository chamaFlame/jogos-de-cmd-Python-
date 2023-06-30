#definir que jogo será escolhido
def perguntarJogo():
    jogoEscolhido = input("\nOlá! escolha o seu jogo:\n1- Pedra Papel Tesoura\n2- Jogo da Velha\n3- Acerte a Conta\n4- Finalizar programa\n")
    
    #continuar perguntando o jogo escolhido enquanto não for feito uma escolha válida
    if(not(int(jogoEscolhido) == 1 or int(jogoEscolhido) == 2 or int(jogoEscolhido) == 3 or int(jogoEscolhido) == 4)):
        print("\nValor inválido! Por favor selecione um dos números abaixo\n")
        jogoEscolhido = input("\nEscolha o seu jogo:\n1- Pedra Papel Tesoura\n2- Jogo da Velha\n3- Acerte a Conta\n4- Finalizar programa\n")
    
    return jogoEscolhido

#definir qual dificuldade será escolhida 
def perguntarDificuldade():
    dificuldadeEscolhida = input("\nEscolha a dificuldade:\n1- Fácil\n2- Médio\n3- Difícil\n")
    
    #continuar perguntando a dificuldade escolhida enquanto não for feito uma escolha válida
    while(not(int(dificuldadeEscolhida) == 1 or int(dificuldadeEscolhida) == 2 or int(dificuldadeEscolhida) == 3)):
        print("\nValor inválido! Por favor selecione um dos números abaixo\n")
        dificuldadeEscolhida = input("\nEscolha a dificuldade:\n1- Fácil\n2- Médio\n3- Difícil\n")

    #converter o valor de "dificuldadeEscolhida" para int e retornar
    return int(dificuldadeEscolhida)