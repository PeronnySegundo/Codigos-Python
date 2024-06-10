import random
from variaveis import *
from esteticaDoTexto import *

#menu dos clientes
nome = ''
def login():
    global nome
    while True:
        logado = False
        validaçãoDeErros = False
        print('\033c')
        titulo('Login -Cine Pypoca-')
        print('[1] Entrar com uma conta existente')
        print('[2] Criar conta')
        tamanhoLinhaFuncao('Login -Cine Pypoca-')
        opcao = input('Opção desejada: ')
        if (opcao == '1'):
            print('\033c')
            titulo('Entrando em uma conta existente')
            nome = input('Nome de usuario: ') 
            senha = input('Senha: ')
            for usuario in listaUsuario:
                if (nome == usuario['nome'] and senha == usuario['senha']):
                    adm = usuario['adm']
                    logado = True
            if (logado == False):
                print('Nome de usuario ou senha Invalida')
                input('Aperte ENTER para continuar...')
            else:
                tamanhoLinhaFuncao('Entrando em uma conta existente')
                print('logado com sucesso!')
                tamanhoLinhaFuncao('Entrando em uma conta existente')
                input('Aperte ENTER para continuar...')
                if (adm == True):
                    menuAdm()
                else:
                    menuClient()
        elif (opcao == '2'):
            while True:
                print('\033c')
                titulo('Criação de conta')
                nome = input('Nome de usuário: ')
                senha = input('Senha: ')
                adm = input('Deseja ser administrador [S/N]? ')
                for verificarNome in listaUsuario:
                    if (nome == verificarNome['nome']):
                        validaçãoDeErros = True
                if (adm == 'S' or adm == 's'):
                    adm = True
                if (adm == 'N' or adm == 'n'):
                    adm = False
                if (adm != True and adm != False):
                    validaçãoDeErros = True
                    print('Digite valores validos')
                    input('Aperte enter para continuar...')
                    break
                if (len(nome) < 4):
                    print('Digite um nome de usuário maior!')
                    input('Aperte enter para continuar...')
                    break
                if (len(senha) < 3):
                    print('Digite uma senha mais segura!')
                    input('Aperte enter para continuar...')
                    break
                if (validaçãoDeErros == False):
                    listaUsuario.append({'nome': nome, 'senha': senha, 'adm': adm, 'assistidos': []})
                    tamanhoLinhaFuncao('Criação de conta')
                    print('Conta criada com sucesso')
                    tamanhoLinhaFuncao('Criação de conta')
                    input('Aperte ENTER para continuar...')
                    logado = True
                    if (adm == False):
                        menuClient()
                    else: 
                        menuAdm()
        else:
            print('\033c')
            titulo('Opção invalida')
            input('Aperte ENTER para continuar...')

def menuClient():
    while True:
        print('\033c')
        titulo('Menu pricipal')
        print('[1] Comprar ingressos')
        print('[2] Comprar itens na conveniência')
        print('[3] Ver estatísticas')
        print('[4] Deslogar')
        tamanhoLinhaFuncao('Menu pricipal')
        opcao = input('Opção desejada: ')
        if (opcao == '1'):
            comprarIngresso()
        elif (opcao == '2'):
            comprarItemLoja()
        elif (opcao == '3'):
            verStatus()
        elif (opcao == '4'):
            login()
        
def comprarIngresso():
    while True:
        print('\033c')
        titulo('Filmes em cartaz')
        contador = 0
        for filme in listaFilme:
            print(f'Título: {contador + 1}')
            print(f' Filme: {filme["filme"]}')
            print(f' Valor: {filme["preco"]}')
            print(f' Cadeiras diponíveis: {filme["cadeiras"]}')
            contador += 1
        tamanhoLinhaFuncao('Filmes em cartaz')
        opcao = input('Deseja compra ingressos [S/N]? ')
        if (opcao.lower() == 's'):
            opcao = int(input('Numero do filme para se comprar o ingresso: '))
            opcao -= 1
            quantidade = int(input('Quantidade de Ingressos: '))
            if ((listaFilme[opcao]['cadeiras']) < quantidade):
                titulo('Não há cadeiras sufucientes nesta sessão!')
                enter()
            else:
                (listaFilme[opcao]['cadeiras']) -= quantidade
                valor = (listaFilme[opcao]['preco'] * quantidade)
                tamanhoLinhaFuncao('Filmes em cartaz')
                print(f'Filme: {listaFilme[opcao]["filme"]}')
                print(f'Valor: {valor} R$')
                print('Compra Realizada com Sucesso!')
                tamanhoLinhaFuncao('Filmes em cartaz')
                input('aperte ENTER para continuar...')
                with open ('vendas.txt', 'a') as vendas:
                    vendas.write(f'----\nFilme: {listaFilme[opcao]["filme"]} / Valor: {valor} R$ / Usuário: {nome}\n')
        elif (opcao.lower() == 'n'):
            print('\033c')
            menuClient()

def comprarItemLoja():
    while True:
        print('\033c')
        titulo('Conveniêcia do Pypoca')
        contador = 0
        for item in listaLoja:
            print(f'Produto: {contador + 1}')
            print(f' Item: {item["produto"]}')
            print(f' Valor: {item["preco"]}')
            print(f' Estoque: {item["estoque"]}')
            contador += 1
        tamanhoLinhaFuncao('Conveniêcia do Pypoca')
        opcao = input('Deseja comprar algum item [S/N]? ')
        if (opcao.lower() == 'n'):
            print('\033c')
            menuClient()
        opcao = int(input('Numero do produto a ser comprado: '))
        opcao -= 1
        quantidade = int(input('Quantidade: '))
        if ((listaLoja[opcao]['estoque']) < quantidade):
            tamanhoLinhaFuncao('Conveniêcia do Pypoca')
            print('Não há essa quantidade disponível estoque!')
            tamanhoLinhaFuncao('Conveniêcia do Pypoca')
            input('Aperte enter para continuar...')
        else:
            tamanhoLinhaFuncao('Conveniêcia do Pypoca')
            (listaLoja[opcao]['estoque']) -= quantidade
            valor = (listaLoja[opcao]['preco'] * quantidade)
            print(f'Produto: {listaLoja[opcao]["produto"]}')
            print(f'Valor: {valor} R$')
            print('Compra Realizada com Sucesso!')
            tamanhoLinhaFuncao('Conveniêcia do Pypoca')
            input('Aperte enter para continuar...')
            with open ('vendas.txt', 'a') as vendas:
                vendas.write(f'----\nProduto: {listaLoja[opcao]["produto"]} / Valor: {valor} R$ / Usuário: {nome}\n')

def verStatus():
    print('\033c')
    titulo('Estatística')
    print('Aqui você pode ver os filmes assistidos e produtos comprados')
    with open ('vendas.txt', 'r') as arquivoDeVendas:
        arquivo = arquivoDeVendas.readlines()
    for linhas in arquivo:
        if (nome in linhas):
            print('----')
            print(linhas)
    tamanhoLinhaFuncao('Estatística')
    input('aperte ENTER para continuar...')
    tamanhoLinhaFuncao('Estatística')

#menu do Administrador
def menuAdm():
    print('\033c')
    titulo('Menu principal -Admin-')
    print('[1] Gerenciar cinema')
    print('[2] Gerenciar conveniência')
    print('[3] Gerenciar funcionarios')
    print('[4] Fluxo de caixa')
    print('[5] Deslogar')
    tamanhoLinhaFuncao('Menu principal -Admin-')
    opcao = input('Opção desejada: ')
    if (opcao == '1'):
        gerenciarCinema()
    elif (opcao == '2'):
        gerenciarConveniencia()
    elif (opcao == '3'):
        gerenciarFuncionarios()
    elif (opcao == '4'):
        fluxoDeCaixa()
    elif (opcao == '5'):
        login()

#funções da conveniência
def gerenciarConveniencia():
    print('\033c')
    titulo('Gerenciamento da Conveniência')
    print('[1] Adicionar Item')
    print('[2] Remover Item')
    print('[3] Editar Item')
    print('[4] Ver Estoque')
    print('[5] Pesquisar Item no Estoque')
    print('[6] Voltar')
    tamanhoLinhaFuncao('Gerenciamento da Conveniência')
    opcao = input('Opção desejada: ')
    if (opcao == '1'):
        adicionarItem()
    elif (opcao == '2'):
        removerItem()
    elif (opcao == '3'):
        editarItem()
    elif (opcao == '4'):
        verItens()
    elif(opcao == '5'):
        pesquisarItem()
    elif (opcao == '6'):
        menuAdm()

def adicionarItem():
    while True:
        print('\033c')
        titulo('Adicionar item a loja')
        itemNovo = input('Nome do Item: ')
        preçoNovo = float(input('Preço: '))
        estoqueNovo = float(input('Estoque: '))
        tamanhoLinhaFuncao('Adcionar item a loja')
        input('Aperte enter para continuar...')
        if (preçoNovo < 0 or estoqueNovo < 0):
            print('\033c')
            titulo('Digite valores validos')
            enter()
        else:
            listaLoja.append({'produto': itemNovo,'preco': preçoNovo,'estoque': estoqueNovo})
        print('\033c')
        titulo('Itens disponíveis na loja')
        contador = 0
        for item in listaLoja:
            print(f'Produto {contador + 1}')
            print(f' Item: {listaLoja[contador]["produto"]}')
            print(f' Valor: {listaLoja[contador]["preco"]} R$')
            print(f' Estoque: {listaLoja[contador]["estoque"]}')
            contador += 1
        tamanhoLinhaFuncao('Itens disponíveis na loja')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarConveniencia()

def removerItem():
    while True:
        print('\033c')
        titulo('Remover item da loja')
        contador = 0
        for item in listaLoja:
            print(f'Produto {contador + 1}')
            print(f' Item: {listaLoja[contador]["produto"]}')
            print(f' Valor: {listaLoja[contador]["preco"]}')
            print(f' Estoque: {listaLoja[contador]["estoque"]}')
            contador += 1
        tamanhoLinhaFuncao('Remover item da loja')
        opcao = int(input('Numero do produto a ser Removido: '))
        opcao -= 1
        print(f'Produto: {listaLoja[opcao]["produto"]}, Removido com sucesso!')
        del listaLoja[opcao]
        tamanhoLinhaFuncao('Remover item da loja')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarConveniencia()
        
def editarItem():
    while True:
        print('\033c')
        titulo('Editar item da loja')
        contador = 0
        for item in listaLoja:
            print(f'Produto {contador + 1}')
            print(f' Nome: {listaLoja[contador]["produto"]}')
            print(f' Valor: {listaLoja[contador]["preco"]}')
            print(f' Estoque: {listaLoja[contador]["estoque"]}')
            contador += 1
        tamanhoLinhaFuncao('Editar item da loja')
        opcao = int(input('Numero do produto a ser editado: '))
        opcao -= 1
        print('\033c')
        titulo(f'Editando {listaLoja[opcao]["produto"]}')
        print(f'Item: {listaLoja[opcao]["produto"]}')
        print(f'Valor: {listaLoja[opcao]["preco"]} R$')
        print(f'Estoque: {listaLoja[opcao]["estoque"]}')
        tamanhoLinhaFuncao('Editar item da loja')
        itemNovo = input('Novo nome: ')
        preçoNovo = float(input('Novo preço: '))
        estoqueNovo = float(input('Novo estoque:'))
        if (preçoNovo < 0 or estoqueNovo < 0):
            print('\033c')
            titulo('Digite valores validos')
            enter()
        else:
            del listaLoja[opcao]
            listaLoja.append({'produto': itemNovo ,'preco': preçoNovo,'estoque': estoqueNovo})
        print('\033c')
        titulo('Itens disponíveis na loja')
        contador = 0
        for filme in listaLoja:
            print(f'Produto {contador + 1}')
            print(f' Item: {listaLoja[contador]["produto"]}')
            print(f' Valor: {listaLoja[contador]["preco"]}')
            print(f' Estoque: {listaLoja[contador]["estoque"]}')
            contador += 1
        tamanhoLinhaFuncao('Itens disponíveis na loja')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarConveniencia()

def verItens():
    print('\033c')
    titulo('Itens disponíveis na loja')
    contador = 0
    for item in listaLoja:
        print(f'Produto {contador + 1}')
        print(f' Item: {listaLoja[contador]["produto"]}')
        print(f' Valor: {listaLoja[contador]["preco"]}')
        print(F' Estoque: {listaLoja[contador]["estoque"]}')
        contador += 1
    tamanhoLinhaFuncao('Itens disponíveis na loja')
    input('Aperte enter para continuar...')
    print('\033c')
    gerenciarConveniencia()

def pesquisarItem():
    while True:
        print('\033c')
        achado = False
        titulo('Pesquisar item')
        nomeItem = input('Nome do item a ser pesquisado: ')
        print('\033c')
        contador = 0
        for item in listaLoja:
            if (nomeItem == item['produto']):
                tamanhoLinhaFuncao('Pesquisar item')
                print(f'Item encontrado')
                print(f' Produto: {item["produto"]}')
                print(f' Valor: {item["preco"]}')
                print(f' Estoque: {item["estoque"]}')
                tamanhoLinhaFuncao('Pesquisar item')
                input('Aperte enter para continuar...')
                print('\033c')
                achado = True
            contador += 1
        if (achado == False):
            titulo('Item não encontrado!')
            input('Aperte enter para continuar...')
            print('\033c')
        titulo('Pesquisar Item')
        opcao = input('Deseja voltar ao menu [S/N]? ')
        if (opcao.lower() == 's'):
            gerenciarConveniencia()
        print('\033c')

#funções do cinema
def gerenciarCinema():
    print('\033c')
    titulo('Gerenciamento do cinema')
    print('[1] Adicionar Filme')
    print('[2] Remover Filme')
    print('[3] Editar Filme')
    print('[4] Filmes em cartaz')
    print('[5] Pesquisar Filme')
    print('[6] Voltar')
    tamanhoLinhaFuncao('Gerenciamento do cinema')
    opcao = input('Opção desejada: ')
    if (opcao == '1'):
        adicionarFilme()
    elif (opcao == '2'):
        removerFilme()
    elif (opcao == '3'):
        editarFilme()
    elif (opcao == '4'):
        verFilmes()
    elif (opcao == '5'):
        pesquisarFilme()
    elif (opcao == '6'):
        menuAdm()
    
def adicionarFilme():
    while True:
        print('\033c')
        titulo('Adicionar filmes')
        filmeNovo = input('Nome do Filme: ')
        preçoNovo = float(input('Preço do Ingresso: '))
        cadeiras = int(input('Numero de cadeiras disponíveis: '))
        tamanhoLinhaFuncao('Adicionar filmes')
        if (preçoNovo < 0 or cadeiras < 0):
            print('\033c')
            titulo('Digite valores validos')
            enter()
        else:
            listaFilme.append({'filme': filmeNovo,'preco': preçoNovo,'cadeiras': cadeiras})
        contador = 0
        print('\033c')
        titulo('Filmes em cartaz')
        contador = 0
        for filme in listaFilme:
            print(f'Filme {contador + 1}')
            print(f' Filme: {listaFilme[contador]["filme"]}')
            print(f' Valor: {listaFilme[contador]["preco"]} R$')
            print(f' Cadeiras diponíveis: {listaFilme[contador]["cadeiras"]}')
            contador += 1
        tamanhoLinhaFuncao('Adicionar filmes')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            gerenciarCinema()
            print('\033c')

def removerFilme():
    while True:
        print('\033c')
        titulo('Remover filmes')
        contador = 0
        for filme in listaFilme:
            print(f'Filme {contador + 1}')
            print(f' Filme: {listaFilme[contador]["filme"]}')
            print(f' Valor: {listaFilme[contador]["preco"]}')
            print(f' Cadeiras diponíveis: {listaFilme[contador]["cadeiras"]}')
            contador += 1
        tamanhoLinhaFuncao('Remover filmes')
        opcao = int(input('Numero do filme a ser Removido: '))
        opcao -= 1
        print(f'Filme: {listaFilme[opcao]["filme"]}, Removido com sucesso!')
        del listaFilme[opcao]
        tamanhoLinhaFuncao('Remover filmes')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarCinema()

def editarFilme():
    while True:
        print('\033c')
        titulo('Editar filmes em cartaz')
        contador = 0
        for filme in listaFilme:
            print(f'Filme {contador + 1}')
            print(f' Filme: {listaFilme[contador]["filme"]}')
            print(f' Valor: {listaFilme[contador]["preco"]}')
            print(f' Cadeiras diponíveis: {listaFilme[contador]["cadeiras"]}')
            contador += 1
        tamanhoLinhaFuncao('Editar filmes em cartaz')
        opcao = int(input('Numero do filme a ser editado: '))
        opcao -= 1
        print('\033c')
        titulo(f'Editando {listaFilme[opcao]["filme"]}')
        print(f'Filme: {listaFilme[opcao]["filme"]}')
        print(f'Valor: {listaFilme[opcao]["preco"]} R$')
        print(f'Cadeiras diponíveis: {listaFilme[opcao]["cadeiras"]}')
        tamanhoLinhaFuncao(f'Editando {listaFilme[opcao]["filme"]}')
        filmeNovo = input('Novo nome: ')
        preçoNovo = float(input('Novo preço: '))
        cadeiras = int(input('Numero de cadeiras disponíveis: '))
        if (preçoNovo < 0 or cadeiras < 0):
            print('\033c')
            titulo('Digite valores validos')
            enter()
        else:
            del listaFilme[opcao]
            listaFilme.append({'filme': filmeNovo,'preco': preçoNovo,'cadeiras': cadeiras})
        contador = 0
        tamanhoLinhaFuncao('Editar filmes em cartaz')
        input('Aperte enter para continuar...')
        print('\033c')
        tamanhoLinhaFuncao('Editar filmes em cartaz')
        contador = 0
        for filme in listaFilme:
            print(f'Filme {contador + 1}')
            print(f' Filme: {listaFilme[contador]["filme"]}')
            print(f' Valor: {listaFilme[contador]["preco"]}')
            print(f' Cadeiras diponíveis: {listaFilme[contador]["cadeiras"]}')
            contador += 1
        tamanhoLinhaFuncao('Editar filmes em cartaz')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarCinema()
    
def verFilmes():
    print('\033c')
    titulo('Filmes em cartaz')
    contador = 0
    for filme in listaFilme:
        print(f'Filme {contador + 1}')
        print(f' Filme: {listaFilme[contador]["filme"]}')
        print(f' Valor: {listaFilme[contador]["preco"]}')
        print(f' Cadeiras diponíveis: {listaFilme[contador]["cadeiras"]}')
        contador += 1 
    tamanhoLinhaFuncao('Filmes em cartaz')
    input('Aperte enter para continuar...')
    print('\033c')
    gerenciarCinema()

def pesquisarFilme():
    print('\033c')
    achado = False
    titulo('Pesquisar nome de filme')
    nomeFilme = input('Nome do filme a ser pesquisado: ')
    print('\033c')
    contador = 0
    for filme in listaFilme:
        if (nomeFilme == filme['filme']):
            tamanhoLinhaFuncao('Pesquisar nome de filme')
            print(f'Filme encontrado')
            print(f' Filme: {filme["filme"]}')
            print(f' Valor: {filme["preco"]}')
            print(f' Cadeiras Disponíveis: {filme["cadeiras"]}')
            tamanhoLinhaFuncao('Pesquisar nome de filme')
            input('Aperte enter para continuar...')
            print('\033c')
            achado = True
        contador += 1
    if (achado == False):
        titulo('Filme não encontrado!')
        input('Aperte enter para continuar...')
        print('\033c')
    titulo('Pesquisar nome de filme')
    opcao = input('Deseja voltar ao menu [S/N]? ')
    if (opcao.lower() == 's'):
        menuAdm()
    print('\033c')

#funções dos funcionários
def gerenciarFuncionarios():
    print('\033c')
    titulo('Gerenciar Funcionarios')
    print('[1] Contratar')
    print('[2] Dispensar')
    print('[3] Promover')
    print('[4] Funcionaios ativos')
    print('[5] Voltar')
    tamanhoLinhaFuncao('Gerenciar Funcionarios')
    opcao = input('Opção desejada: ')
    if (opcao == '1'):
        contratarFuncionaio()
    elif (opcao == '2'):
        dispensarFuncionario()
    elif (opcao == '3'):
        promoverFuncionario()
    elif (opcao == '4'):
        verFuncionarios()
    elif (opcao == '5'):
        menuAdm()

def contratarFuncionaio():
    while True:
        print('\033c')
        titulo('Contrtar Funcionário')
        nomeFuncionario = input('Nome: ')
        salario = float(input('Salário: '))
        escala = float(input('Horas por semana: '))
        tamanhoLinhaFuncao('Contrtar Funcionario')
        if (salario < 0 or escala < 0 or escala > 168):
            print('\033c')
            titulo('Digite valores validos')
            enter()
        else:
            listaFuncionarios.append({'nomeFuncionario': nomeFuncionario,'salario': salario,'escala': escala})
        contador = 0
        print('\033c')
        titulo('Contrtar Funcionario')
        contador = 0
        for empregado in listaFuncionarios:
            print(f'Empregado {contador + 1}')
            print(f' Funcionáio: {empregado["nomeFuncionario"]}')
            print(f' Salário: {empregado["salario"]} R$')
            print(f' Horas por semana: {empregado["escala"]}')
            contador += 1
        tamanhoLinhaFuncao('Contrtar Funcionario')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            gerenciarFuncionarios()
            print('\033c')

def dispensarFuncionario():
    while True:
        print('\033c')
        titulo('Dispensar Funcionário')
        contador = 0
        for empregado in listaFuncionarios:
            print(f'Empregado {contador + 1}')
            print(f' Funcionário: {empregado["nomeFuncionario"]}')
            print(f' Salário: {empregado["salario"]}')
            print(f' Horas por semana: {empregado["escala"]}')
            contador += 1
        tamanhoLinhaFuncao('Dispensar Funcionário')
        opcao = int(input('Numero do Servidor a ser dispensado: '))
        opcao -= 1
        print(f'Empregdo: "{listaFuncionarios[opcao]["nomeFuncionario"]}" dispensado com sucesso!')
        del listaFuncionarios[opcao]
        tamanhoLinhaFuncao('Dispensar Funcionario')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarFuncionarios()

def promoverFuncionario():
    while True:
        print('\033c')
        titulo('Promover Funcionário')
        contador = 0
        for empregdo in listaFuncionarios:
            print(f'Servidor {contador + 1}')
            print(f' Funcionário: {empregdo["nomeFuncionario"]}')
            print(f' Salário: {empregdo["salario"]}')
            print(f' Horas por semana: {empregdo["escala"]}')
            contador += 1
        tamanhoLinhaFuncao('Promover Funcionários')
        opcao = int(input('Número do Servidor a ser promovido: '))
        opcao -= 1
        print('\033c')
        titulo(f'Servidor {listaFuncionarios[opcao]["nomeFuncionario"]}')
        print(f'Funcionário: {listaFuncionarios[opcao]["nomeFuncionario"]}')
        print(f'Salário: {listaFuncionarios[opcao]["salario"]} R$')
        print(f'Horas por semana: {listaFuncionarios[opcao]["escala"]}')
        tamanhoLinhaFuncao(f'Promovendo {listaFuncionarios[opcao]["nomeFuncionario"]}')
        nomeFuncionario = input('Novo Nome: ')
        salario = float(input('Salário: '))
        escala = float(input('Horas por semana: '))
        del listaFuncionarios[opcao]
        if (salario < 0 or escala < 0 or escala > 168):
            print('\033c')
            titulo('Digite valores validos')
            enter()
        else:
            listaFuncionarios.append({'nomeFuncionario': nomeFuncionario,'salario': salario,'escala': escala})
        contador = 0
        enter()
        print('\033c')
        tamanhoLinhaFuncao('Promover Funcionários')
        contador = 0
        for servidor in listaFuncionarios:
            print(f'Servidor {contador + 1}')
            print(f' Funcionário: {servidor["nomeFuncionario"]}')
            print(f' Salário: {servidor["salario"]}')
            print(f' Horas por semana: {servidor["escala"]}')
            contador += 1
        tamanhoLinhaFuncao('Promover Funcionário')
        opcao = input('Deseja voltar ao Menu [S/N]? ')
        if (opcao.lower() == 's'):
            print('\033c')
            gerenciarCinema()

def verFuncionarios():
    print('\033c')
    titulo('Funcionários Ativos')
    contador = 0
    for empregado in listaFuncionarios:
        print(f'Servidor {contador + 1}')
        print(f' Funcionário: {empregado["nomeFuncionario"]}')
        print(f' Salário: {empregado["salario"]}')
        print(f' Escala: {empregado["escala"]}')
        contador += 1 
    tamanhoLinhaFuncao('Funcionários Ativos')
    input('Aperte enter para continuar...')
    print('\033c')
    gerenciarFuncionarios()

#fluxo de caixa
def fluxoDeCaixa():
    dia1 = random.randint(200, 350)
    dia2 = random.randint(200, 350)
    dia3 = random.randint(200, 350)
    dia4 = random.randint(200, 350)
    dia5 = random.randint(200, 350)
    dia6 = random.randint(200, 350)
    dia7 = random.randint(200, 350)
    print('\033c')
    titulo('Fluxo de caixa')
    quantidadeDePessoas = [dia1, dia2, dia3, dia4, dia5, dia6, dia7]
    capital = []
    for dias in range(7):
        valorMedioGasto = random.randint(15, 50)
        valorMedioGasto = quantidadeDePessoas[dias] * valorMedioGasto
        capital.append(valorMedioGasto)
    print(f'Segunda-Feira\n Fluxo de pessoas: {dia1}\n Fluxo de capital: {capital[0]}')
    print(f'Terça-Feira\n Fluxo de pessoas: {dia2}\n Fluxo de capital: {capital[1]}')
    print(f'Quarta-Feira\n Fluxo de pessoas: {dia3}\n Fluxo de capital: {capital[2]}')
    print(f'Quita-Feira\n Fluxo de pessoas: {dia4}\n Fluxo de capital: {capital[3]}')
    print(f'Sexta-Feira\n Fluxo de pessoas: {dia5}\n Fluxo de capital: {capital[4]}')
    print(f'Sabado-Feira\n Fluxo de pessoas: {dia6}\n Fluxo de capital: {capital[5]}')
    print(f'Domingo-Feira\n Fluxo de pessoas: {dia7}\n Fluxo de capital: {capital[6]}')
    tamanhoLinhaFuncao('Fluxo de caixa')
    print('Iformações sobre vendas')
    tamanhoLinhaFuncao('Fluxo de caixa')
    with open ('vendas.txt', 'r') as arquivoDeVendas:
        arquivo = arquivoDeVendas.read()
    print(arquivo)
    tamanhoLinhaFuncao('Fluxo de caixa')
    input('aperte ENTER para continuar...')
    menuAdm()
