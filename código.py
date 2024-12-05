import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while tentativas < 5:
        chute_str = input("Digite seu chute: ")
        chute = int(chute_str)
        tentativas += 1

        if chute < numero_secreto:
            print("O seu chute foi menor que o número secreto.")
        elif chute > numero_secreto:
            print("O seu chute foi maior que o número secreto.")
        else:
            print("Parabéns! Você acertou em", tentativas, "tentativas!")
            return

    print("O número secreto era:", numero_secreto)
    print("Você perdeu!")

if _name_ == "_main_":
    jogar()
