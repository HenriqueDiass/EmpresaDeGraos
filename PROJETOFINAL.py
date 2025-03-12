import json
import tabulate
import time

faturamento = {"faturamento": []}

dadosCL = {
    "Nome": [],
    "CPF": [],
    "Idade": []
}
Estoque = {
    "Nome": [],
    "Quantidade": [],
    "Valor": []
}
def menu():
    while True:
        print("====== Menu ======")
        print("1. Terminal vendedor")
        print("2. Terminal gerente")
        print("3. Sair")
        menu = input("Escolha o terminal que voce deseja ser direcionado: ")
        if menu == "1":
            loginV = input("LOGIN: ")
            senhaV = input("SENHA: ")
            if loginV == "Equipe" and senhaV == "123":
            
                print("====== TERMINAL DE VENDAS ======")
                print("1. Vender Produto")
                print("2. Cadastrar cliente")
                print("3. Voltar para Menu inicial")
                menuV = input("Escolha o terminal que voce deseja ser direcionado: ")
                if menuV =="1":
                    print("====== AREA DE VENDAS ======")
                    areaDevendas()
                if menuV =="2":
                    print("====== AREA DE CADASTRAMENTO ======")
                    cadastro_cliente()
                if menuV =="3":
                    print("VOLTAR MENU PRINCIPAL")
            else:
                print("LOGIN OU SENHA INVALIDOS!!")
                print("")
        if menu == "2":
            loginG = input("LOGIN: ")
            senhaG = input("SENHA: ")
            if loginG == "Gerente" and senhaG == "123":
                print("====== TERMINAL DE GERENCIA ======")
                print("1. Cadastros")
                print("2. Estoque")
                print("3. Exibir faturamento")
                print("4. Voltar para Menu inicial")
                menuG = input("Escolha o terminal que voce deseja ser direcionado: ")

                if menuG == "1":
                    print("====== AREA DE CADASTROS ======")
                    print("1. Exibir cadastros")
                    print("2. Remover cadastro")
                    print("3. voltar para menu inicial")
                    menuAreaDeCadastro = input("Escolha o terminal que voce deseja ser direcionado: ")
                    if menuAreaDeCadastro == "1":
                        tabuletCL()
                    if menuAreaDeCadastro == "2":
                        atulazarCL()
                    if menuAreaDeCadastro == "3":
                        print("VOLTANDO")
                if menuG =="2":
                    print("====== AREA DO ESTOQUE ======")
                    print("1. Adicionar produto no estoque:")
                    print("2. Editar estoque")
                    menuAreaDoEstoque = input("Escolha o terminal que voce deseja ser direcionado: ")
                    if menuAreaDoEstoque == "1":
                        adicionarE()
                    if menuAreaDoEstoque == "2":
                        atualizarE()
                if menuG =="3":
                    faturamentoT()    
            else:
                print("LOGIN OU SENHA INVALIDOS!!")
                print("")                
                if menuG =="4":
                    print("VOLTAR MENU PRINCIPAL")
        if menu == "3":
            print("Saindo do programa.")
            break           

            
def areaDevendas():             
    with open("Estoque.json", "r") as arquivo:
        Estoque = json.load(arquivo)
    tabuletE()

    print("Qual o nome do produto que você deseja comprar?")
    produtoE = input()
    print("Qual a quantidade de produto que você deseja comprar?")
    quantidadeP = int(input())

    if produtoE in Estoque["Nome"]:
        indice = Estoque["Nome"].index(produtoE)
        quantidadeDisponivel = int(Estoque["Quantidade"][indice])

        if quantidadeP <= quantidadeDisponivel:
            Estoque["Quantidade"][indice] = quantidadeDisponivel - quantidadeP  ########
            valorT = float(Estoque["Valor"][indice])
            valorT = valorT * quantidadeP

            if valorT <= 100:
                print("PARABENS VOCE FOI PREMIADO COM UM DESCONTO DE 5%")
                des = 5 / 100 * valorT
                pn = valorT - des
                print(f'O valor da sua venda com desconto de 5% é de R$ {pn}')

            elif valorT <= 150:
                print("PARABENS VOCE FOI PREMIADO COM UM DESCONTO DE 10%")
                des = 10 / 100 * valorT
                pn = valorT - des
                print(f'O valor da sua venda com desconto de 10% é de R$ {pn}')

            elif valorT <= 350:
                print("PARABENS VOCE FOI PREMIADO COM UM DESCONTO DE 15%")
                des = 15 / 100 * valorT
                pn = valorT - des
                print(f'O valor da sua venda com desconto de 15% é de R$ {pn}')
            
            elif valorT > 350:
                print("PARABENS VOCE FOI PREMIADO COM UM DESCONTO DE 20%")
                des = 20 / 100 * valorT
                pn = valorT - des
                print(f'O valor da sua venda com desconto de 20% é de R$ {pn}')


            # Atualiza faturamento globalmente
            with open("faturamento.json", "r") as arquivo:
                faturamento = json.load(arquivo)
            faturamento["faturamento"].append(pn)  # Adiciona o valor com desconto

            with open("faturamento.json", "w") as arquivo:
                json.dump(faturamento, arquivo, indent=4)

            with open("Estoque.json", "w") as arquivo:
                json.dump(Estoque, arquivo, indent=4)

            print("Compra realizada com sucesso!")
            print("Quantidade atualizada no estoque:", Estoque["Quantidade"][indice])
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não encontrado no estoque.")


def cadastro_cliente():
    print("Digite o nome do cliente que você deseja cadastrar:")
    nomeCL = input().strip().upper()  # Remover espaços e deixar em maiúsculas
    time.sleep(3)
    print("Digite o cpf do cliente:")
    cpf = input().strip()  # Remover espaços extras
    time.sleep(3)
    print("Digite a idade do cliente:")
    idade = int(input())

    if len(cpf) == 11 and idade >= 18:  # Verifica se o CPF tem 11 dígitos e a idade é maior ou igual a 18
        # Carregar os dados do arquivo
        with open("dadosCL.json", "r") as arquivo:
            dadosCL = json.load(arquivo)

        # Adicionar o novo cliente aos dados
        dadosCL["Nome"].append(nomeCL)
        dadosCL["CPF"].append(cpf)
        dadosCL["Idade"].append(idade)

        # Salvar os dados atualizados no arquivo
        with open("dadosCL.json", "w") as arquivo:
            json.dump(dadosCL, arquivo)  # Salva com indentação
            time.sleep(2)
        print("Cliente cadastrado! Apto a receber descontos ao final da compra!")
        espaço()
        tabuletCL()
    else:
        print("Erro no cadastro. Certifique-se de que o CPF tem 11 dígitos e a idade seja maior ou igual a 18.")

def tabuletCL():
    with open("dadosCL.json", "r") as arquivo:
        dadosCL = json.load(arquivo)
    print(tabulate.tabulate(dadosCL, headers="keys", tablefmt="grid"))

def atulazarCL():
    with open("dadosCL.json", "r") as arquivo:
        dadosCL = json.load(arquivo)
        tabuletCL()
    print("de qual cliente voce deseja alterar os dados")
    cliente = input()
    if cliente in dadosCL["Nome"]:
        indice = dadosCL["Nome"].index(cliente)
        print("O que você deseja atualizar?")
        print("1. Nome")
        print("2. Idade")
        print("3. CPF")
        print("4. Excluir por completo")
        print("5. voltar para menu inicial")
        menuCL = input()
        print("")

        if menuCL == "1":
            novo_nome = input("Digite o novo nome: ")
            dadosCL["Nome"][indice] = novo_nome
        elif menuCL == "2":
            nova_idade = input("Digite a nova idade: ")
            dadosCL["Idade"][indice] = nova_idade
        elif menuCL == "3":
            novo_CPF = input("Digite o novo CPF: ")
            dadosCL["CPF"][indice] = novo_CPF
        elif menuCL == "4":
            # del serve para excluir o dado do indice
            del dadosCL["Nome"][indice]
            del dadosCL["Idade"][indice]
            del dadosCL["CPF"][indice]
            print("Cadastro excluído com sucesso!")
        elif menuCL == "5":
            print("Voltando para menu inicial")
            espaço()
        else:
            print("Opção inválida.")

        # Salvar as alterações no arquivo JSON
        with open("dadosCL.json", "w") as arquivo:
            json.dump(dadosCL, arquivo, indent=4)
        print("Dados atualizados com sucesso!")
    else:
        print("Nome não encontrado no cadastro.")
    espaço()   
    tabuletCL()

def adicionarE():
    with open("Estoque.json", "r") as arquivo:
        Estoque = json.load(arquivo)
    tabuletE()
            # Adicionar um produto
    print("Digite o produto que você deseja adicionar:")
    produto = input()
    print("Digite a quantidade do produto que você deseja adicionar:")
    qtd = int(input())
    print("Digite o valor do produto que você deseja adicionar:")
    valor = float(input())
    if qtd >= 10 and valor > 0:
        Estoque["Nome"].append(produto)
        Estoque["Quantidade"].append(qtd)
        valor = valor + 2.50
        Estoque["Valor"].append(valor)
    if qtd < 10 or valor == 0:
        print("NÃO É POSSIVEL ADICIONAR PRODUTO COM ESSA QUANTIDADE OU ESSE VALOR")

            # Salvar os novos dados no arquivo
    with open("Estoque.json", "w") as arquivo:
        json.dump(Estoque, arquivo, indent=4)

    print("Produto adicionado com sucesso!")
    tabuletE()   

def tabuletE():
    with open("Estoque.json", "r") as arquivo:
        Estoque = json.load(arquivo)
    print(tabulate.tabulate(Estoque, headers="keys", tablefmt="grid"))

def atualizarE():
 
    with open("Estoque.json", "r") as arquivo:
        Estoque = json.load(arquivo)
        tabuletE()
    print("qual produto voce deseja modificar")
    produto = input()
    if produto in Estoque["Nome"]:
        indice = Estoque["Nome"].index(produto)
        print("menu de atualizaçao de produtos")
        print("1. Nome")
        print("2. quantidade")
        print("3. valor")
        print("4. Excluir por completo")
        print("5. Voltar para o menu inicial")
        menuE = input()
        espaço()

        if menuE == "1":
            novo_nome = input("Digite o novo nome: ")
            Estoque["Nome"][indice] = novo_nome
        elif menuE == "2":
            novaQuantidade = input("Digite a nova quantidade: ")
            Estoque["Quantidade"][indice] = novaQuantidade
        elif menuE == "3":
            novoValor = input("Digite o novo valor: ")
            Estoque["Valor"][indice] = novoValor
        elif menuE == "4":
            # del serve para excluir o dado do indice
            del Estoque["Nome"][indice]
            del Estoque["Quantidade"][indice]
            del Estoque["Valor"][indice]
            print("Cadastro excluído com sucesso!")
        elif menuE =="5":
            print("Voltando para menu inicial")
            espaço()
        else:
            print("Opção inválida.")

        # Salvar as alterações no arquivo JSON
        with open("Estoque.json", "w") as arquivo:
            json.dump(Estoque, arquivo, indent=4)
        print("Dados atualizados com sucesso!")
    else:
        print("Nome não encontrado no cadastro.")
    tabuletE()
    
def faturamentoT():
    with open("faturamento.json", "r") as arquivo:
        faturamento = json.load(arquivo)
    # Somar os valores no faturamento
    total_faturamento = sum(faturamento["faturamento"])

    print(f"O faturamento total é: {total_faturamento}")

def espaço():
    for i in range(2):
        print("")

menu()