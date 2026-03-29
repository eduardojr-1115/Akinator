nome = input("Digite seu nome: ")

print("🏦 Bem vindo", nome, "\nAo caixa eletrônico Chama Violeta 🔮")

saldo = int(input("Digite seu saldo: "))

if saldo <= 0:
    print("❌ Saldo insuficiente para saque!")
else:
    saque = int(input("💸 Qual valor deseja sacar: "))

    if saque % 10 != 0:
        print("❌ Saque inválido! Somente notas múltiplas de 10")

    elif saque > saldo:
        print("❌ Saldo insuficiente!")

    else:
        print("✅ Saque realizado com sucesso!")

        saque_original = saque
        saldo -= saque

        print("💰 Saldo final:", saldo)

        # cálculo das notas
        notas_200 = saque // 200
        saque %= 200

        notas_100 = saque // 100
        saque %= 100

        notas_50 = saque // 50
        saque %= 50

        notas_20 = saque // 20
        saque %= 20

        notas_10 = saque // 10

        print("\n💵 Notas entregues:")
        print(f"R$200: {notas_200} nota(s)")
        print(f"R$100: {notas_100} nota(s)")
        print(f"R$50 : {notas_50} nota(s)")
        print(f"R$20 : {notas_20} nota(s)")
        print(f"R$10 : {notas_10} nota(s)")

        print("\n📄 Resumo da transação:")
        print("Cliente:", nome)
        print("Valor sacado:", saque_original)
        print("Saldo restante:", saldo)