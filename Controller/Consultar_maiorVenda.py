from Models import connection as db
#função que faz a busca da maior venda cadastrada
def consulta_maiorValor(tabela):
    conn = db.ConectarDB()
    mycursor = conn.cursor()
    mycursor.execute("select * from {0} order by valor desc; " .format(tabela))
    myresult = mycursor.fetchone()

    return myresult