from Models import connection as db
import datetime
#função que faz a inserção de uma nova venda
def inserir(nomeVenda,valorVenda,dataVenda):
    ano, mes, dia = map(int, dataVenda.split('-'))
    date1 = datetime.date(ano, mes, dia)
    if date1 < datetime.date.today() and nomeVenda != '' and valorVenda > 0:

        conn = db.ConectarDB()
        mycursor = conn.cursor()
        sql = "INSERT INTO vendas VALUES (default,%s, %s,%s)"
        value = nomeVenda,valorVenda,dataVenda
        mycursor.execute(sql,value)
        print('Inserção feita com sucesso')
    else:
        print('Data maior que a atual ou valor da venda menor que 0')