def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
palavra_secreta = "banana"
enforcou = False
acertou = False
while (not acertou and not enforcou):
    print("Jogando...")
    chute = input("Qual é a letra?")
    chute = chute.strip()

    index = 0 
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1
    print("Fim do jogo")

    if(__name__ == "__main__"):
        jogar()
