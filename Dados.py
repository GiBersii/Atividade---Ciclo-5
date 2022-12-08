# -*- coding: utf-8 -*-

import sqlite3

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

# Fecha a conexão
con.close()

