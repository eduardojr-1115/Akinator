import random

opcao = 0

while opcao != 2:
    print("\n1 - Usar o programa")
    print("2 - Sair")

    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    match opcao:
        case 1:
            numero_secreto = random.randint(1, 100)
            print("Você escolheu o programa de adivinhação 🧙‍♂️!")
            print("Pense em um número de 1 a 100...")
            input("Quando estiver pronto, aperte Enter...")
            print("Seu numero é . . .")
            print(numero_secreto)

            acertou = False

            while not acertou:
                resposta = input("Eu acertei o número? ").strip().lower()

                match resposta:
                    case "sim" | "acertou" | "correto" | "certo":
                        print("Acertei! 😎")
                        acertou = True
                    case "não" | "nao" | "errado" | "incorreto":
                        numero_secreto = random.randint(1, 100)
                        print("Poxa, vamos tentar de novo!")
                        print("Seu número é: ", numero_secreto)
                    case _:
                        print("Não entendi sua resposta. Responda com 'sim' ou 'não'.")

        case 2:
            print("Saindo do programa... Foi bom ter você por aqui 👋")

        case _:
            print("Opção inválida")