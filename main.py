import sqlite3

table_client = """
    CREATE TABLE IF NOT EXISTS CLIENTE(
    ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(50) NOT NULL,
    Sobrenome VARCHAR(50) NOT NULL,
    RG CHAR(9) NOT NULL,
    Telefone CHAR(11),
    RUA VARCHAR(50),
    NUMERO VARCHAR(5),
    BAIRRO VARCHAR(50)
    )
"""

def addClient(nome:str,sobrenome:str,rg:str,telefone:str,rua:str,numero:str,bairro:str):
    insert = """
    INSERT INTO Cliente (nome,sobrenome,rg,telefone,rua,numero,bairro)
    VALUES (?,?,?,?,?,?,?)
"""
    return insert, (nome,sobrenome,rg,telefone,rua,numero,bairro)

try:
    conexao = sqlite3.connect("floricultura.db")
    cursor = conexao.cursor()
    command,params = addClient("Clary","Theme","12783734","119550877","rua jose paulo","1","Santo Antonio")
    cursor.execute(table_client)
    cursor.execute(command,params)
    conexao.commit()
    print("Alterções feita com sucesso!")
except Exception as e:
    print(f"Erro:{e}")
finally:
    if conexao:
        conexao.close()
        print("Conexão fechada com exito!")

