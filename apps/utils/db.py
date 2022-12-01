import pandas as pd
import sqlite3

# df.to_sql("name",conn,if_exists='replace',index=False, index_label="id")
def write_to_table(table_name, df, behavior='replace'):
    con = sqlite3.connect('db.sqlite3')
    df.to_sql(table_name, con, if_exists=behavior, index=True, index_label='id')
    return