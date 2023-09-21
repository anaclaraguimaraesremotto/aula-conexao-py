#cmd -> pip install oracledb

import oracledb

with oracledb.connect(user='rm97898', 
                      password='210904', 
                      dsn='oracle.fiap.com.br/orcl') as con:
    with con.cursor() as cur:
        dado = {'num' : 6000, 'nome' : 'Prof Pardal', 
                'sal' : 8500, 'departamento' : 'P&D'}
        sql = '''UPDATE RM97898.EMPREGADO SET NOME = :NOME, 
                SALARIO = :SAL, DEPARTAMENTO = :DEPARTAMENTO 
                WHERE NUMERO = :NUM'''
        cur.execute(sql, dado)
    
    con.commit()
