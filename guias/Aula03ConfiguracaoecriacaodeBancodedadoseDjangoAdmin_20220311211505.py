#################################################
# Acesso PostgreSQL e Criação do Banco de dados #
#################################################

# Acesse o postgres via PgAdmin, PSQL ou outro porgrama de sua escolha.

# Utilizando PgAdmin:
# Acesse o diretorio de instalação do PostgrSQL e utilize a interface 
# grafica para definir um nome de usuario, senha e os privilegios 
# necessarios. Como nao e recomendado utilizar o usuario de senha 
# de administador o recomendado é criar uma regra/usuario no postgres.
# defina um nome intuitivo como nome_do_projeto_que_voce_escolher_user
# e nome_do_projeto_que_voce_escolher_db.

# Criando um usuario para o banco de dados.

Servers >> PostgreSQL 13 >> Botão direito mouse >> create >> Login/Group Role

# Cria um banco de dados.

Servers >> PostgreSQL 13 >> Databases >> botao direito mouse >> create

# Vincule o usuario ao banco dea dados criado.

nome_do_projeto_que_voce_escolher_db >> Properties >> Security

# Utilizando PgSQL:
# Utilize linha de comandos e encontre o executavel no diretorio de
# instalação do PostgreSQL. Essas operações podem mudar dependendo 
# da versão ou do sistema operacional. Consulte os manuais e se 
# adapte ao ambiente instalado caso necessario.

psql (SQL Shell)

# O sistema solicitara as informações do banco uma de cada vez, 
# mas como elas não exitem aimda, voce somente precisa inserir 
# a informação de senha que sera para o usuario padrao "postgres"
# criado na instalacao do PostgreSQL (Caso tenha seguido as 
# orientacoes a sugestao de senha sera "123456". 

Server [localhost]: 
Database [postgres]: 
Port [5432]: 
Username [postgres]: 
Password for user postgres: 

# Como não e recomendado utilizar o usuario de senha de administador
# o recomendado e criar uma regra/usuario no postgres.

create role nome_de_usuairo_de_acesso_ao_banco with login password '123456';

# Crair um banco de dados no postgres

create database nome_banco_de_dados owner nome_de_usuairo_de_acesso_ao_banco;

# A seguir alguns comandos Postgres para verificar se o banco
# foi criado corretamente.

# Comando listar bancos de dados

\l

# Conectar a um banco de dados

\c nome_banco_de_dados

# Listar tabelas

\dt

# Listar colunas da tabela

\d nome_tabela
