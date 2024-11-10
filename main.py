import sqlite3

table_client = """
    CREATE TABLE IF NOT EXISTS CLIENTE(
    ID_Cliente INT INDENTITY(1,1) PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Sobrenome VARCHAR(50) NOT NULL,
    RG CHAR(9) NOT NULL,
    Telefone CHAR(11),
    RUA VARCHAR(50),
    NUMERO VARCHAR(5),
    BAIRRO VARCHAR(50)
    )
"""

try:
    conexao = sqlite3.connect("floricultura.db")
    cursor = conexao.cursor()
    cursor.execute(table_client)
    conexao.commit()
    print("Alterções feita com sucesso!")
except Exception as e:
    print(f"Erro:{e}")
finally:
    if conexao:
        conexao.close()
        print("Conexão fechada com exito!")

