#Bibliotecas
import os
import time

#Class responsável por ler e atribuir valores no txt
class Agenda:

    #Faz apenas a leitura do arquivo e verifica se email se encontra
    def __init__(self, email):
        self.email = email
        self.lista = []

        with open('1-Trabalho-Agenda.txt', 'r') as lista:
            for linha in lista:
                self.lista.append(linha)
        lista.close()

        with open('1-Trabalho-Agenda.txt', 'r') as arquivo:
            for linha in arquivo:
                if self.email in linha:
                    return True
        arquivo.close()

        return False

    #Faz apenas a escrita de dados no arquivo
    def Escrita(self, nome, numero, email):
        self.nome = nome
        self.numero = numero
        with open('1-Trabalho-Agenda.txt', 'a') as arquivo:
            arquivo.write(str(self.nome) + '\n')
            arquivo.write(str(self.numero) + '\n')
            arquivo.write(str(self.email) + '\n')
        arquivo.close()

    #Essa função tem duas utilidades, sendo remover um contato e retornar uma lista
    #com todos os daddos de um contato
    def Remove(self, utilidade):
        auxiliar = []
        posicao = 0

        for linha in self.lista:
            if self.email in linha:
                posicao = posicao +1
                break
            else:
                posicao = posicao +1

        dados = posicao -3

        for controle in range(3):
            auxiliar.append(self.lista[dados])
            self.lista.pop(dados)

        if utilidade == True:
            with open('1-Trabalho-Agenda.txt', 'w') as arquivo:
                for linha in self.lista:
                    arquivo.write(str(linha))
                arquivo.close
        else:
            return auxiliar