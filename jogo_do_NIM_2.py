def NIM():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    x=0
    print("1 - para jogar uma partida isolada ou")
    x=int(input("2 - para jogar um campeonato.   1 ou 2? "))
    print()
    if x==1:
        print("Você escolheu uma partida!")
        print()
        partida()
    elif x==2:
        print("você escolheu um campeonato!")
        print()
        campeonato()
    else:
        print("Resposta inválida!")
        NIM()
def usuario_escolhe_jogada(n,m):
    a=0
    while (a<1) or (a>m):
        a=int(input("Quantas peças você vai tirar? "))
        print()
        if (a<1) or (a>m):
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            jogada=a
    return jogada
def computador_escolhe_jogada(n,m):
    if n<=m:
        a=n
        jogada=a
    else:
        a=0
        g=1
        while (n%(m+1)!=0):
            n=n-g
            a=a+1
        jogada=a
        if jogada>m:
            jogada=m
    return jogada
def partida():
    n=0
    n=int(input("Quantas peças? "))
    while n<1:
        print("Número de peças deve ser maior que zero.")
        n=int(input("Quantas peças? "))
    m=0
    while m>n or (m<1):
        m=int(input("Limite de peças por jogada? "))
        if m>n or (m<1):
            print("Limite de peças por jogada inválido! O limite deve ser menor ou igual a quantidade máxima de peças e maior ou igual a 1.")
    if (n%(m+1))==0:
        print()
        print("Você começa!")
        r=0
    else:
        print()
        print("Computador começa!")
        r=1
    while n!=0:
        if r==0:
            r=r+1
            print()
            u=usuario_escolhe_jogada(n,m)
            if u==1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",u,"peças.")
            n=n-u
            if n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n,"peças no tabuleiro.")
        if r==1:
            r=r-1
            print()
            c=computador_escolhe_jogada(n,m)
            if c==1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",c,"peças.")
            n=n-c
            if n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n,"peças no tabuleiro.")
    if n==0:
        print()
        if r==0:
            print("Fim de jogo! O computador ganhou!")
        else:
            print("Fim do jogo! Parabéns! Você ganhou!")
        print()
def campeonato():
    print("***Rodada 1***")
    print()
    partida()
    u=0
    p=1
    print("***Rodada 2***")
    print()
    partida()
    p=p+1
    print("***Rodada 3***")
    print()
    partida()
    p=p+1
    print("***Fim do campeonato!***")
    print()
    print("Placar: Você",u,"X",p,"Computador")
q=NIM()