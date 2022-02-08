import pandas as pd
import mysql.connector
from mysql.connector import Error

margem_df = pd.read_csv('realizadoMargem.csv', sep=';')

try:
    conn = mysql.connector.connect(host='localhost',database='db_daju',user='root',password='')
    for i in range(margem_df.shape[0]):
        data = pd.to_datetime(margem_df['dt.transacao'][i], format='%d/%m/%Y').date()
        insert_info = "INSERT INTO `margem_produtos`(`id`, `nr_transacao`, `dt_transacao`, `cd_produto`, `ds_artigo`, `cst`, `cmv`, `cm_porcent`, `vlr_cm`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, margem_df['nr.transacao'][i],data,margem_df['Cod. Produto'][i],margem_df['Ds. Artigo'][i],margem_df['cst'][i], margem_df['CMV+CRIT_CALC.'][i],margem_df['%_CM'][i],margem_df['VLR._CM'][i])
        print(insert_info)
        cursor = conn.cursor()
        cursor.execute(insert_info)
        conn.commit()
        cursor.close()
except Error as erro:
    print("Falha ao inserir dados: {}".format(erro))
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()
        print('Conexão ao MySql Finalizada forçadamente!')