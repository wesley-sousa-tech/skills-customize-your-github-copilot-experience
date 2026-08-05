
# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo da Forca em Python para praticar manipulação de strings, laços de repetição, condicionais e tratamento de entrada do usuário.

## 📝 Tarefas

### 🛠️ Implementar Seleção de Palavra e Configuração Inicial

#### Descrição
Crie a configuração inicial do jogo definindo uma lista de palavras, selecionando uma palavra aleatória e inicializando o estado da partida.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente a partir de uma lista predefinida.
- Inicializar a exibição da palavra oculta usando sublinhados (por exemplo: `_ _ _ _`).
- Definir o número inicial de tentativas incorretas permitidas.

### 🛠️ Construir o Laço de Palpites e Condições de Encerramento

#### Descrição
Implemente o laço principal do jogo para receber palpites de letras, atualizar o progresso e encerrar a partida com um resultado claro.

#### Requisitos
O programa concluído deve:

- Aceitar palpites de letras do usuário, um por vez.
- Revelar as letras corretamente adivinhadas na exibição atual da palavra.
- Diminuir as tentativas restantes apenas quando o palpite estiver incorreto.
- Encerrar com uma mensagem de vitória quando a palavra for totalmente adivinhada.
- Encerrar com uma mensagem de derrota quando as tentativas chegarem a zero.