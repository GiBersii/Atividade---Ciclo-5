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

# Fecha a conexão
con.close()


