# Movere_vendas

----------------------- Projeto para empresa Movere Software -------------------------

1) Decidi usar Python por ser mais prático e dar uma treinada na linguagem.

2) Para rodar é necessario usar o pycharm e fazer a importação da biblioteca mysql.connector.
(quando abrir o programa no arquivo connection ira pedir para instalar)

3) Optei por usar conecxão ao banco de dados pois acho prático e versatil, usei o banco de dados MySQL.(abaixo o comando usado para criar a tabela)
	
	create table vendas (
	id_venda int auto_increment primary key,
	nome_cliente varchar(30) not null,
	valor float,
	data_venda date
	);

4) No arquivo connection é onde faço a conecxão com o banco de dados usando a função ConectarDB que dentro dessa função eu implemento a biblioteca mysql.connector.

5) No Arquivo Inserir_vendas é onde a função inserir executa o comando mysql "insert into vendas" do banco de dados é executado.

6) Em seguida no arquivo Excluir_vendas dentro da função excluir o comando mysql "DELETE FROM vendas WHERE id_venda" ira fazer a exclusão dos dados pelo id que o usuário digitar.

7) Depois vem o arquivo Consulta_vendas onde a função consultar onde executa o comando mysql "SELECT * FROM vendas" esse comando traz do banco de dados todas as vendas cadastradas no sistema.

8) Por fim no arquivo Consultar_maioVenda é onde está a função consulta_maiorValor que busca a venda de maior valor cadastrada usando o comando mysql "select * from vendas order by valor desc".

9) Na main é onde a magia acontece, usei o while para ter um menu retornavel equanto for verdade sempre volta para o menu,
tem um menu para o usuário escolher as ações que deseja realizar, onde a opção 1 faz com que o usuário realize a inserção de uma nova venda.

10) A opção 2 busca todas as vendas cadastradas pelo usuário mostrando o id, nome, valor e data da venda.

11) Na opção 3 é onde o usuário faz a exclusão de um registro de venda por meio do id.

12) E por fim na opção 4 é onde o sistema faz a busca da venda com o maior valor no banco de dados e retorna para o usuário.



