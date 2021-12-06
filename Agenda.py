#Variáveis
Agenda = []

#Funções
def LeituraTXT():
    Arquivo = open('Agenda.txt', 'r')
    Agenda = Arquivo.readlines()
    Arquivo.close()

#---------------Programa Principal---------------#

    #Titulo
    print('-+-'*10)
    print('{:>22}'.format('Agenda  Pessoal'))
    print('-+-'*10)

    #Menu
    print('\n {:>16}\n'.format('Menu'))
    print('1- Exibir Contatos')
    print('2- Buscar')
    print('3- Inserir')
    print('4- Editar')
    print('5- Remover')
    print('6- Sair\n')
    print('-+-'*10)
    
    #Seleção
    Menu = str(input('\nOpção Desejada: ')).lower().strip()