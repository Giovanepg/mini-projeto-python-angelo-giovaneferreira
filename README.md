# 🏪 Sistema de Gerenciamento de Produtos em Python

Este projeto apresenta um **sistema interativo de cadastro e gerenciamento de produtos**, desenvolvido em **Python** e executado diretamente no **terminal**.  
O programa permite **cadastrar, listar, buscar, atualizar e excluir produtos**, além de organizá-los por **categorias predefinidas**.

---

## ⚙️ Estrutura Geral

O sistema utiliza um **menu interativo baseado em um loop `while`**, que mantém o programa em execução até o usuário optar por sair (opção `0`).  
Cada opção do menu executa uma função específica, tornando o código modular e fácil de entender.

---

## 🧩 Funcionalidades Principais

### 1️⃣ Cadastrar Produto
- Solicita ao usuário:
  - Código do produto  
  - Nome  
  - Preço  
  - Quantidade  
- Em seguida, o usuário escolhe a **categoria** (Alimentos, Bebidas, Limpeza, Vestuário ou N/A).  
- O produto é salvo como um **dicionário** dentro da lista `lista_produtos`.  
- Um **set (`set_produtos`)** é usado para evitar produtos duplicados.

### 2️⃣ Listar Produtos
- Exibe todos os produtos cadastrados, **agrupados por categoria**.  
- Mostra o código, nome, preço e quantidade de cada item.  
- Caso não haja produtos cadastrados, informa o usuário.

### 3️⃣ Buscar Produto
- Permite procurar um produto pelo **código**.  
- Exibe suas informações detalhadas: código, nome, preço, quantidade e categoria.  
- Caso o produto não exista, mostra uma mensagem de erro.

### 4️⃣ Atualizar Item
- Busca o produto pelo código e permite **editar todos os seus dados**:  
  - Código, nome, preço, quantidade e categoria.  
- Substitui o produto antigo pelos novos dados informados.

### 5️⃣ Excluir Produto
- Solicita o código e **remove o produto correspondente** da lista.  
- Exibe quantos produtos foram excluídos (geralmente um).

### 0️⃣ Sair
- Encerra a execução do sistema com uma mensagem de despedida.

---

## 🧠 Estruturas de Dados Utilizadas

| Estrutura | Função |
|------------|--------|
| **`list` (lista)** | Armazena todos os produtos cadastrados (`lista_produtos`). |
| **`set` (conjunto)** | Evita a duplicação de nomes de produtos (`set_produtos`). |
| **`tuple` (tupla)** | Define as categorias fixas de produtos (`tup_categorias`). |
| **`dict` (dicionário)** | Representa cada produto com seus atributos (código, nome, preço, quantidade e categoria). |

---

## 🔄 Estruturas de Controle

O sistema utiliza:

- **`while`** → mantém o menu em execução até o usuário sair.  
- **`for`** → percorre os produtos nas operações de listagem, busca e exclusão.  
- **`if / elif / else`** → controla o fluxo das opções e valida entradas do usuário.  
- **Funções (`def`)** → organizam o código e separam a lógica de cada operação.

---

## 🧮 Categorias Disponíveis

As categorias de produtos são pré-definidas e armazenadas na tupla `tup_categorias`:

| Código | Categoria  |
|--------:|-------------|
| 1 | Alimentos |
| 2 | Bebidas |
| 3 | Limpeza |
| 4 | Vestuário |
| Outro | N/A (não especificado) |

---

# 2. Sistema de Controle de Alunos e Notas

## 🧮 Descrição do Código

O código apresenta um **sistema interativo em Python** para **cadastro e gerenciamento de alunos e suas notas**, desenvolvido para ser executado diretamente no terminal.

Seu funcionamento é baseado em um **menu de opções** que permite ao usuário interagir com o sistema, cadastrando alunos, registrando notas, consultando médias e verificando quem foi aprovado ou reprovado.

---

## ⚙️ Estrutura Geral

O sistema utiliza um **loop `while`** que mantém o programa em execução até que o usuário escolha a opção **"0 - Sair"**.  
Dentro do laço, são exibidas as opções do menu, e o usuário escolhe o que deseja fazer.

---

## 🧩 Principais Funcionalidades

### 1️⃣ Cadastrar Aluno
- Solicita a **matrícula** e o **nome** do aluno.  
- Verifica se o nome já foi cadastrado (evitando duplicações por meio de um `set`).  
- Armazena o aluno no dicionário principal `alunos` com sua matrícula como chave.

### 2️⃣ Registrar Nota
- Solicita o número da matrícula.  
- Permite registrar **3 notas** para o aluno informado.  
- As notas são salvas como uma **tupla**, associada ao nome do aluno dentro do dicionário.

### 3️⃣ Listar Alunos e Médias
- Percorre todos os alunos cadastrados e calcula a **média aritmética** das notas.  
- Exibe a matrícula, nome e média (com uma casa decimal).  
- Caso o aluno ainda não tenha notas, o sistema avisa.

### 4️⃣ Mostrar Aprovados e Reprovados
- Calcula a média de cada aluno e classifica:
  - ✅ **Aprovado**: média maior ou igual a 7.  
  - ❌ **Reprovado**: média menor que 7.  
- Exibe o nome do aluno, a média e o status.

### 0️⃣ Sair
- Encerra a execução do sistema com uma mensagem de saída.

---

## 🧠 Estruturas de Dados Utilizadas

| Estrutura | Função |
|------------|--------|
| **`dict` (dicionário)** | Armazena os alunos, usando a matrícula como chave e uma tupla (nome, notas) como valor. |
| **`tuple` (tupla)** | Guarda as notas de cada aluno, tornando-as imutáveis após registro. |
| **`set` (conjunto)** | Evita que nomes duplicados sejam cadastrados mais de uma vez. |
| **`list` (lista)** | Armazena temporariamente as notas digitadas antes de convertê-las em tupla. |

---

## 🔄 Estruturas de Controle

O programa faz uso de:

- **`while`** → mantém o menu ativo até que o usuário opte por sair.  
- **`for`** → percorre e exibe os alunos, calcula médias e registra notas.  
- **`if / elif / else`** → controla o fluxo do menu e valida as opções escolhidas.

---