from Models import connection as db
#função que exclui a venda selecionada no banco de dados
def excluir (id):
    conn = db.ConectarDB()
    mycursor = conn.cursor()
    sql = "DELETE FROM vendas WHERE id_venda = {0} ".format(id)

    mycursor.execute(sql)

    conn.commit()
    print('A exclusão foi realizada com sucesso')



excluir(2)