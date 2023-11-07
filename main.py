banco_de_dados = []
matricula_atual = 0


def criarAluno(nome, idade, curso):
    # Permite alterar o valor de uma variavel global
    global matricula_atual
    matricula_atual += 1
    # Criando um aluno através de um dicionário
    aluno = {
        'matricula': matricula_atual,
        'nome': nome,
        'idade': idade,
        'curso': curso
    }
    return aluno


def adicionarAluno(nome, idade, curso):
    aluno = criarAluno(nome, idade, curso)
    banco_de_dados.append(aluno)
    print('Aluno adicionado com sucesso!')


def listarTodosAlunos():
    print('------ Alunos matriculados ------')
    for aluno in banco_de_dados:
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print('--------------------------------\n')


def editarAluno(matricula, nome, idade, curso):
    aluno = alunoExiste(matricula)

    if aluno:
        aluno['nome'] = nome
        aluno['idade'] = idade
        aluno['curso'] = curso
        print('Dados alterados com sucesso!')
    else:
        print('Matricula informada não econtrada!')


def alunoExiste(matricula):
    for aluno in banco_de_dados:
        if aluno['matricula'] == matricula:
            return aluno
    return False


def removerAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        banco_de_dados.remove(aluno)
        print('Aluno removido com sucesso!')

    else:
        print('Matricula não encontrada!')


def consultarAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        print('--- DADOS DO ALUNO ---')
        print(f'Matricula: {aluno["matricula"]}')
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade: {aluno["idade"]}')
        print(f'Curso: {aluno["curso"]}')
    else:
        print('Matricula não encontrada!')


def menu():
    while True:
        print('--- BEM VINDO AO MENU ESCOLAR ---')
        print('1 - Adicionar aluno')
        print('2 - Editar aluno')
        print('3 - Remover aluno')
        print('4 - Buscar aluno')
        print('5 - Listar todos os alunos')
        print('6 - Sair do sistema')
        opcao = input('Selecione uma opcao: ')

        if opcao == '1':
            print('--- ADICIONAR ALUNO ---')
            nome = input('Digite o nome do aluno: ')
            idade = input('Digite a idade do aluno: ')
            curso = input('Digite o nome do curso: ')
            adicionarAluno(nome, idade, curso)
            listarTodosAlunos()
        elif opcao == '2':
            print('--- EDITAR DADOS DO ALUNO ---')
            listarTodosAlunos()
            matricula = int(input('Digite o número da matricula do aluno que deseja editar: '))
            nome = input('Digite o nome do aluno: ')
            idade = input('Digite a idade do aluno: ')
            curso = input('Digite o nome do curso: ')
            editarAluno(matricula, nome, idade, curso)
            listarTodosAlunos()
        elif opcao == '3':
            listarTodosAlunos()
            matricula = int(input('Digite o número da matricula do aluno que deseja remover: '))
            removerAluno(matricula)
            listarTodosAlunos()
        elif opcao == '4':
            print('--- BUSCAR ALUNOS ---')
            matricula = int(input('Digite o número da matricula do aluno: '))
            consultarAluno(matricula)
        elif opcao == '5':
            listarTodosAlunos()
        elif opcao == '6':
            print('Você saiu do sistema!')
            break

        else:
            print('Opção inválida')



menu()
