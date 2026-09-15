
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa um jogo clássico de adivinhação de palavras usando strings, loops, condicionais e entrada de dados em Python. Esta atividade ajudará você a praticar seleção aleatória, manipulação de strings e controle do estado do jogo.

## 📝 Tarefas

### 🛠️ Criar a Seleção da Palavra e Configurar o Jogo

#### Description
Crie a estrutura inicial do jogo da forca definindo uma lista de palavras, selecionando uma palavra aleatoriamente e preparando a exibição da palavra oculta.

#### Requirements
O programa concluído deve:

- Usar uma lista predefinida de palavras e escolher uma delas aleatoriamente.
- Exibir a palavra oculta como sublinhados, por exemplo, `_ _ _ _ _`.
- Manter o controle das letras já informadas pelo jogador.
- Pedir ao jogador que informe uma letra e validar a entrada.

### 🛠️ Implementar a Lógica do Jogo e as Condições de Encerramento

#### Description
Desenvolva o loop principal para que o jogador possa adivinhar letras até revelar a palavra ou esgotar as tentativas.

#### Requirements
O programa concluído deve:

- Mostrar o progresso atual após cada palpite, por exemplo, `H _ N _ A _`.
- Contar as tentativas incorretas e reduzir o número de vidas restantes.
- Permitir palpites repetidos sem perder o progresso quando as letras repetidas estiverem corretas.
- Encerrar o jogo quando a palavra for totalmente descoberta ou quando o jogador ficar sem tentativas.
- Exibir uma mensagem de vitória quando a palavra for concluída e uma mensagem de derrota quando as tentativas acabarem.