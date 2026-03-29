import json

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return ["Seu animal vive na água? 🐠", "Baleia", "Gato"]

def salvar_dados(banco):
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(banco, arquivo, indent=4, ensure_ascii=False)

def tratar_resposta(resp):
    resp = resp.lower().strip()
    if resp in ["não", "nao", "n"]:
        return "nao"
    if resp in ["sim", "s"]:
        return "sim"
    return resp

banco_dados = carregar_dados()

while True:
    print("\n" + "="*30)
    print("🔮 Bem-vindo à Adivinhalândia!")
    
    no_atual = banco_dados
    no_pai = None
    lado = None

    while type(no_atual) == list:
        pergunta = no_atual[0]
        resposta = tratar_resposta(input(f"{pergunta} (sim/nao): "))
        
        if resposta == "sair":
            exit()

        no_pai = no_atual
        if resposta == "sim":
            lado = 1
            no_atual = no_atual[1]
        else:
            lado = 2
            no_atual = no_atual[2]

    print(f"\n✨ Eu acho que é: {no_atual}")
    acertou = tratar_resposta(input("Acertei? (sim/nao): "))

    if acertou == "sim":
        print("😎 Eu sou demais!")
    else:
        animal_correto = input("Qual era o animal? ").strip()
        pergunta_nova = input(f"Que pergunta diferencia {animal_correto} de {no_atual}? ").strip()
        resp_novo = tratar_resposta(input(f"Para {animal_correto}, a resposta é sim ou nao? "))

        nova_estrutura = [pergunta_nova, animal_correto, no_atual] if resp_novo == "sim" else [pergunta_nova, no_atual, animal_correto]

        if no_pai is None:
            banco_dados = nova_estrutura
        else:
            no_pai[lado] = nova_estrutura
        
        salvar_dados(banco_dados)
        print("📚 Aprendi!")

    if tratar_resposta(input("\nJogar de novo? (sim/nao): ")) == "nao":
        break