
# ==========================================================
# SISTEMA DE REGISTO DE NASCIMENTOS E IDENTIFICACAO
# DE RECEM-NASCIDOS
# ==========================================================

from datetime import datetime


nascimentos = []


numero = 1




def registar_nascimento():
    global numero

    print("\n========== REGISTO DE NASCIMENTO ==========")

 
    nome_mae = input("Nome completo da mãe: ")
    id_mae = input("Número de identificação da mãe: ")
    contacto = input("Contacto da mãe: ")
  
    nome_bebe = input("Nome do recém-nascido: ")

    while True:
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")

        try:
            data = datetime.strptime(data_nascimento, "%d/%m/%Y")

            if data.month == 10:
                break
            else:
                print("Atenção: só são permitidos nascimentos de outubro.")

        except ValueError:
            print("Data inválida. Tente novamente.")

  
    while True:
        genero = input("Género (M/F): ").upper()

        if genero == "M" or genero == "F":
            break
        else:
            print("Opção inválida. Introduza M ou F.")

    medico = input("Nome do médico responsável: ")

    id_bebe = "RN" + str(numero).zfill(4)

    bebe = {
        "id": id_bebe,
        "nome": nome_bebe,
        "genero": genero,
        "data": data_nascimento,
        "mae": nome_mae,
        "id_mae": id_mae,
        "contacto": contacto,
        "medico": medico
    }

    # Adicionar o registo à lista
    nascimentos.append(bebe)

    print("\nNascimento registado com sucesso!")
    print("Número de identificação:", id_bebe)

    numero += 1




def consultar_registo():
    print("\n========== CONSULTA DE REGISTO ==========")

    id_mae = input("Introduza o número de identificação: ")

    encontrado = False

   
    for bebe in nascimentos:

        if bebe["id_mae"] == id_mae:

            print("\nDados do recém-nascido:")
            print("Identificação:", bebe["id"])
            print("Nome:", bebe["nome"])

            if bebe["genero"] == "M":
                print("Género: Masculino")
            else:
                print("Género: Feminino")

            print("Data de nascimento:", bebe["data"])
            print("Nome da mãe:", bebe["mae"])
            print("Médico responsável:", bebe["medico"])

            encontrado = True

    
    if not encontrado:
        print("Nenhum registo encontrado para esta mãe.")




def listar_nascimentos():

    print("\n========== LISTA DE NASCIMENTOS ==========")

    if len(nascimentos) == 0:
        print("Não existem nascimentos registados.")
        return

    for bebe in nascimentos:

        print("\nIdentificação:", bebe["id"])
        print("Nome do bebé:", bebe["nome"])

        if bebe["genero"] == "M":
            print("Género: Masculino")
        else:
            print("Género: Feminino")

        print("Data:", bebe["data"])
        print("Mãe:", bebe["mae"])
        print("Médico:", bebe["medico"])
        print("----------------------------------------")



def apresentar_estatisticas():

    print("\n========== ESTATÍSTICAS ==========")

    total = len(nascimentos)
    masculino = 0
    feminino = 0

    for bebe in nascimentos:

        if bebe["genero"] == "M":
            masculino += 1
        else:
            feminino += 1

    print("Total de nascimentos:", total)
    print("Bebés masculinos:", masculino)
    print("Bebés femininos:", feminino)

    if total > 0:

        percentagem_m = (masculino / total) * 100
        percentagem_f = (feminino / total) * 100

        print("Percentagem masculina:", round(percentagem_m, 2), "%")
        print("Percentagem feminina:", round(percentagem_f, 2), "%")

    else:
        print("Ainda não existem dados para calcular estatísticas.")


def menu():

    while True:

        print("\n==========================================")
        print(" SISTEMA DE REGISTO DE NASCIMENTOS")
        print("==========================================")
        print("1 - Registar nascimento")
        print("2 - Consultar registo")
        print("3 - Listar todos os nascimentos")
        print("4 - Apresentar estatísticas")
        print("5 - Sair")
        print("==========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_nascimento()

        elif opcao == "2":
            consultar_registo()

        elif opcao == "3":
            listar_nascimentos()

        elif opcao == "4":
            apresentar_estatisticas()

        elif opcao == "5":
            print("\nPrograma encerrado com sucesso.")
            break

        else:
            print("\nOpção inválida! Escolha uma opção de 1 a 5.")


menu()
