# -*- coding: utf-8 -*-
import sqlite3

# Cria uma conexão e um cursor
con = sqlite3.connect('usuarios.db')
cur = con.cursor()

# Cria uma tabela
sql = 'create table usuarios' \
'(id integer primary key, '\
'nome varchar(100), '\
'endereço varchar(100), '\
'peso double(4,2), '\
'altura double(3,2)' \
'(peso / POW(altura, 2)) as imc)'
cur.execute(sql)

# Cria uma conexão e um cursor
con = sqlite3.connect('usuarios.db')
cur = con.cursor()

# Sentença  SQL para inserir registros
sql = 'insert into usuarios values (null, ?, ?, ?, ?)'

#Dados
recset = [('Fulano'), ('Rua Parana'), ('62'), ('1,90')]

#Insere os registros
for rec in recset:
    cur.execute(sql, rec)

# Confirma a transação
con.commit()

# Seleciona todos os registro
cur.execute('select * from usuarios')

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print('%d: %s(%s)' % rec)

# Fecha a conexão
con.close()
