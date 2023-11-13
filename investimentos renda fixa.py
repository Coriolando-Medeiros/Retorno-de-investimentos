# Importa as bibliotecas necessárias
import os  # Para funções relacionadas ao sistema operacional
import stdiomask #Para mascarar a senha ao ser digitada
from string import capwords #Para capitular a primeira letra do usúario

# Define uma função para verificar o login com base no nome de usuário e senha
def verificar_login(usuario, senha):
    # Abre o arquivo "login.txt" para leitura
    with open("login.txt", "r") as arquivo:
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo

    # Percorre as linhas do arquivo
    for linha in linhas:
        partes = linha.strip().split(":")  # Divide a linha em partes usando ":" como separador
        if len(partes) == 2:
            usuario_arquivo, senha_arquivo = partes
            # Se o nome de usuário e senha correspondem ao que foi fornecido, retorna True
            if usuario_arquivo == usuario and senha_arquivo == senha:
                return True
    # Se nenhum login válido for encontrado, retorna False
    return False

# Define uma função para limpar a tela do console com base no sistema operacional
def limpar_tela():
    if os.name == "posix":
        os.system("clear")  # Limpa a tela no sistema Unix/Linux
    elif os.name in ("nt", "dos", "ce"):
        os.system("cls")  # Limpa a tela no sistema Windows

# Define uma função para calcular o retorno de investimentos com imposto de renda
def calcula_retorno(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses):
    # Calcula a taxa de juros mensal
    taxa_juros_mensal = taxa_juros_ano / 12

    # Calcula o retorno acumulado considerando o investimento inicial, aporte mensal e taxa de juros
    acumulado = aporte_inicial * (1 + taxa_juros_mensal / 100) ** periodo_meses + \
                         (aporte_mensal / (taxa_juros_mensal / 100)) * \
                         ((1 + taxa_juros_mensal / 100) ** periodo_meses - 1)

    return acumulado

# Define uma função para calcular o retorno de investimentos com imposto de renda
def calcula_final_com_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses):
    dias = periodo_meses * 30
    investimentos = aporte_inicial + (aporte_mensal * periodo_meses)
    usuario = nome_capitulado
    # Verifica a quantidade de dias para determinar a alíquota de imposto de renda
    if dias < 181:
        redimento_bruto = calcula_retorno(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
        juros_totais = redimento_bruto - investimentos
        juros_totais = juros_totais - (juros_totais * 0.225)
        acumulado = rendimentos_ir + investimentos
        print(f"{usuario} seu investimento de {periodo_meses} meses poderá render R$ {acumulado:.2f} líquidos de IR")
        print(f"Sendo R$ {investimentos} de investimentos e R$ {juros_totais:.2f} de juros  de juros totais e R$ {rendimentos_ir:.2f} líquidos")
    elif dias > 181 and dias < 361:
        redimento_bruto = calcula_retorno(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
        juros_totais = redimento_bruto - investimentos
        juros_totais = juros_totais - (juros_totais * 0.200)
        acumulado = rendimentos_ir + investimentos
        print(f"{usuario} seu investimento de {periodo_meses} meses poderá render R$ {acumulado:.2f} líquidos de IR")
        print(f"Sendo R$ {investimentos} de investimentos e R$ {juros_totais:.2f} de juros  de juros totais e R$ {rendimentos_ir:.2f} líquidos")
    elif dias > 361 and dias < 721:
        redimento_bruto = calcula_retorno(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
        juros_totais = redimento_bruto - investimentos
        juros_totais = juros_totais - (juros_totais * 0.175)
        acumulado = rendimentos_ir + investimentos
        print(f"{usuario} seu investimento de {periodo_meses} meses poderá render R$ {acumulado:.2f} líquidos de IR")
        print(f"Sendo R$ {investimentos} de investimentos e R$ {juros_totais:.2f} de juros  de juros totais e R$ {rendimentos_ir:.2f} líquidos")
    elif dias > 721:
        rendimento_bruto = calcula_retorno(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
        juros_totais = rendimento_bruto - investimentos
        rendimentos_ir = juros_totais - (juros_totais * 0.150)
        acumulado = rendimentos_ir + investimentos
        print(f"{usuario} seu investimento de {periodo_meses} meses poderá render R$ {acumulado:.2f} líquidos de IR")
        print(f"Sendo R$ {investimentos} de investimentos e R$ {juros_totais:.2f} de juros  de juros totais e R$ {rendimentos_ir:.2f} líquidos")

# Define uma função para calcular o retorno de investimentos sem imposto de renda
def calcula_final_sem_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses):
    investimentos = aporte_inicial + (aporte_mensal * periodo_meses)
    acumulado = calcula_retorno(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
    usuario = nome_capitulado
    juros_totais = acumulado - investimentos
    print(f"{usuario} seu investimento de {periodo_meses} meses poderá render R$ {acumulado:.2f} líquidos de IR")
    print(f"Sendo R$ {investimentos} de investimentos e R$ {juros_totais:.2f} de juros")

def menu():
    print("")
    print("Menu")
    print("")
    print("1 -> Tesouro Direto - IR de 22,5% a 15%")
    print("2 -> CDB - IR de 22,5% a 15%")
    print("3 -> LCI - IR Pessoa Física Isento")
    print("4 -> LCA - IR Pessoa Física Isento")
    print("5 -> Poupança - IR Isento")
    print("6 -> Debêntures - IR de 22,5% a 15%")
    print("7 -> Fundos de Renda Fixa - IR de 22,5% a 15%")
    print("0 -> Sair")

# Imprime uma mensagem de boas-vindas
print("")
print("Sistema de cálculo de retorno de investimentos")

# Loop principal
while True:
    # Solicita o nome de usuário e senha
    usuario = input("Usuário: ")
    senha = stdiomask.getpass(prompt= 'Senha: ', mask='*')
    nome_capitulado = capwords(usuario)
    
    # Verifica o login com base no nome de usuário e senha
    if verificar_login(usuario, senha):
        limpar_tela()
        print(f"Login efetuado! {nome_capitulado}")
        break
    else:
        print("Usuário ou senha incorretos.")
    

# Limpa a tela do console

while True:
    # Exibe as opções do menu para o usuário
    menu()
    # Solicita a opção do usuário e converte para um número inteiro
    try:
        opcao = int(input("Digite a opção: "))
        if opcao > 0 or opcao < 8: 
                # Verifica a opção selecionada pelo usuário
                if opcao == 0:
                    # Se a opção for 0, exibe agradecimento e sai da aplicação encerrando o loop
                    limpar_tela()
                    print("Obrigado por usar nossos sistemas")
                    print("Saindo da aplicação!...")
                    break

                elif opcao > 0 and opcao < 8:
                        # Se a opção for maior que zero, executa o bloco de código dentro do try
                        try:
                            # Tenta converter e obter o valor do investimento inicial, mensal e taxa de juros anual
                            aporte_inicial = float(input("Investimento inicial: ").replace(',', '.'))
                            if aporte_inicial > 0:
                                aporte_mensal = float(input("Investimento mensal: ").replace(',', '.'))
                                if aporte_mensal >= 0:
                                    taxa_juros_ano = float(input("Taxa de juros anual: ").replace(',', '.'))
                                    if taxa_juros_ano >= 0:
                                        periodo_meses = int(input("Tempo de investimentos - meses: "))
                                        # Verifica a opção escolhida e chama a função correspondente
                                        if opcao == 1:
                                            calcula_final_com_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                        elif opcao == 2:
                                            calcula_final_com_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                        elif opcao == 3:
                                            calcula_final_sem_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                        elif opcao == 4:
                                            calcula_final_sem_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                        elif opcao == 5:
                                            calcula_final_sem_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                        elif opcao == 6:
                                            calcula_final_com_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                        elif opcao == 7:
                                            calcula_final_com_ir(aporte_inicial, taxa_juros_ano, aporte_mensal, periodo_meses)
                                    else:
                                        print("Taxa de juros anual inválida!")
                                else:
                                    print("Investimento mensal inválido!")
                            else:
                                print("Investimento inicial inválido!")
                        except ValueError:
                            # Se houver erro na conversão para float, exibe uma mensagem de valor inválido
                            print("Valor inválido. Certifique-se de usar um número válido e utilize ponto (.) em vez de vírgula (,).")
    except ValueError: 
        # Se houver erro na escolha da opção
        limpar_tela()
        print("Valor inválido. Certifique-se de usar um número válido")
    else:
        # Se a opção não for válida, exibe uma mensagem de opção inválida
        print("Opção inválida!")
