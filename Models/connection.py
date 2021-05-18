import mysql.connector
#Função que faz a conecxão com o banco de dados
def ConectarDB():
    conectar= mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        port='3306',
        database='registro_vendas'
    )
    return conectar