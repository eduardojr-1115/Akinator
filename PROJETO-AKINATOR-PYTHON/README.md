# 🔮 Adivinhalândia - Oráculo de Animais em Python

Um jogo de adivinhação inteligente que utiliza estruturas de dados em árvore e aprendizado dinâmico para tentar descobrir em qual animal o usuário está pensando.

## 🧠 Sobre o Projeto
Este projeto foi desenvolvido para praticar conceitos fundamentais de lógica de programação e engenharia de software. O sistema não apenas faz perguntas, mas **aprende** com seus erros, expandindo sua base de conhecimento em tempo real.

## 🛠️ Tecnologias e Conceitos Aplicados
- **Linguagem:** Python 3
- **Persistência de Dados:** Uso de arquivos **JSON** para salvar o progresso e garantir que o aprendizado seja permanente.
- **Estrutura de Dados:** Implementação de uma **Árvore de Decisão** baseada em listas aninhadas.
- **Tratamento de Exceções:** Uso de blocos `try/except` para manipulação de arquivos de forma segura.
- **Sanitização de Inputs:** Tratamento de strings para aceitar variações de acentuação e espaços (ex: "sim", "S", "Não", "nao").

## 🚀 Como Funciona
O programa percorre uma árvore de decisões. Ao chegar em um palpite errado, ele solicita ao usuário:
1. O nome do animal correto.
2. Uma pergunta que o diferencie do palpite anterior.
3. A resposta correta para o novo animal.

Essas informações são reorganizadas na árvore e salvas automaticamente no arquivo `dados.json`.

## ▶️ Como rodar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `akinator.py`.
3. Execute o comando:
   ```bash