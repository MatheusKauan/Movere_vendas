from Models import connection as db
#função que faz a consulta de todas as vendas
def consulta(tabela):
    conn = db.ConectarDB()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM {0} " .format(tabela))
    myresult = mycursor.fetchall()

    return myresult