from conectapet.controllers.clinica import Clinica
from conectapet.models.tutor import Tutor
from conectapet.models.veterinario import Veterinario

def menu():
    clinica = Clinica("ConectaPet", "00.000.000/0001-00")

    while True:
        print("\n=== Sistema ConectaPet ===")
        print("1. Cadastrar Tutor")
        print("2. Cadastrar Veterinário")
        print("3. Listar Tutores")
        print("4. Listar Veterinários")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            id_ = len(clinica.tutores) + 1
            tutor = Tutor(id_, nome, telefone, email, cpf, endereco)
            clinica.cadastrar_tutor(tutor)
            print("Tutor cadastrado com sucesso!")

        elif opcao == "2":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            crmv = input("CRMV: ")
            esp = input("Especialidade: ")
            id_ = len(clinica.veterinarios) + 1
            vet = Veterinario(id_, nome, telefone, email, crmv, esp)
            clinica.cadastrar_veterinario(vet)
            print("Veterinário cadastrado com sucesso!")

        elif opcao == "3":
            print("\n--- Tutores Cadastrados ---")
            for t in clinica.listar_tutores():
                print(t)

        elif opcao == "4":
            print("\n--- Veterinários Cadastrados ---")
            for v in clinica.listar_veterinarios():
                print(v)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
