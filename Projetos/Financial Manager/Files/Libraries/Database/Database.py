import sqlite3
import pandas as pd

#Faz conexão com o banco de dados
Con = sqlite3.connect('Python\Projetos\Financial Manager\Files\Database\Database.db')

#Cursor
Cur = Con.cursor()

def Insert_Login(User, Password):
    #Insere User e Password na tabela Login
    Cur.execute(f'''
        INSERT INTO Login VALUES
        (NULL, "{User}", "{Password}")
    ''')

    #Executa as alterações
    Con.commit()

def Data_Login():
    #Obtem os dados da tela Login
    Data = Cur.execute('SELECT * FROM Login')

    #Passando os dados para um dataframe
    DataFrame_Login = pd.DataFrame(Data, columns = ['ID', 'User', 'Password', 'Logged'])
    return DataFrame_Login

def Delete_Login(ID):
    #Deleta o login do usuário
    Cur.execute(f'''
        DELETE FROM Login WHERE ID={ID}
    ''')

    #Executa as alterações
    Con.commit()