import json

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo: # Adicionei encoding para evitar erros
            return json.load(arquivo)
    except FileNotFoundError:
        return ["Seu animal vive na água? 🐠", "Baleia", "Gato"]

def salvar_dados(banco):
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(banco, arquivo, indent=4, ensure_ascii=False) # ensure_ascii=False mantém os acentos bonitos no arquivo

# --- FUNÇÃO PARA LIMPAR A RESPOSTA ---
def tratar_resposta(resp):
    # Remove espaços, coloca em minúsculo e aceita "não" com ou sem til
    resp = resp.lower().strip()
    if resp in ["não", "nao", "n"]:
        return "nao"
    if resp in ["sim", "s"]:
        return "sim"
    return resp

banco_dados = carregar_dados()

# --- LOOP PRINCIPAL DO JOGO ---
while True:
    print("\n" + "="*30)
    print("🔮 Bem-vindo à Adivinhalândia!")
    print("Pense em um animal... ou digite 'sair' para encerrar.")
    
    no_atual = banco_dados
    no_pai = None
    lado = None

    # Navegação na árvore
    while type(no_atual) == list:
        pergunta = no_atual[0]
        resposta = tratar_resposta(input(f"{pergunta} (sim/nao): "))
        
        if resposta == "sair":
            print("👋 Até a próxima!")
            exit() # Fecha o programa

        no_pai = no_atual
        if resposta == "sim":
            lado = 1
            no_atual = no_atual[1]
        else:
            lado = 2
            no_atual = no_atual[2]

    # Palpite Final
    print(f"\n✨ Eu acho que é: {no_atual}")
    acertou = tratar_resposta(input("Acertei? (sim/nao): "))

    if acertou == "sim":
        print("😎 Eu sou demais! Sabia que ia conseguir.")
    else:
        # Pergunta se quer ensinar
        quer_ensinar = tratar_resposta(input("😅 Droga! Quer me ensinar esse animal novo? (sim/nao): "))
        
        if quer_ensinar == "sim":
            animal_correto = input("Qual era o animal? ").strip()
            pergunta_nova = input(f"Que pergunta eu faço para diferenciar {animal_correto} de {no_atual}? ").strip()
            resp_novo = tratar_resposta(input(f"Para {animal_correto}, a resposta é sim ou nao? "))

            if resp_novo == "sim":
                nova_estrutura = [pergunta_nova, animal_correto, no_atual]
            else:
                nova_estrutura = [pergunta_nova, no_atual, animal_correto]

            if no_pai is None:
                banco_dados = nova_estrutura
            else:
                no_pai[lado] = nova_estrutura
            
            salvar_dados(banco_dados)
            print("📚 Aprendi! Agora estou mais esperto.")
        else:
            print("👌 Sem problemas! Vamos jogar de novo.")

    # Pergunta se quer continuar jogando
    jogar_de_novo = tratar_resposta(input("\nQuer jogar outra rodada? (sim/nao): "))
    if jogar_de_novo == "nao":
        print("👋 Valeu por jogar! Até mais.")
        break # Quebra o loop principal e encerra