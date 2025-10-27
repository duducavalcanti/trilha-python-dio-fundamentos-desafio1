# 💰 Otimizando o Sistema Bancário com Funções Python

![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

---

## 📌 Índice

- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Autor](#autor)

---

## ⚙️ Funcionalidades

| Comando | Função             | Descrição                                                                 |
| ------- | ------------------ | ------------------------------------------------------------------------- |
| `d`     | Depositar          | Realiza depósitos em uma conta.                                           |
| `s`     | Sacar              | Efetua saques, validando saldo, limite e número máximo de saques diários. |
| `e`     | Extrato            | Exibe extrato de movimentações e saldo atual.                             |
| `nu`    | Novo usuário       | Cadastra um novo cliente do banco, validando CPF.                         |
| `lu`    | Listar usuários    | Lista todos os usuários cadastrados.                                      |
| `nc`    | Nova conta         | Cria uma nova conta vinculada a um usuário existente.                     |
| `lc`    | Listar contas      | Lista todas as contas cadastradas no sistema.                             |
| `lcu`   | Contas por usuário | Lista todas as contas vinculadas a um usuário pelo CPF.                   |
| `q`     | Sair               | Encerra o programa.                                                       |

---

## 🏗 Estrutura do Projeto

O sistema é modularizado em funções:

- `depositar()` – depósitos (argumentos posicionais)
- `sacar()` – saques (keyword-only)
- `exibir_extrato()` – extrato (posicional + keyword)
- `validar_cpf()` – valida CPF
- `criar_usuario()` – cadastra novos usuários
- `listar_usuarios()` – lista usuários cadastrados
- `filtrar_usuario()` – busca usuário pelo CPF
- `criar_conta()` – cria conta bancária
- `listar_contas()` – lista todas as contas
- `listar_contas_por_usuario()` – lista contas de um usuário
- `main()` – função principal, gerencia o fluxo e menu

---

## 🚀 Como Executar

1. Certifique-se de ter **Python 3.x** instalado.
2. Clone o repositório:

```bash
git clone https://github.com/duducavalcanti/trilha-python-dio-fundamentos-desafio1.git
```

3. Acesse a pasta raiz do sistema:

```bash
cd sistema-bancario
```

4. Execute o arquivo do sistema:

```bash
python desafio_fundamentos.py
```

## 👤 Autor

Eduardo Cavalcanti
