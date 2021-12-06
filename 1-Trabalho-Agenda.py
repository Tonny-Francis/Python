#Bibliotecas
import os
import time

#Variáveis/Listas/classes...
class Agenda:

    def Leitura(email):
        with open('1-Trabalho-Agenda.txt', 'r') as arquivo:
            for linha in arquivo:
                if email in linha:
                    return True
            arquivo.close()
            return False

    def Escrita(nome, numero, email):
        with open('1-Trabalho-Agenda.txt', 'a') as arquivo:
            arquivo.write(str(nome) + '\n')
            arquivo.write(str(numero) + '\n')
            arquivo.write(str(email) + '\n')
            arquivo.write(str(' ') + '\n')
        arquivo.close()
    
    def Remove(email):
        lista = []
        posicao = 0

        with open('1-Trabalho-Agenda.txt', 'r') as arquivo:
            for linha in arquivo:
                lista.append(linha)
            arquivo.close

        for linha in lista:
            if email in linha:
                posicao = posicao +1
                break
            else:
                posicao = posicao +1

        dados = posicao -3

        for controle in range(3):
            lista.pop(dados)

        with open('1-Trabalho-Agenda.txt', 'w') as arquivo:
            for linha in lista:
                arquivo.write(str(linha))
            arquivo.close
#Funções
def Adicionar():
    email = str(input('Email do Contato: '))
    auxiliar = Agenda.Leitura(email)

    while auxiliar != False:
        print('Email já Registrado!!')
        print('Tente Novamente')
        time.sleep(2)
        email = str(input('Email do Contato: '))

    nome = str(input('Nome do Contato: '))
    numero = str(input('Número do Contato: '))
    Agenda.Escrita(nome, numero, email)

    print('Contato {} Registrado com Sucessso!!'.format(nome))

def Editar():
    email = str(input('Digite o Email do Contato que\nDeseja Editar\n>> '))
    auxiliar = Agenda.Leitura(email)

    while auxiliar != True:
        print('Esse Contato não Existe!!')
        print('Tente Novamente')
        time.sleep(2)
        email = str(input('Digite o Email do Contato que\nDeseja Editar\n>> '))
    
    Agenda.Remove(email)




def Buscar():
    pass

def Listar():
    pass

def Remover():
    pass

def LimpaTela():
    if os.name == "nt":
        os.system("clear")
    else:
        os.system("cls")

def ProgramaPrincipal():
    controle = True
    while controle != False:
        #Titulo
        print('-+-'*10)
        print('{:>22}'.format('Agenda  Pessoal'))
        print('-+-'*10)

        #Menu
        print('\n {:>16}\n'.format('Menu'))
        print('1 - Inserir Contato')
        print('2 - Editar Contato')
        print('3 - Buscar Contato')
        print('4 - Listar Contatos')
        print('5 - Remover Contato')
        print('6 - Sair\n')
        print('-+-'*10)
        
        #Seleção
        menu = int(input('Opção Desejada: '))

        #Verificação
        if menu == 1:
            Adicionar()
        elif menu == 2:
            Editar()
        elif menu == 3:
            Buscar()
        elif menu == 4:
            Listar()
        elif menu == 5:
            Remover()
        elif menu == 6:
            LimpaTela()
            print('-+-'*10)
            print('{:>24}'.format('Fechando Agenda...'))
            print('-+-'*10)
            time.sleep(2)
            LimpaTela()
        else:
            LimpaTela()
            print('-+-'*10)
            print('{:>27}'.format('Opção desejada Inválida!'))
            print('-+-'*10)
            time.sleep(2)
            LimpaTela()

#Programa Principal
ProgramaPrincipal()