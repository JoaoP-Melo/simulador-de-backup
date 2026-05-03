import abstract_factory.armazenamentos as am
import proxy.autentificacao as at
import memento.backup as bp


def criar_usuario():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = int(input("CPF: "))
    plano = input("Plano (FREE/PREMIUM): ").upper()

    return at.Usuario(nome, idade, cpf, plano)


def criar_arquivo():
    extensao = input("Extensão (txt, pdf...): ")
    tamanho = int(input("Tamanho: "))
    conteudo = input("Conteúdo: ")

    return bp.Arquivo(extensao, tamanho, conteudo)


def main():
    print("==== CRIAR USUÁRIO ====")
    usuario = criar_usuario()

    print("\n==== ESCOLHER ARMAZENAMENTO ====")
    tipo = input("1 - Local | 2 - Nuvem: ")

    if tipo == "1":
        fabrica = am.FactoryLocal()
    else:
        fabrica = am.FactoryNuvem()

    armazenamento = fabrica.criar_armazenamento()
    proxy = at.Proxy(usuario, armazenamento)

    backup = bp.Backup()
    gerente = bp.GerenciadorBackup(backup)

    arquivos = []

    while True:
        print("\n========= MENU =========")
        print("1 - Criar arquivo")
        print("2 - Adicionar arquivo ao backup")
        print("3 - Fazer backup")
        print("4 - Restaurar versão")
        print("5 - Listar backups")
        print("6 - Salvar (proxy)")
        print("7 - Carregar (proxy)")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            arquivo = criar_arquivo()
            arquivos.append(arquivo)
            print("Arquivo criado!")

        elif opcao == "2":
            if not arquivos:
                print("Nenhum arquivo criado.")
            else:
                for i, arq in enumerate(arquivos):
                    print(f"{i} - {arq.formato}")
                idx = int(input("Escolha o arquivo: "))
                print(backup.adicionar_arquivo(arquivos[idx]))

        elif opcao == "3":
            print(gerente.fazer_backup())

        elif opcao == "4":
            print(gerente.restaurar_versao())

        elif opcao == "5":
            print(gerente.imprimir_mementos())

        elif opcao == "6":
            print(proxy.salvar(gerente.mementos))

        elif opcao == "7":
            msg, pasta = proxy.carregar()
            print(msg)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

main()