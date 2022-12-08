# -*- coding: utf-8 -*-
import sqlite3

# Cria uma conexão e um cursor
con = sqlite3.connect('usuarios.db')
cur = con.cursor()

# Seleciona todos os registro
cur.execute('select * from usuarios')

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print('%d: %s(%s)' % rec)

# Fecha a conexão
con.close()
