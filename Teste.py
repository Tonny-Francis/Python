

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

    
    print(lista)
    with open('1-Trabalho-Agenda.txt', 'w') as arquivo:
        for linha in lista:
            arquivo.write(str(linha))
        arquivo.close

email = input('Email: ')
Remove(email)